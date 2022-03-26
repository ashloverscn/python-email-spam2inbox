import imaplib
import email

imap_host = 'imap.gmail.com'
imap_user = 'admin@quicksupport.live'
imap_pass = 'tchwsmdjnyfdfyal'
from_folder = '"[Gmail]/Spam"'
to_folder = '"INBOX"'

imap = imaplib.IMAP4_SSL(imap_host,993)
imap.login(imap_user, imap_pass)
imap.select(from_folder)

(retcode, messagess) = imap.uid('search', None, "ALL")
if retcode == 'OK':
    for num in messagess[0].split():
        typ, data = imap.uid('fetch', num,'(RFC822)')
        msg = email.message_from_bytes((data[0][1]))
        result = imap.uid('COPY', num, to_folder)
        if result[0] == 'OK':
            mov, data = imap.uid('STORE', num , '+FLAGS', '(\Deleted)')
            imap.expunge()
      
imap.close()

print ("moving completed")
