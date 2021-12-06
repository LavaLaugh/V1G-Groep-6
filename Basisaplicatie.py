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
