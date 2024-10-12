from bs4 import BeautifulSoup

#whats does request do?
import requests

import time
import datetime
import pandas as pd
import smtplib

# Web link to scrape
URL = "https://www.amazon.com.au/Crucial-BX500-2TB-2-5-SATA3/dp/B07YD5F561/ref=sr_1_6?crid=XCSJCTZSOIO4&dib=eyJ2IjoiMSJ9.vUgKkI1UoeyulLXJYhdChEo56Ph2k5lwJmzgTouWXMXzzpcuvqim9FN7cHLrwPgGrEzPpjEspmlb51d-33QlII0BQOr5bd_B7Zn7qP6Hm6KhqUwvHipkthK1YsJG11Y37pn7kU6j_DtyTtFjt0oaTQ2BPQtEP4bgmcxPSThfKCGx7xAzr2DYGTlOh3Zr2DGy3JZnPODdnkMhnlxi0egqRmWVNdBYy7re0uMGS6WV0PGhIWczzpeODmgsb4GPUCWzGim6EMZUMfSW1VOlgOkdhSHcgzR5-AIlv1pq0fNfhkI.w7atzyLzDWyHBh7jedYYUIKLiG5Du-dPr9iFWQWSAEI&dib_tag=se&keywords=ssd&qid=1728216546&sprefix=s%2Caps%2C269&sr=8-6"

# headers for user agent
headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/129.0.0.0 Safari/537.36"}
#get the url

page = requests.get(URL, headers=headers)

# Bring in the Data
soup1 = BeautifulSoup(page.content, "html.parser")

# Soup.prettify formats and makes it easier to read
soup2 = BeautifulSoup(soup1.prettify(), "html.parser")

#.get_text will remove the class and ids printing only the item
title = soup2.find(id='productTitle').get_text()
# trying id="aok-offscreen" didnt work no return

# Method 1: below works which i got from stack overflow i understand it as searching span with aok-offscreen inside class
#price = soup2.find("span", {"class": "aok-offscreen"})

# Method 2: insipred from method 1, by searching aok-offscreen inside span or search span then matching aok-offscreen
price = soup2.find("span","aok-offscreen").get_text()

#Strips the first digit and displays everything onwards
price = price.strip()[1:]

# Strips the Empty Space
title = title.strip()
print(title)
print(price)

import datetime
today = datetime.date.today()

print(today)

#Import excel and defining header for cell 1 as title and cell as price
# Taking data that we scraped from title and price and writing it as data
import csv
header = ['Title', 'Price', 'Date']
data = [title, price, today]

#Df just the name however the full code allows to read in terminal

df = pd.read_csv('D:\Python\Scraper\Amazon_Scraper.csv')

print(df)

# with open means saves as followed by in that directory and file name blah blah, A+ Appends and adds new data
with open('D:\Python\Scraper\Amazon_Scraper.csv', 'a+', newline='', encoding='UTF8') as f:

    writer = csv.writer(f)
    writer.writerow(data)


def check_price():
    
    URL = "https://www.amazon.com.au/Crucial-BX500-2TB-2-5-SATA3/dp/B07YD5F561/ref=sr_1_6?crid=XCSJCTZSOIO4&dib=eyJ2IjoiMSJ9.vUgKkI1UoeyulLXJYhdChEo56Ph2k5lwJmzgTouWXMXzzpcuvqim9FN7cHLrwPgGrEzPpjEspmlb51d-33QlII0BQOr5bd_B7Zn7qP6Hm6KhqUwvHipkthK1YsJG11Y37pn7kU6j_DtyTtFjt0oaTQ2BPQtEP4bgmcxPSThfKCGx7xAzr2DYGTlOh3Zr2DGy3JZnPODdnkMhnlxi0egqRmWVNdBYy7re0uMGS6WV0PGhIWczzpeODmgsb4GPUCWzGim6EMZUMfSW1VOlgOkdhSHcgzR5-AIlv1pq0fNfhkI.w7atzyLzDWyHBh7jedYYUIKLiG5Du-dPr9iFWQWSAEI&dib_tag=se&keywords=ssd&qid=1728216546&sprefix=s%2Caps%2C269&sr=8-6"
    headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/129.0.0.0 Safari/537.36"}
    page = requests.get(URL, headers=headers)

    soup1 = BeautifulSoup(page.content, "html.parser")

    soup2 = BeautifulSoup(soup1.prettify(), "html.parser")

    title = soup2.find(id='productTitle').get_text()

    price = soup2.find("span","aok-offscreen").get_text()
    price = price.strip()[1:]
    title = title.strip()



    import datetime
    today = datetime.date.today()

    import csv
    header = ['Title', 'Price', 'Date']
    data = [title, price, today]
    
    with open('D:\Python\Scraper\Amazon_Scraper_Add.csv', 'a+', newline='', encoding='UTF8') as f:
        writer = csv.writer(f)
        writer.writerow(data)
#checks price every 5 seconds    
while (True):
        check_price()
        time.sleep(5)
        df = pd.read_csv('D:\Python\Scraper\Amazon_Scraper.csv')
        print(df)

    