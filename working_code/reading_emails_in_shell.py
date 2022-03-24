#modules
import imaplib
import email

#credentials
username ="admin@quicksupport.live"

#generated app password
app_password= "tchwsmdjnyfdfyal"

# https://www.systoolsgroup.com/imap/
gmail_host= 'imap.gmail.com'

#set connection
mail = imaplib.IMAP4_SSL(gmail_host)

#login
mail.login(username, app_password)

#select inbox
mail.select("[Gmail]/Spam")

#### print all folder labels
##for i in imap.list()[1]:
##    print(i)
##

########## what i got in folders ##########
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

