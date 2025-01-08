import re

pattern = "python"
text = "python is a high-level programming language. python is most popular programming language."


match = re.search(pattern,text)
print(match)

if match:
    print(match.group())
else:
    print(match)