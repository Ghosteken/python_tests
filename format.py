# # name = input('whatis yourname').strip()
# # if ","in name:
# #     last , first = name.split(",")
# #     name = f'{first}, {last}'
# # print (f'hello, {name}')


# #regex formatting
# import re

# name = input('whatis yourname').strip()
# if matches:= re.search(r"^(.+), ?(.+)$",name):
#     name = matches.group(2) +  '' + matches.group(1)
# print (f'hello, {name}')


# 



import re

url = input("URL: ").strip()
# username = url.removeprefix('https//twitter.com/')
if matches :=  re.sub(r'^(https?://)(?:www\.)?twitter\.com/(.+)$',url, re.IGNORECASE):
    print(f'Username',matches.group(1))




