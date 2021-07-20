#Search the numbers (0-9) of length between 1 to 3

import re
def findMatch(str):
    pattern = r"([0-9]{1,3})"

    result = re.finditer(pattern, str)
    print('Number of length 1 to 3')
    for n in result:
        print(n.group(0))


findMatch("Exercises number 1, 12, 13, and 345 are important 124")


'''

=> {m,n}
    Causes the resulting RE to match from m to n repetitions of the preceding RE, 
    attempting to match as many repetitions as possible. 
    For example, a{3,5} will match from 3 to 5 'a' characters. 
    Omitting m specifies a lower bound of zero, and 
    omitting n specifies an infinite upper bound. 
    As an example, a{4,}b will match 'aaaab' or a thousand 'a' characters followed by a 'b', 
    but not 'aaab'.

=> (...) 
    Matches whatever regular expression is inside the parentheses, 
    and indicates the start and end of a group; 
    the contents of a group can be retrieved after a match has been performed, 

=> re.finditer(pattern, string, flags=0)
    Return an iterator yielding match objects over all non-overlapping matches for the RE pattern in string. 
    The string is scanned left-to-right, and matches are returned in the order found. 
    Empty matches are included in the result.

'''