import sys
import requests

"""
if len(sys.argv) == 1:
    print("USAGE: python3 app.py <password>")
else:
    password = sys.argv[1]
    print("Password: ", password)
"""

response = requests.get("http://google.com")
print(response)
