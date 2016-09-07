import requests

response = requests.post('http://ccid-eddieantonio.rhcloud.com/verunica')
print(response.status_code)