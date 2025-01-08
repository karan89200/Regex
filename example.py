# Q1 : filter out the date from data

text = "2024-05-16 is karan birthday 34 and 2024-03-24 is ankit birthday."
pattern = r'\d{4}-\d{2}-\d{2}'

import re
match_iter = re.finditer(pattern,text)
for match in match_iter:
    print(match)



