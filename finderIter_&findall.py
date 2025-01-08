text = "python is a high level programming language. python is used for ml and dl"
pattern = "python"

import re
### FINDITER FUNCTION START
print("FindIter")
match_iter = re.finditer(pattern,text,re.IGNORECASE)
print(match_iter)
for match in match_iter:
    print(match.start())
    print(match.end())
    print(match)

print()

### FINDITER FUNCTION END

# =============================================================================================================

### FINDALL FUNCTION START
print()
print("FindALL Function")
match_list = re.findall(pattern,text,re.IGNORECASE)
print(match_list)
### FINDALL FUNCTION END



