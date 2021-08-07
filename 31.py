#replace all occurrences of space, comma, or dot with a colon.

import re

def replaceWithColon(text):
    pattern = "[ ,.]"
    repl = ":"

    print(re.sub(pattern, repl, text))


text = 'Python Exercises, PHP exercises.'
replaceWithColon(text)