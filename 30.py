#Abbreviate 'Road' as 'Rd.' in a given string

import re
street = '21 Ramkrishna Road'
print(street)

pattern = 'Road$'
repl = 'Rd.'
print(re.sub(pattern, repl, street))



'''
=> re.subn(pattern, repl, string, count=0, flags=0)
   Perform the same operation as sub(), 
   but return a tuple (new_string, number_of_subs_made).
'''