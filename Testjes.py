extra_list = []
open_jayson = open('steam.json')
data = json.load(open_jayson)
for i in data:
    extra_list.append(list(i.items()))
print(extra_list[0][1][1])