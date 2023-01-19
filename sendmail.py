
from email.message import EmailMessage
from smtplib import SMTP_SSL

password = open('password.txt').read().strip()

def send(subject, content, to=None, cc=None, bcc=None):

    if to  == None: to  = []
    if cc  == None: cc  = []
    if bcc == None: bcc = []
    if type(to ) == str: to  = [to ]
    if type(cc ) == str: cc  = [cc ]
    if type(bcc) == str: bcc = [bcc]

    from_email = 'fact.vomiting.zone@gmail.com'

    email_message = EmailMessage()
    if to:  email_message.add_header('To',  ', '.join(to ))
    if cc:  email_message.add_header('Cc',  ', '.join(cc ))
    if bcc: email_message.add_header('Bcc', ', '.join(bcc))

    email_message.add_header('From', from_email)
    email_message.add_header('Subject', subject)
    email_message.set_content(content)

    # Connect, authenticate, and send mail
    smtp_server = SMTP_SSL('smtp.gmail.com', port=465)
    smtp_server.login(from_email, password)
    smtp_server.sendmail(from_email,
                         to + cc + bcc, email_message.as_bytes())

    # Disconnect
    smtp_server.quit()
