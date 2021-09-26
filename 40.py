#remove all whitespaces from a string

import re

text1 = '       Akash            Is  The          Best               '

print('Original string : ',text1)
print('Without extra spaces : ', re.sub(r'\s+', '', text1))


'''
=> \s
    For Unicode (str) patterns:
    Matches Unicode whitespace characters (which includes [ \t\n\r\f\v], and also many other characters,
    
=> re.sub(pattern, repl, string, count=0, flags=0)
    Return the string obtained by replacing the leftmost non-overlapping occurrences of pattern in string by the replacement repl. 


'''
