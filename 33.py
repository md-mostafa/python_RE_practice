# Find all five characters long word in a string


import re

text = 'The quick brown fox jumps over the lazy dog'

pattern = r"\b\w{5}\b"

print(re.findall(pattern, text))


'''
=> \b
    Matches the empty string, 
    but only at the beginning or end of a word.
    Note that formally, \b is defined as the boundary 
    between a \w and a \W character (or vice versa), 
    or between \w and the beginning/end of the string. 
    This means that r'\bfoo\b' matches 'foo', 'foo.', '(foo)', 'bar foo baz' 
    but not 'foobar' or 'foo3'.
'''