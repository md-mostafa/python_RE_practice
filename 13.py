#containing 'z', not at the start or end of the word


import re

def findMatch(str):
    pattern = '\Bz\B'

    if re.search(pattern, str):
        return 'Found a match'
    else:
        return 'Not matched'

print(findMatch("The quick brown fox jumps over the lazy dog."))
print(findMatch("Python Exercises."))
print(findMatch('z'))


'''
=> \b Word boundary. This is a zero-width assertion that matches only at the beginning or end of a word. 
    A word is defined as a sequence of alphanumeric characters,
    so the end of a word is indicated by whitespace or a non-alphanumeric character.
    
=>  \B Another zero-width assertion, 
    this is the opposite of \b, only matching when the current position is not at a word boundary.
    
    
'''