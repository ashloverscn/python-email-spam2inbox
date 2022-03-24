import imaplib

# account credentials and other configs
# replace with you Gmail username and password
imap_host = 'imap.gmail.com'
username = "admin@quicksupport.live"
password = "tchwsmdjnyfdfyal"
folder = "[Gmail]/Spam"

# create IMAP4 with SSL
imap = imaplib.IMAP4_SSL(imap_host, 993)
# authenticate
imap.login(username, password)
# list all the mailboxes present
#print(imap.list())
# select the mailbox 
imap.select(folder)

typ, [msg_ids] = imap.search(None, 'X-GM-RAW', '""')
msg_count = len(msg_ids)
print("Found message count: ", msg_count)
if msg_count == 0:
    print("No new messages matching the criteria to be deleted.")
else:
    if isinstance(msg_ids, bytes):
        # if it's a bytes type, decode to str
        msg_ids = msg_ids.decode()

    imap.select(folder)
    imap.store("1:*", '+FLAGS', '\\Important')  # Flag all Trash as Deleted
    imap.expunge()

    
print("Done. Closing connection & logging out.")
imap.close()
imap.logout()

