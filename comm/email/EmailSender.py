from exchangelib import DELEGATE, Account, Credentials, Message, Mailbox, HTMLBody, Configuration, NTLM
from exchangelib.protocol import BaseProtocol, NoVerifyHTTPAdapter

def sendEmail(to, subject, body):
    BaseProtocol.HTTP_ADAPTER_CLS = NoVerifyHTTPAdapter
    creds = Credentials(
        username='j16492',
        password='Jh123456'
    )
    config = Configuration(server='rndcas.h3c.com', credentials=creds, auth_type=NTLM)
    account = Account(
        primary_smtp_address='jiang.haoa@h3c.com',
        config=config,
        autodiscover=False,
        access_type=DELEGATE
    )
    m = Message(
        account=account,
        subject=subject,
        body=HTMLBody(body),
        to_recipients = [Mailbox(email_address=to)]
    )
    m.send_and_save()