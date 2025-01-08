# Q1 :extract file name with file type 

# text = " my file data.csv and requirement.txt is necessary"
# pattern = r'\w+\.\w+' # answer

# Q2 : extract phone numbers in format xxx-xxx-xxxx (first digit should not be zero)

# text = "893-345-6757 is fake number and 097-345-2345 is not valid."
# pattern = r'\b[1-9]\d{2}-\d{3}-\d{4}\b'


# Q3 : Write a regular expression to find sequences of any character repeated three or more times.
# text = 'aaa bbb zz ccc ddddd eeee fgh'
# pattern = r'(.)\1{2,}'
# output : aaa ,bbb,ccc,dddd,eee



# Q4 : extract email from text
# text = "karan email id kks345@gmail.com and ankit mail akkgiri45@outlook.in"
# pattern = r'\w+@\w+\.\w{2,}'

import re
match_iter = re.finditer(pattern,text)

for match in match_iter:
    print(match.group()) 

