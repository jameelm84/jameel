emails= {}

print(f"emails=" , (emails))
print(type(emails))

emails ['ashley']= 'ashley@yahoo.com'
emails ['caiag']= 'cariag@yahoo.com'
emails ['elizabeth']= 'elizabeth@yahoo.com'
print(emails)
emails.pop('caiag')
print(emails)
# emailsss = emails.keys() # display the keys
# print(emailsss)
emails ['dalton'] = 'dalton@yahoo.com'
print(emails)
users = list(emails.keys())
print(f"users =" ,users)
emails_list_val = list(emails.values()) #return values not keys
print(f"emails value  list = ", emails_list_val)
pairs = list(emails.items())
print("pairs = " , pairs)