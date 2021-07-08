# Find the sequences of one upper case letter followed by lower case letters
import re

def findMatch(str):
    pattern= '[A-Z]+[a-z]+$'

    if re.search(pattern, str):
        return 'Found A Match'
    else:
        return 'Not matched'


print(findMatch('AAaBbGg'))
print(findMatch("Python"))
print(findMatch("python"))
print(findMatch("PYTHON"))
print(findMatch("aA"))
print(findMatch("Aa"))