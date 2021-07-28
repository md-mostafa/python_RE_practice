#convert date format
# yyyy-mm-dd format to dd-mm-yyyy

import re

def change_date_formate(dt):
    pattern = r'(\d{4})-(\d{1,2})-(\d{1,2})'
    repl = '\\3-\\2-\\1'

    return re.sub(pattern, repl, dt)

dt1 = '2021-07-29'

print('Original date in YYY-MM-DD Format: ', dt1)
print('New date in DD-MM-YYY Format: ', change_date_formate(dt1))