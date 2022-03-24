# caso sua caixa de emails esteja muito cheia
# use esta variável para aumentar o limite do
# tamanho da resposta
import imaplib

imaplib._MAXLINE = 1000000

EMAIL = 'admin@quicksupport.live'
PASSWORD = 'tchwsmdjnyfdfyal'
SERVER = 'imap.gmail.com'

mail = imaplib.IMAP4_SSL(SERVER)
mail.login(EMAIL, PASSWORD)
# select the box you want to clean
mail.select('inbox')

status, search_data = mail.search(None, 'ALL')

mail_ids = []

for block in search_data:
    mail_ids += block.split()

# define the range for the operation
start = mail_ids[0].decode()
end = mail_ids[-1].decode()

# move the emails to the trash
# this step is Gmail specific because
# it doesn't allow excluding messages
# outside the trash
mail.store(f'{start}:{end}'.encode(), '+X-GM-LABELS', '\\Trash')

# access the Gmail trash
mail.select('[Gmail]/Trash')
# mark the emails to be deleted
# mail.store("1:*", '+FLAGS', '\\Deleted')

# remove permanently the emails
mail.expunge()

# close the mailboxes
mail.close()
# close the connection
mail.logout()
