#convert camel case string to snake case string.

def camel_to_snake(str):
    import re
    x = re.findall('(.)([A-Z][a-z]+)', str)
    print(x)
    str1 = re.sub('(.)([A-Z][a-z]+)', r'\1_\2', str)
    print(str1)
    return re.sub('(a-z0-9)([A-Z])', r'\1_\2', str1).lower()

print(camel_to_snake('PythonExercises'))



'''
=> .
    (Dot.) In the default mode, this matches any character except a newline. 
    If the DOTALL flag has been specified, 
    this matches any character including a newline.
    
=> []
    Used to indicate a set of characters. In a set:
    -> Characters can be listed individually, e.g. [amk] will match 'a', 'm', or 'k'.
    -> Ranges of characters can be indicated by giving two characters and separating them by a '-', 
        for example [a-z] will match any lowercase ASCII letter, 
    -> [0-5][0-9] will match all the two-digits numbers from 00 to 59, 
    -> [0-9A-Fa-f] will match any hexadecimal digit.
    -> If - is escaped (e.g. [a\-z]) or if it’s placed as the first or last character (e.g. [-a] or [a-]), it will match a literal '-'.
    -> Special characters lose their special meaning inside sets. 
        For example, [(+*)] will match any of the literal characters '(', '+', '*', or ')'.

'''