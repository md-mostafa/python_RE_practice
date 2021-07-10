#Matches a word containing 'z'

import re

def findMatch(str):
    pattern = '\w*z.\w*'

    if re.search(pattern, str):
        return 'Found a match'
    else:
        return 'Not matched'

print(findMatch('The quick brown fox jumps over the lazy dog'))
print(findMatch('Python Exercise'))



'''
=> \w For Unicode (str) patterns: Matches Unicode word characters; 
    this includes most characters that can be part of a word in any language, 
    as well as numbers and the underscore
    
=> . (Dot.) In the default mode, this matches any character except a newline. 

'''