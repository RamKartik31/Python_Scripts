import outlook
mail = outlook.Outlook()
mail.login(username='surendra.sambana@carrier.com',password='CARAPR2021*12345')
mail.select(CASE)
print(mail.unread())
'''

'''
import outlook
mail = outlook.Outlook()
mail.login(username='surendra.sambana@carrier.com',password='CARAPR2021*12345')
mail.inbox()
#print mail.unread()
'''

'''
from O365 import Account
credentials = ('surendra.sambana@carrier.com', 'CARAPR2021*12345')

account = Account(credentials)
if account.authenticate(scopes=['basic', 'message_all']):
   print('Authenticated!')
