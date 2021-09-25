#snake case string to camel case string

def snake_to_camel(str):
    import re

    return ''.join(x.capitalize() or '_' for x in str.split('_'))


print(snake_to_camel('python_excerises'))