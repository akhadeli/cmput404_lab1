import requests

print(requests.__version__)

google = requests.get('http://google.com/')
print(google.text)

script = requests.get('https://raw.githubusercontent.com/akhadeli/cmput404_lab1/main/script.py')
print(script.text)