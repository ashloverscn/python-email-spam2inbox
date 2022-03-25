mail_server = 'imap.gmail.com'
account_id = 'admin@quicksupport.live'
password = 'tchwsmdjnyfdfyal'
TLS_port = '993'

import imaplib, email

conn = imaplib.IMAP4_SSL(mail_server, TLS_port)

try:
    (retcode, capabilities) = conn.login(account_id, password)
    
except:
    messages.error(request, 'Request Failed! Unable to connect to Mailbox. Please try again.')

conn.select('"[Gmail]/Spam"')

(retcode, messagess) = conn.uid('search', None, "ALL")
if retcode == 'OK':
    for num in messagess[0].split():
        typ, data = conn.uid('fetch', num,'(RFC822)')
        msg = email.message_from_bytes((data[0][1]))
        result = conn.uid('COPY', num, '"INBOX"')
        if result[0] == 'OK':
            mov, data = conn.uid('STORE', num , '+FLAGS', '(\Deleted)')
            conn.expunge()
      
conn.close()

print ("moving completed")
