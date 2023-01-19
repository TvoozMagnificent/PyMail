
import imaplib

def folders():

    imap_server = imaplib.IMAP4_SSL(host='imap.gmail.com')
    imap_server.login('fact.vomiting.zone@gmail.com', 'cesfdtyyqkfuvdrp')

    _, folders = imap_server.list()
    _ =  [_.decode().split()[-1].strip('"') for _ in folders]

    imap_server.logout()

    return _
