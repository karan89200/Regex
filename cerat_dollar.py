'''
    Caret (^) symbol uses for :-
    i) start with particular entity
    ii) negatlaction of entities

    Dollar ($) symbol uses for :-
    i) end with particular entity
'''

text = "Hello, my age is 25"
pattern = r'^\D'
pattern1 = r'[^0-9]'
pattern2 = r'\d$'
import re
match_list = re.findall(pattern,text)
match_list1 = re.findall(pattern1,text)
match_list2 = re.findall(pattern2,text)
print(match_list)
print(match_list1)
print(match_list2)