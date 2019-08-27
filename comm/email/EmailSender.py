from exchangelib import Account, Credentials
from exchangelib.folders import Message, Mailbox

email = 'john@example.com'
password = 'topsecret'

a = Account(email, credentials=Credentials(email, password), autodiscover=True)

# If you don't want a local copy
m = Message(
    account=a,
    subject='Daily motivation',
    body='All bodies are beautiful',
    to_recipients=[Mailbox(email_address='erik@cederstrand.dk')]
)
m.send()

# Or, if you want a copy in the 'Sent' folder
m = Message(
    account=a,
    folder=a.sent,
    subject='Daily motivation',
    body='All bodies are beautiful',
    to_recipients=[Mailbox(email_address='erik@cederstrand.dk')]
)
m.send_and_save()