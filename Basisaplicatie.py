import json

open_jayson = open('steam.json')

data = json.load(open_jayson)

for i in data:
    print(i)
    print('data')