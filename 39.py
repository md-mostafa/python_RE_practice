#remove multiple spaces in a string
import re

str = 'Python    Exerises'

print('Original string : ', str)
print('Without extra spaces : ',re.sub(' +', ' ', str))


'''
=> re.sub(pattern, repl, string, count=0, flags=0)
    Return the string obtained by replacing the leftmost non-overlapping occurrences of pattern in string 
    by the replacement repl. 
'''