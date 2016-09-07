import requests

response = requests.get('https://github.com/megsum/Cmput401Lab1/raw/master/lab1.py')
print response.text
