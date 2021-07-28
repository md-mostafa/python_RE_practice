#extract year, month and date from an url

import re
def extract_date(url):
    pattern = r'/(\d{4})/(\d{1,2})/(\d{1,2})/'
    return re.findall(pattern, url)

url1= "https://www.washingtonpost.com/news/football-insider/wp/2016/09/02/odell-beckhams-fame-rests-on-one-stupid-little-ball-josh-norman-tells-author/"

print(extract_date(url1))