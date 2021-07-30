#separate and print the numbers of a given string.

import re
text ="Ten 10, Twenty 20, Thirty 30"
x = re.findall('\D+', text)
print(x)
result = re.split("\D+", text)
print(result)

for element in result:
    print(element)


'''
=> \D   
    Matches any character which is not a decimal digit.
    This is the opposite of \d. 
    If the ASCII flag is used this becomes the equivalent of [^0-9].

=> re.split(pattern, string, maxsplit=0, flags=0)
    Split string by the occurrences of pattern. 
    If capturing parentheses are used in pattern,
    then the text of all groups in the pattern are also returned as part of the resulting list. 
    If maxsplit is nonzero, at most maxsplit splits occur, and 
    the remainder of the string is returned as the final element of the list.
'''