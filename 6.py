#matches a string that has an a followed by two to three 'b'.

import re
def text_match(str):
    pattern = 'ab{2,3}' #can not be any space between curly bracket
    if re.search(pattern, str):
        return 'Found a match'
    else:
        return 'Not matched'

print(text_match('ab'))
print(text_match('abbbb'))
print(text_match('abbbbbbbabbbbbabbbbbb'))
print(text_match('a'))

