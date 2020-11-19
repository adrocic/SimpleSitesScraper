import requests
import settings
import smtplib
import time
import sys
import os
from bs4 import BeautifulSoup
from dotenv import load_dotenv

load_dotenv()
settings.init()

global flag
flag = True

global SLACK_WEBHOOK
SLACK_WEBHOOK = os.environ.get('SLACK_WEBHOOK')

global GOOGLE_APP_PASSWORD
GOOGLE_APP_PASSWORD = os.environ.get('GOOGLE_APP_PASSWORD')

global headers
headers = {
    "User-Agent": 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/86.0.4240.198 Safari/537.36'}


def send_email(url):
    subject = 'Xbox Available!'
    body = f'Click this link to get your Xbox! -> {url}'
    msg = f"Subject: {subject}\n\n{body}"

    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.ehlo()
    server.starttls()
    server.ehlo()
    server.login('anel.drocic@gmail.com', GOOGLE_APP_PASSWORD)
    server.sendmail(
        'anel.drocic@gmail.com',
        'anel.drocic@gmail.com',
        msg
    )
    server.quit()


def send_slack(url):
    slack_message = {
        "text": f"Hey! the Xbox Series X is available on `BestBuy.com`\n{url}"}
    requests.post(SLACK_WEBHOOK, json=slack_message)


def check_availability():
    global headers
    global purchaseButton
    for url in settings.testers:
        page = requests.get(url, headers=headers)
        soup = BeautifulSoup(page.content, 'html.parser')
        if 'bestbuy.com' in url:
            print('Checking BestBuy...')
            purchaseButton = soup.find("button", text="Add to Cart")
        elif 'walmart.com' in url:
            print('Checking Walmart...')
            purchaseButton = soup.find("button", text="Add to Cart")
        elif 'target.com' in url:
            print('Checking Target...')
            purchaseButton = soup.find("button", text="Pick it up")

        if purchaseButton is None:
            print('-> Still sold out!')
        else:
            print('Its available! Sending email and slack now, then terminating script.\n')
            send_email(url)
            send_slack(url)
            global flag
            flag = False


while flag:
    wait_time = 60 * 3

    check_availability()
    if flag:
        for remaining in range(wait_time, 0, -1):
            sys.stdout.write("\r")
            sys.stdout.write(
                "-> Checking again in {:2d} seconds.".format(remaining))
            sys.stdout.flush()
            time.sleep(1)
        print('\n')
