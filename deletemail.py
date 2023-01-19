
import imaplib

password = open('password.txt').read().strip()

def delete(id, mailbox = '[Gmail]/All'):

    # Connect to inbox
    imap_server = imaplib.IMAP4_SSL(host='imap.gmail.com')
    imap_server.login('fact.vomiting.zone@gmail.com', password)
    imap_server.select()  # Default is `INBOX`

    # Delete an email
    imap_server.store(id, '+FLAGS', '\Deleted')
    # Expunge after marking emails deleted
    imap_server.expunge()

    imap_server.close()
    imap_server.logout()
