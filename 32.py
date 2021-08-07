#replace maximum 2 occurences of space, comma or dot with a colon

import re

text = 'Python Exercises, PHP exercises.'

def replaceWithColon(text):
    pattern = '[ ,.]'
    repl = ':'

    print(re.sub(pattern, repl, text, 2))

print(text)
replaceWithColon(text)



'''
=> re.sub(pattern, repl, string, count=0, flags=0)
    Return the string obtained by replacing the leftmost non-overlapping occurrences of pattern in string by the replacement repl. 
    If the pattern isn’t found, string is returned unchanged. repl can be a string or a function; 
    if it is a string, any backslash escapes in it are processed. 
    That is, \n is converted to a single newline character, \r is converted to a carriage return, 
    and so forth. Unknown escapes of ASCII letters are reserved for future use and treated as errors. 
    Other unknown escapes such as \& are left alone. 
    Backreferences, such as \6, are replaced with the substring matched by group 6 in the pattern.
'''