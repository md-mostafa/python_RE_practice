#Find URLs in a String

text = '<p>Contents :</p><a href="https://w3resource.com">Python Examples</a><a href="http://github.com">Even More Examples</a>'


def findAllUrl(str):
    import re
    pattern = 'http[s]?://(?:[a-zA-Z]|[0-9]|[$-_@.&+]|[!*\(\),]|(?:%[0-9a-fA-F][0-9a-fA-F]))+'

    return re.findall(pattern, str)


print('Original String : ', text)
print('Urls : ', findAllUrl(text))
