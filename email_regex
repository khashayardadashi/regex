import re
input=input()
email=re.match(r'^.+@\w+\.\w{2,3}$',input)
a=re.match(r'^(.+)@\w+\.\w{2,3}$',input)
b=re.match(r'^(.+)@(\w+)\.\w{2,3}$',input)
c=re.match(r'^.+@\w+\.(\w{2,3})$',input)
if email==None:
    print('WRONG')
elif a.string.isidentifier()==True and b.string.isidentifier()==True and c.string.isidentifier()==True:
    print('OK')
elif a.string.isidentifier()==False or b.string.isidentifier()==False or c.string.isidentifier()==False:
    print('WRONG')
