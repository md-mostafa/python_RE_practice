#find all adverbs and their positions

import re

text = 'Clearly, he has no excuses for such behavior'

for m in re.finditer(r"\w+ly", text):
    print('%d-%d: %s' %(m.start(), m.end(), m.group(0)))



'''
=> re.finditer(pattern, string, flags=0)
    Return an iterator yielding match objects over all non-overlapping matches 
    for the RE pattern in string.

=> \
    Either escapes special characters 
    (permitting you to match characters like '*', '?', and so forth), 
    or signals a special sequence;

'''