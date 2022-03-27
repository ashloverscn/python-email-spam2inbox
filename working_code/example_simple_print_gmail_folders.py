########## what i got as folders ##########
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

import imaplib

imap_host = 'imap.gmail.com'
imap_port = '993'
imap_user = 'admin@quicksupport.live'
imap_pass = 'tchwsmdjnyfdfyal'

# connect to host using SSL
imap = imaplib.IMAP4_SSL(imap_host,imap_port)

## login to server
imap.login(imap_user, imap_pass)

## print all folder labels
for i in imap.list()[1]:
    print(i)
