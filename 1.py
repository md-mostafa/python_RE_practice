#Write a Python program to check that a string contains only a certain set of characters (in this case a-z, A-Z and 0-9).

import re
def is_allowed_specific_char(string):
    charRe = re.compile(r'[^a-zA-Z0-9.]')
    string = charRe.search(string)

    return not bool(string)

print(is_allowed_specific_char('23432'))

'''

--> . (Dot) this matches any character except a newline
--> ^ (Caret) Matches the start of the string
--> [] used to indicate a set of characters.

--> re.compile(pattern flags=0)
    => Compile a regular expression pattern into a regular expression object, which can be used for matching using
    its match(), search() and other methods

--> search(pattern, string, flags=0)
    =>If zero or more characters at the beginning of string match the regular expression pattern, return a corresponding match object. 
    Return None if the string does not match the pattern
    
    
# re.compile(r'[sfdass]') r means that the string is to be treated as a raw string, which means all escape codes will be ignored
# '\n' will be treated as a newline character, while r'\n' will be treated as the characters \ followed by n.
'''