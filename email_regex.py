import re
input=input()
email=re.match(r'^.+@\w+\.\w{2,3}$',input)
a=re.match(r'^(.+)@\w+\.\w{2,3}$',input)
b=re.match(r'^.+@(\w+)\.\w{2,3}$',input)
c=re.match(r'^.+@\w+\.(\w{2,3})$',input)
if email==None:
    print('WRONG')
elif a.string.isalnum()==False or b.string.isalnum()==False or c.string.isalpha()==False:
    print('WRONG')
elif a.string.isalnum()==True and b.string.isalnum()==True and c.string.isalpha()==True:
    print('OK')
