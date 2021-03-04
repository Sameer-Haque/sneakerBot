import requests
import json

login = '{"Email Address":"dragonballgt76@gmail.com","Password":"your_gay"}'
x = json.loads(login)
print(x["Password"])
y = requests.get('http://www.FLI.tech')
print(y.text)
