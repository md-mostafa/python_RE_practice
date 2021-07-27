#replace whitespaces with an underscore and vice versa

import re
text ='Python Exercises'

text = text.replace(" ", "_")
print(text)


text = text.replace("_", " ")
print(text)