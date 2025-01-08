
pattern = r'[a-zA-Z0-9]'
text = "python course : $200"

import re
match_list = re.findall(pattern,text)
print(match_list)

#=============================================================================================

# password validation
#Question : Include atleast one capital letter inside password
import re
password = input("Enter the password : ")
pass_pattern = r'[A-Z]'

pass_match_list = re.findall(pass_pattern,password)


if pass_match_list:
    print("valid password",pass_match_list)
else:
    print("invalid password",pass_match_list)



