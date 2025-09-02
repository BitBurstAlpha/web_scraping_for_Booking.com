# This app scrap data from booking.com

import requests
from bs4 import BeautifulSoup
import lxml
import csv
import time
import random

def web_scrapper1(web_url,f_name):

    #Greeting
    print("Thank you sharing the url and file name!\n⏳\nWeb Scrapping is starting!")
    num = random.randint(3,7)
    #Processing
    time.sleep(num)

    header = {'User-Agent':'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/139.0.0.0 Safari/537.36'}

    response = requests.get(web_url, headers=header)



    if response.status_code == 200:
        print("Connected to the website!!!!")
        print('-----------------------------')
        html_content = response.text

        #creating soup
        soup =  BeautifulSoup(html_content, 'lxml')
        #print(soup.prettify())

        #Main Containers
        hotel_divs = soup.find_all('div',role="listitem")

        with open(f"{f_name}.csv",'w',encoding='utf-8') as file_csv:
            writer = csv.writer(file_csv)

            #adding header
            writer.writerow(['hotel_name','location','price','rating','score','total_review',''])
        
        #Process
            for hotel in hotel_divs:
                hotel_name = hotel.find('div', class_="b87c397a13 a3e0b4ffd1").text.strip() # type: ignore
                hotel_name if hotel_name else "NA"

                location = hotel.find('span', class_="d823fbbeed f9b3563dd4").text.strip() # type: ignore
                location if location else "NA"

                price = hotel.find('span', class_="b87c397a13 f2f358d1de ab607752a2").text.strip().replace("£",'') # type: ignore
                price if price else "NA"

                rating = hotel.find('div', class_="f63b14ab7a f546354b44 becbee2f63").text.strip() # type: ignore
                rating if rating else "NA"

                score = hotel.find('div', class_="f63b14ab7a dff2e52086").text.strip().split(' ')[-1] # type: ignore
                score if score else "NA"

                total_review = hotel.find('div', class_="fff1944c52 fb14de7f14 eaa8455879").text.strip() # type: ignore
                total_review if total_review else "NA"

                link = hotel.find('a',href=True).get('href')# type: ignore
                link if link else "NA"

                #Saving the file
                writer.writerow([hotel_name,location,price,rating,score,total_review,link])

            print("Web Scrapped Done!!!!")
            print('-----------------------------')


    else:
        print(f"Connection Fails{response.status_code}")# Check status code to check weather is correct or not

#if using this script directly than below task will be executed

if __name__ == '__main__':

    url = input("Please Enter URL?: ")
    f_n = input("Please Enter File Name?: ")

    # calling the function
    web_scrapper1(url,f_n)

