import imaplib

# account credentials and other configs
# replace with you Gmail username and password
username = "admin@quicksupport.live"
password = "tchwsmdjnyfdfyal"
folderToDeleteEmailsFrom = '"[Gmail]/All Mail"'
trashFolder = '[Gmail]/Trash'

# create IMAP4 with SSL
imap = imaplib.IMAP4_SSL("imap.gmail.com", 993)
# authenticate
imap.login(username, password)

# list all the mailboxes present
print(imap.list())
# SECTION 1: select the mailbox to delete emails from
imap.select(folderToDeleteEmailsFrom)

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
    imap.select(trashFolder)
    imap.store("1:*", '+FLAGS', '\\Deleted')  # Flag all Trash as Deleted
    imap.expunge()

# SECTION 4: close the mailbox once the task is done
print("Done. Closing connection & logging out.")
imap.close()
# logout
imap.logout()
