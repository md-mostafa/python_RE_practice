#Search a literals string in a string and also find the location where the pattern occurs

import re
pattern = 'fox'
text = 'The quick brown fox jumps over the lazy dog.'

match = re.search(pattern, text)

s = match.start()
e = match.end()

print('Found "%s" in "%s" from %d to %d ' %(match.re.pattern, match.string, s, e))


'''
=> Match.start([group])
=> Match.end([group])
=>  Return the indices of the start and end of the substring matched by group

'''