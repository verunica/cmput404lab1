import requests

response = requests.get('https://raw.githubusercontent.com/verunica/cmput404lab1/master/request_script.py')
print(response.text)