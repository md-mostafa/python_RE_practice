#remove leading zeros from an IP address.

import re
ip = '216.08.094.196'

def removeLeadingZero(ip):
    pattern = '\.[0]*'
    repl = '.'
    #string = re.sub('\.[0]*', '.', ip)
    x = re.findall(pattern, ip)
    print(x)
    string = re.sub(pattern, repl, ip)
    return string

print(removeLeadingZero(ip))



'''
=> \ Either escapes special characters (permitting you to match characters like '*', '?', and so forth), or signals a special sequence; 
    special sequences are discussed below.


=> re.sub(pattern, repl, string, count=0, flags=0)
    Return the string obtained by replacing the leftmost non-overlapping occurrences of pattern in string by the replacement repl. 
    If the pattern isn’t found, string is returned unchanged. repl can be a string or a function; 
    if it is a string, any backslash escapes in it are processed. 
    That is, \n is converted to a single newline character, \r is converted to a carriage return, and so forth. 
'''