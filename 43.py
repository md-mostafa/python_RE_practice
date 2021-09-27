#split a string at uppercase letter


import re

text = 'PythonTutorialAndExcercises'

print(re.findall('[A-Z][^A-Z]*', text))