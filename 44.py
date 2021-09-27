#case-insensitive string replacement

import re

text = 'PHP Exercises'

print('Orignal Text: ', text)
redata = re.compile(re.escape('php'), re.IGNORECASE)

new_data = redata.sub('php', text)

print("Using 'php' replace PHP")

print(new_data)


'''

=> re.compile(pattern, flags=0)
    Compile a regular expression pattern into a regular expression object, 
    which can be used for matching using its match(), search() and other methods,

=> re.escape(pattern)
    Escape special characters in pattern. 
    This is useful if you want to match an arbitrary literal string 
    that may have regular expression metacharacters in it.
    
=> re.IGNORECASE
    Perform case-insensitive matching; 
    expressions like [A-Z] will also match lowercase letters. 
    
=> re.sub(pattern, repl, string, count=0, flags=0)
    Return the string obtained by 
    replacing the leftmost non-overlapping occurrences of pattern in string by the replacement repl.

'''