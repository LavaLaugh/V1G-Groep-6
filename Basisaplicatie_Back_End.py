import json


def naam_game_1():
    open_jayson = open('steam.json')
    data = json.load(open_jayson)
    game_1 = data[0]
    open_jayson.close()
    return game_1.get('name')


def sorteren_basis(input):
    sorted_games = []
    open_jayson = open('steam.json')
    data = json.load(open_jayson)
    sorted_data = sorted(data, key=lambda d: d[input].lower())
    for game in sorted_data:
        sorted_games.append(game)
    return sorted_games


def shellsort():
    extra_list = []
    open_jayson = open('steam.json')
    data = json.load(open_jayson)
    for i in data:
        extra_list.append(list(i.items()))
    gap = len(extra_list) // 2
    while gap > 0:
        if gap == 1:
            done = 1
            for i in range(0, len(extra_list)):
                temp = extra_list[i][1][1], extra_list[i + 1][1][1]
                if temp[0] > temp[1]:
                    extra_list[i], extra_list[i + 1] = extra_list[i + 1], extra_list[i]
                    done = 0
                if done == 1 and i == len(extra_list):
                    return extra_list
        for i in range(0, len(extra_list)):
            temp = extra_list[i][1][1], extra_list[gap + i][1][1]
            if temp[0] > temp[1]:
                extra_list[i], extra_list[gap + i] = extra_list[gap + i], extra_list[i]
            print(i)
            print(str(gap) + 'gap')
            if i == len(extra_list) - 1:
                gap /= 2
                if gap == 2:
                    gap -= 1
                if isinstance(gap, float) == True:
                    gap = int(gap)
                    gap += 1

    print(extra_list)


print(shellsort())


