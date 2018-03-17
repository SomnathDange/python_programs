import re

addressToVerify ='info@emailhippo.com1'
match = re.match('^[_a-z0-9-]+(\.[_a-z0-9-]+)*@[a-z0-9-]+(\.[a-z0-9-]+)*(\.[a-z]{2,4})$', addressToVerify)

if match == None:
    print('Bad Syntax')
    raise ValueError('Bad Syntax')
else:
    print "Email is Valid"
