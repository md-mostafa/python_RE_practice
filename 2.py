# Matches a string that has an a followed by zero or more b's

import re
def text_match(text):
    patterns = 'ab*?'

    if re.search(patterns, text):
        return 'Found a match!'
    else:
        return 'Not matched!'



print(text_match('ac'))
print(text_match("abc"))
print(text_match('bb'))


'''

 --> * causes the resulting RE to match 0 or more repetitions of the preceding RE.
 
 --> ? causes the resulting RE to match 0 or 1 repetitions of the preceding RE. ab? will match 'a' or 'ab'
 
 
 --> re.search(pattern, string, flags=0)
    => Scan through string looking for the first location where the regular expression pattern produces a match, 
    and return a corresponding match object


'''