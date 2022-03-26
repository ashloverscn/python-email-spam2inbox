########## gmail folders available ##########
##b'(\\HasNoChildren) "/" "INBOX"'
##b'(\\HasNoChildren) "/" "Knowledge"'
##b'(\\HasChildren \\Noselect) "/" "[Gmail]"'
##b'(\\All \\HasNoChildren) "/" "[Gmail]/All Mail"'
##b'(\\HasNoChildren \\Trash) "/" "[Gmail]/Bin"'
##b'(\\Drafts \\HasNoChildren) "/" "[Gmail]/Drafts"'
##b'(\\HasNoChildren \\Important) "/" "[Gmail]/Important"'
##b'(\\HasNoChildren \\Sent) "/" "[Gmail]/Sent Mail"'
##b'(\\HasNoChildren \\Junk) "/" "[Gmail]/Spam"'
##b'(\\Flagged \\HasNoChildren) "/" "[Gmail]/Starred"'
#############################################

imap_host = 'imap.gmail.com'
imap_port = '993'
imap_user = 'admin@quicksupport.live'
imap_pass = 'tchwsmdjnyfdfyal'
from_folder = '"[Gmail]/Spam"'
to_folder = '"INBOX"'

import sys, imaplib, email

imap = imaplib.IMAP4_SSL(imap_host, imap_port)

try:
    (retcode, capabilities) = imap.login(imap_user, imap_pass)
    
except:
    messages.error(request, 'Request Failed! Unable to connect to Mailbox. Please try again.')

imap.select(from_folder)

(retcode, messagess) = imap.uid('search', None, "ALL")
count = 0
if retcode == 'OK':
    sys.stdout.write ('moving mails from ' + from_folder + ' to ' + to_folder + '\n')
    sys.stdout.write ('Total ' + str(len(messagess[0].split())) + '\n')
    sys.stdout.write ('moving started\n')
    for num in messagess[0].split():
        typ, data = imap.uid('fetch', num,'(RFC822)')
        msg = email.message_from_bytes((data[0][1]))
        result = imap.uid('COPY', num, to_folder)
        if result[0] == 'OK':
            mov, data = imap.uid('STORE', num , '+FLAGS', '(\Deleted)')
            imap.expunge()
            count += 1
            sys.stdout.flush()
            sys.stdout.write("\r{0}".format(count))
            
if count == 0:
    sys.stdout.write('nothing to move')

imap.close()

sys.stdout.write ('\nmoving completed')

input("\nPress enter to exit ;)")


