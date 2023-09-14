import requests

print(requests.__version__)
requests.get('http://google.com/')
resp = requests.get('https://raw.githubusercontent.com/akhadeli/cmput404_lab1/main/script.py')
print(resp.text)