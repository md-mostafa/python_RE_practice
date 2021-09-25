#extract values between quotation marks of a string.
import re

text1 = '"Python", "PHP", "Java"'

print(re.findall(r'"(.*?)"', text1))


'''

=> .
    (Dot.) In the default mode, this matches any character except a newline. 
    If the DOTALL flag has been specified, 
    this matches any character including a newline.
    
=> *?, +?, ??
    The '*', '+', and '?' qualifiers are all greedy; they match as much text as possible. 

=> (...)
    Matches whatever regular expression is inside the parentheses, and indicates the start and end of a group; 
    the contents of a group can be retrieved after a match has been performed, 
    and can be matched later in the string with the \number special sequence, described below.
    To match the literals '(' or ')', use \( or \), or enclose them inside a character class: [(], [)].

'''