#modules
import imaplib
import email

#credentials
imap_host = 'imap.gmail.com'
imap_port = '993'
imap_user = 'admin@quicksupport.live'
imap_pass = 'tchwsmdjnyfdfyal'
from_folder = '"INBOX"'
to_folder = '"[Gmail]/Spam"'

# https://www.systoolsgroup.com/imap/
gmail_host= 'imap.gmail.com'

#set connection
mail = imaplib.IMAP4_SSL(imap_host,imap_port)

#login
mail.login(imap_user, imap_pass)

#select inbox
mail.select(from_folder)
#select specific mails
##_, selected_mails = mail.search(None, '(FROM "admin@quicksupport.live")')
_, selected_mails = mail.search(None, 'ALL')

#total number of mails from specific user
##print("Total Messages from admin@quicksupport.live:" , len(selected_mails[0].split()))
print("ALL" , len(selected_mails[0].split()))

for num in selected_mails[0].split():
    _, data = mail.fetch(num , '(RFC822)')
    _, bytes_data = data[0]

    #convert the byte data to message
    email_message = email.message_from_bytes(bytes_data)
    print("\n===========================================")

    #access data
    print("Subject: ",email_message["subject"])
    print("To:", email_message["to"])
    print("From: ",email_message["from"])
    print("Date: ",email_message["date"])
    for part in email_message.walk():
        if part.get_content_type()=="text/plain" or part.get_content_type()=="text/html":
            message = part.get_payload(decode=True)
            print("Message: \n", message.decode())
            print("==========================================\n")
            break
