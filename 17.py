# Check for a number at the end of a string

import re

def check_end_num(str):
    pattern = r".*[0-9]$"
    text = re.compile(pattern)

    if text.match(str):
        return True
    else:
        return False

print(check_end_num('abcdef'))
print(check_end_num('abcdef6'))
print(check_end_num('aher 2'))


'''

=> re.compile(pattern, flags=0)
    Compile a regular expression pattern into a regular expression object, 
    which can be used for matching using its match(), search() and other methods,


'''