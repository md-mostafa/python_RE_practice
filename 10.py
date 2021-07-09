#matches a word at the beginning of a string

import re

def findMatch(str):
    pattern = '^\w+'

    if re.search(pattern, str):
        return 'Found a match'
    else:
        return 'Not matched'

print(findMatch('The quick brown fox jumps over the lazy dog'))
print(findMatch(' The quick brown fox jumps over the lazy dog'))


'''
=> ^ (Caret.) Matches the start of the string, and in MULTILINE mode also matches immediately after each newline.

=> \w For Unicode (str) patterns:
      Matches Unicode word characters; 
      this includes most characters that can be part of a word in any language, as well as numbers and the underscore.
      If the ASCII flag is used, only [a-zA-Z0-9_] is matched.

'''