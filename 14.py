# contains only upper and lowercase letters, numbers, and underscores

import re


def findMatch(str):
    pattern = '^[a-zA-Z0-9_]*$'

    if re.search(pattern, str):
        return 'Found a match'
    else:
        return 'Not matched!'

print(findMatch("The quick brown fox jumps over the lazy dog."))
print(findMatch("Python_Exercises_1"))
print(findMatch('He is the best'))