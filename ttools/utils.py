import smtplib
from email.message import EmailMessage

import twitter

from ttools.settings import (
    ACCESS_TOKEN_KEY, ACCESS_TOKEN_SECRET,
    CONSUMER_KEY, CONSUMER_SECRET,
    EMAIL_ADDRESS, EMAIL_SENDER,
)


def get_client():
    return twitter.Api(
        consumer_key=CONSUMER_KEY,
        consumer_secret=CONSUMER_SECRET,
        access_token_key=ACCESS_TOKEN_KEY,
        access_token_secret=ACCESS_TOKEN_SECRET,
    )


def send_email(title, message):
    if not EMAIL_ADDRESS:
        return

    msg = EmailMessage()
    msg.set_content(message)

    msg['Subject'] = title
    msg['From'] = EMAIL_SENDER
    msg['To'] = EMAIL_ADDRESS

    s = smtplib.SMTP('localhost')
    s.send_message(msg)
    s.quit()
