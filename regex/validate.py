# email = input(print('what is your email')).strip()


# # what if its three
# username,domain = email.split('@')

# if (username) and ('.' in domain):
#     print('valid')
# else:
#     print('invalid')     

import re

email = input(print('what is your email')).strip()


if re.search(r'^\w+@\w+\.edu$',email):
    print('valid')  
else:
    print('invalid')     