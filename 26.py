#match if two words from a list of words starting letter 'P'


import re
words = ["Python PhP","Java JavaScript", "c c++"]

for word in words:
    m = re.match("(P\w+)\W(P\w+)", word)

    if m:
        print(m.groups())



'''
 => \w
    For Unicode (str) patterns:
    Matches Unicode word characters; 
    this includes most characters that can be part of a word in any language, 
    as well as numbers and the underscore. 
    If the ASCII flag is used, only [a-zA-Z0-9_] is matched.
    
=> \W
    Matches any character which is not a word character. 
    This is the opposite of \w. 
    If the ASCII flag is used this becomes the equivalent of [^a-zA-Z0-9_]. 
    If the LOCALE flag is used, matches characters which are neither alphanumeric in the current locale nor the underscore.
'''