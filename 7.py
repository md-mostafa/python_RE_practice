#Find sequences of lowercase letters joined with a underscore

import re

def findMatch(str):
    patterns = '^[a-z]+_[a-z]+$'

    if re.search(patterns, str):
        return 'Found a match'
    else:
        return 'Not matched'


print(findMatch('aab_cbbbc'))
print(findMatch('AAAA_BAABB'))
print(findMatch('aaaa_'))
print(findMatch('Aaab_b'))
print(findMatch('aab__b'))

'''
=> ^  (Caret.) Matches the start of the string, and in MULTILINE mode also matches immediately after each newline.
=> $ Matches the end of the string or just before the newline at the end of the string, and in MULTILINE mode also matches
=> + Causes the resulting RE to match 1 or more repetitions of the preceding RE.
=> [] Used to indicate a set of characters




'''