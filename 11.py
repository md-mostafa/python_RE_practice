# matches a word at the end of string, with optional punctuation


import re
def findMatch(str):
    pattern = '\w+\S*$'

    if re.search(pattern, str):
        return 'Found a match'
    else:
        return 'Not matched'

print(findMatch("The quick brown fox jumps over the lazy dog."))
print(findMatch("The quick brown fox jumps over the lazy dog. "))
print(findMatch("The quick brown fox jumps over the lazy dog "))


'''
=> * Causes the resulting RE to match 0 or more repetitions of the preceding RE, 
    as many repetitions as are possible. ab* will match ‘a’, ‘ab’, or ‘a’ followed by any number of ‘b’s.
    
=> $ Matches the end of the string or just before the newline at the end of the string.

=> \S Matches any character which is not a whitespace character.
=> \s For Unicode (str) patterns: Matches Unicode whitespace characters (which includes [ \t\n\r\f\v], 


'''