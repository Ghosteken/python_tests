import sys
import requests
import json

if len(sys.argv) < 2:
    print("You must enter a filename or path as a command line argument.")
    sys.exit(1)

response = requests.get("http://www.google.com/" + sys.argv[1])

if response.status_code == 200:
    try:
        print(json.dumps(response.json(), indent=4))
    except requests.exceptions.JSONDecodeError:
        print("The response is not in JSON format.")
else:
    print(f"Error: Received status code {response.status_code}")
    print(response.text)
    
o = response.json
for result in o['results']:
    print(result['trackName'])      
