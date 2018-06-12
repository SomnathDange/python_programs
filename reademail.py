from password import *
import getpass, poplib
user = 'Somnath.Dange@xyz.com'
Mailbox = poplib.POP3_SSL('outlook.office365.com', '995')
Mailbox.user(user)
Mailbox.pass_(password)
numMessages = len(Mailbox.list()[1])
print numMessages
#for i in range(numMessages):
#    for msg in Mailbox.retr(i+1)[1]:
#        print msg
Mailbox.quit()



