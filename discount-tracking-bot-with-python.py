import requests
from bs4 import BeautifulSoup
import smtplib
import time

url = 'https://www.trendyol.com/lego/marvel-hulkbuster-wakanda-savasi-76247-8-yas-ve-uzeri-cocuklar-icin-yapim-seti-385-parca-p-635014005?boutiqueId=634459&merchantId=968'

headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/126.0.0.0 Safari/537.36"
}

def check_price():
    response = requests.get(url, headers=headers)
        
    soup = BeautifulSoup(response.text, 'html.parser')
    
    try:
        price = soup.find('span', class_='prc-dsc').text
        new_price = price.replace(".", "").replace(",", ".")
        new_price = float(new_price.replace(" TL", "").strip())

        if new_price < 1400:
            send_email(new_price)

    except Exception as e:
        print("There was an error in the price check:", e)

def send_email(new_price):

    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.ehlo()
    server.starttls()
    server.ehlo()


    server.login('trial20022@gmail.com', '123456')

    header = 'Price drop!'
    warning = f'The price you expected fell below! {new_price} TL! Check it out from this link: {url}'

    msgcontent = f"Subject: {header}\n\n{warning}"

    server.sendmail('trial2002@gmail.com','trial2001@gmail.com',msgcontent)

    print('Message sent')

    server.quit()


while True:
    fiyat_kontrolu()
    time.sleep(3600)  
