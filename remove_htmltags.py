text = "<head> This is title bar </head> , <b> it means bold </b>"
pattern = r'<[^>]+>' # universal code
pattern2 = r'</?\w+>' # when html tags are proper separated from spaces.
import re
match_list = re.findall(pattern2,text)
print(match_list)

new_list = []
for word in text.split():
    if word not in match_list:
        new_list.append(word)

print(new_list)