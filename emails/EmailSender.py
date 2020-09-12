#!/usr/bin/env python
from exchangelib import DELEGATE, Account, Credentials, Message, Mailbox, HTMLBody, Configuration, NTLM
from exchangelib.protocol import BaseProtocol, NoVerifyHTTPAdapter
import urllib3
urllib3.disable_warnings()

SENDER = 'jiang.haoa@h3c.com'
SENDER_NAME = ''


def sendEmail(to, subject, body, cc = []):
    BaseProtocol.HTTP_ADAPTER_CLS = NoVerifyHTTPAdapter
    creds = Credentials(
        username='j16492',
        password='Jh203142'
    )
    config = Configuration(server='rndcas.h3c.com', credentials=creds, auth_type=NTLM)
    account = Account(
        primary_smtp_address=SENDER,
        config=config,
        autodiscover=False,
        access_type=DELEGATE
    )
    m = Message(
        account=account,
        subject=subject,
        body=HTMLBody(body),
        to_recipients = [Mailbox(email_address=email) for email in to],
        cc_recipients = [Mailbox(email_address=email) for email in cc]
    )
    m.send_and_save()