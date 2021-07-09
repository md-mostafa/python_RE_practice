#matches a string that has an 'a' followed by anything, ending in 'b'


import re
def findMatch(str):
    pattern = 'a.*?b$'

    if re.search(pattern, str):
        return 'Found a match'
    else:
        return 'Not a match'


print(findMatch('aaadsafbbbbbsadfaab'))
print(findMatch("aabbbbd"))
print(findMatch("aabAbbbc"))
print(findMatch("accddbbjjjb"))


'''
=> . (Dot.) In the default mode, this matches any character except a newline. 
      If the DOTALL flag has been specified, this matches any character including a newline.

=> * Causes the resulting RE to match 0 or more repetitions of the preceding RE, as many repetitions as are possible. 
     ab* will match ‘a’, ‘ab’, or ‘a’ followed by any number of ‘b’s.

=> ? Causes the resulting RE to match 0 or 1 repetitions of the preceding RE. ab? will match either ‘a’ or ‘ab’

=> $ Matches the end of the string or just before the newline at the end of the string

'''
