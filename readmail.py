
from email import message_from_bytes
import imaplib

password = open('password.txt').read().strip()

def read(mailbox = '[Gmail]/All'):

    messages = []

    # Connect to inbox
    imap_server = imaplib.IMAP4_SSL(host='imap.gmail.com')
    imap_server.login('fact.vomiting.zone@gmail.com', password)
    imap_server.select(mailbox)  # Default is `INBOX`

    # Find all emails in inbox
    _, message_numbers_raw = imap_server.search(None, 'ALL')
    for message_number in message_numbers_raw[0].split():
        _, msg = imap_server.fetch(message_number, '(RFC822)')

        # Parse the raw email message in to a convenient object
        message = message_from_bytes(msg[0][1])

        content = message.get_payload()
        if type(content) == list:
            content = content[0].get_payload().split('.com>')[0].split('\r\n\r\nOn ')[0]

        messages.append({
            "subject": message["subject"],
            "from": message["from"],
            "to": message["to"],
            "cc": message["cc"],
            "bcc": message["bcc"],
            "content": content.strip(),
            "id": message_number,
            "folder": mailbox,
        })

    return messages
