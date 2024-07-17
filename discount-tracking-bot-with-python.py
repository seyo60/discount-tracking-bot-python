import requests
from bs4 import BeautifulSoup
import smtplib
import time

url = 'https://www.trendyol.com/lego/marvel-hulkbuster-wakanda-savasi-76247-8-yas-ve-uzeri-cocuklar-icin-yapim-seti-385-parca-p-635014005?boutiqueId=634459&merchantId=968'

headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/126.0.0.0 Safari/537.36"
}

def fiyat_kontrolu():
    response = requests.get(url, headers=headers)
        
    soup = BeautifulSoup(response.text, 'html.parser')
    
    try:
        fiyat = soup.find('span', class_='prc-dsc').text
        yeni_fiyat = fiyat.replace(".", "").replace(",", ".")
        yeni_fiyat = float(yeni_fiyat.replace(" TL", "").strip())

        if yeni_fiyat < 1400:
            email_gonder(yeni_fiyat)

    except Exception as e:
        print("Fiyat kontrolünde bir hata oluştu:", e)

def email_gonder(yeni_fiyat):

    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.ehlo()
    server.starttls()
    server.ehlo()


    server.login('trial20022@gmail.com', '123456')

    baslik = 'Fiyat dususu!'
    uyari = f'Bekledigin fiyatin altina dustu! {yeni_fiyat} TL! Bu linkten kontrol et: {url}'

    icerik = f"Subject: {baslik}\n\n{uyari}"

    server.sendmail('trial2002@gmail.com','trial2001@gmail.com',icerik)

    print('Mesaj gonderildi')

    server.quit()


while True:
    fiyat_kontrolu()
    time.sleep(3600)  
