#Matches a string that has an a followed by three 'b'

import re
def text_match(str):
    pattern = 'ab{3}?'
    if re.search(pattern, str):
        return 'Found a match'
    else:
        return 'Not matched'

print(text_match('babbbaaa'))
print(text_match('abbbbbaaaaa'))
print(text_match('aaaaa'))