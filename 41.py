#Remove everything except alphanumeric characters from a string

import re
text = '**//Python Excercises// - 12. '

pattern = re.compile('[\W_]+')
print(pattern.sub('', text))



'''
 => \W
    Matches any character which is not a word character. This is the opposite of \w.
 
 => re.compile(pattern, flags=0)
    Compile a regular expression pattern into a regular expression object, 
    which can be used for matching using its match(), search() and other methods,
'''