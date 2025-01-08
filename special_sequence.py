''' 
\d = Matches any digit character (0,1,2,3,4,5,6,7,8,9)
\D = Matches any non-digit character 
\w = Matches any word character (alphanumeric plus underscore)
\W = Matches any non-word character
\s = Matches any whitespace character (space, tabs, newlines, etc.)
\S = Matches any non-whitespace character
\b = Matches a word boundary
\A = startswith
\Z = endswith
'''

import re
text = "python _course %#rate 200$ ."
pattern = '\d'
match_list = re.findall(pattern,text)
print(match_list)




