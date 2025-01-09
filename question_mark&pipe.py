'''
QuestionMark (?): use for non-mandatory items
'''

text = 'colour is different from color word.'
pattern = r'colou?r'
import re
match_iter = re.finditer(pattern,text)
for match in match_iter:
    print(match)

'''
Pipe (|) : use for multiple pattern
'''

text1 = 'find cat and dog both in this sentence'
pattern1 = r'cat|dog'
match_list = re.findall(pattern1,text1)
print(match_list)