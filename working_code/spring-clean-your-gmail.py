import imaplib

# account credentials and other configs
imap_host = 'imap.gmail.com'
imap_port = '993'
imap_user = 'admin@quicksupport.live'
imap_pass = 'tchwsmdjnyfdfyal'
from_folder = '"[Gmail]/Spam"'
to_folder = '"INBOX"'

# create IMAP4 with SSL
imap = imaplib.IMAP4_SSL(immap_host, imap_port)
# authenticate
imap.login(imap_user, imap_pass)

# list all the mailboxes present
print(imap.list())
# SECTION 1: select the mailbox to delete emails from
imap.select(from_folder)

gmail_search = '"category:promotions NOT is: important"'
typ, [msg_ids] = imap.search(None, 'X-GM-RAW', gmail_search)
msg_count = len(msg_ids)
print("Found message count: ", msg_count)
if msg_count == 0:
    print("No new messages matching the criteria to be deleted.")
else:
    if isinstance(msg_ids, bytes):
        # if it's a bytes type, decode to str
        msg_ids = msg_ids.decode()

    # SECTION 2: imap store command allows us to batch perform an operation
    # on a bunch of comma-separated msg ids
    msg_ids = ','.join(msg_ids.split(' '))
    print("Moving to Trash using X-GM_LABELS.")
    imap.store(msg_ids, '+X-GM-LABELS', '\\Trash')

    # SECTION 3: Once all the required emails have been sent to Trash,
    # permanently delete emails marked as deleted from the selected folder
    print("Emptying Trash and expunge...")
    imap.select(to_folder)
    imap.store("1:*", '+FLAGS', '\\Deleted')  # Flag all Trash as Deleted
    imap.expunge()

# SECTION 4: close the mailbox once the task is done
print("Done. Closing connection & logging out.")
imap.close()
# logout
imap.logout()
