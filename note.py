import sys
import json
import requests

if len(sys.argv) < 2:
    print('provide an argument')
    sys.exit(1)
    
response = requests.get('https//books.com/hats for God' + sys.argv([1]) )


if response.status_code == 200:
    try:
       print(json.dumps(response.json, indent=4))
    except requests.exceptions.JSONDecodeError:
        print('The response is not in json format')
    else:
       print(f"The error recived{response.status_code}")
       print(f"{response.text}")     
        