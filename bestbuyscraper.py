import requests
from bs4 import BeautifulSoup
import smtplib
import time
import sys

global flag
flag = True


def check_availability():

    print('\nAvailability check of the Xbox Series X on bestbuy.com')
    BEST_BUY_URL = 'https://www.bestbuy.com/site/microsoft-xbox-series-x-1tb-console-black/6428324.p?skuId=6428324'
    SLACK_WEB_HOOK = 'https://hooks.slack.com/services/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'

    headers = {
        "User-Agent": 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/86.0.4240.198 Safari/537.36'}
    slack_message = {
        "text": f"Hey! the Xbox Series X is available on `BestBuy.com`\n{BEST_BUY_URL}"}

    page = requests.get(BEST_BUY_URL, headers=headers)
    soup = BeautifulSoup(page.content, 'html.parser')
    purchasebutton = soup.find(class_="add-to-cart-button").get_text()

    def send_slack():
        requests.post(SLACK_WEB_HOOK, json=slack_message)

    def send_email():
        server = smtplib.SMTP('smtp.gmail.com', 587)
        server.ehlo()
        server.starttls()
        server.ehlo()
        server.login('anel.drocic@gmail.com', 'yuqwicshwguxvmxj')
        subject = 'Xbox Available!'
        body = 'Click this link to get your Xbox! -> https://www.bestbuy.com/site/microsoft-xbox-series-x-1tb-console-black/6428324.p?skuId=6428324'
        msg = f"Subject: {subject}\n\n{body}"
        server.sendmail(
            'anel.drocic@gmail.com',
            'anel.drocic@gmail.com',
            msg
        )
        print('Its available! Sending email and slack now, then terminating script.\n')
        server.quit()

    if(purchasebutton == "Sold Out"):
        print('-> Still sold out!')
    else:
        send_email()
        send_slack()
        global flag
        flag = False


while(flag):
    wait_time = 60 * 3

    check_availability()
    if(flag):
        for remaining in range(wait_time, 0, -1):
            sys.stdout.write("\r")
            sys.stdout.write(
                "-> Checking again in {:2d} seconds.".format(remaining))
            sys.stdout.flush()
            time.sleep(1)
        print('\n')
