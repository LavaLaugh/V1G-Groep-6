import json


def gemiddelde(input):
    lst = []
    open_jayson = open('steam.json')
    data = json.load(open_jayson)
    if input == 'required_age':
        for ding in data:
            lst.append(ding[7][1])
    if input == 'price':
        for ding in data:
            lst.append(ding[17][1])

    t = 0
    w = 0
    for i in lst:
        w += i
        t += 1
    a = w / t
    return a


def bereik(input):
    lst = []
    open_jayson = open('steam.json')
    data = json.load(open_jayson)
    if input == 'required_age':
        for ding in data:
            lst.append(ding[7][1])
    if input == 'price':
        for ding in data:
            lst.append(ding[17][1])
    lst.sort()
    bereik = lst[-1] - lst[0]
    return bereik


def mediaan(input):
    lst = []
    open_jayson = open('steam.json')
    data = json.load(open_jayson)
    if input == 'required_age':
        for ding in data:
            lst.append(ding[7][1])
    if input == 'price':
        for ding in data:
            lst.append(ding[17][1])

    deel = len(lst) / 2
    if deel != int(deel):
        oldwaarde = lst[int(deel)]
        waarde = float(oldwaarde)
        return waarde
    else:
        waarde = (lst[int(deel - 1)] + lst[int(deel)]) / 2
        return waarde


def q1(input):
    lst = []
    open_jayson = open('steam.json')
    data = json.load(open_jayson)
    if input == 'required_age':
        for ding in data:
            lst.append(ding[7][1])
    if input == 'price':
        for ding in data:
            lst.append(ding[17][1])

    q1lst = []
    t = 0
    while t != int(len(lst) / 2):
        q1lst.append(lst[t])
        t += 1
    a = mediaan(q1lst)
    waarde = float(a)
    return waarde


def q3(input):
    lst = []
    open_jayson = open('steam.json')
    data = json.load(open_jayson)
    if input == 'required_age':
        for ding in data:
            lst.append(ding[7][1])
    if input == 'price':
        for ding in data:
            lst.append(ding[17][1])

    q3lst = []
    b = len(lst) / 2
    if b != int(b):
        b = int(b) + 1
    else:
        b = int(b)
    for i in range(b, len(lst)):
        q3lst.append(lst[i])
    print(q3lst)
    a = mediaan(q3lst)
    waarde = float(a)
    return waarde


def variantie(lst):
    open_jayson = open('steam.json')
    data = json.load(open_jayson)
    if input == 'required_age':
        for ding in data:
            lst.append(ding[7][1])
    if input == 'price':
        for ding in data:
            lst.append(ding[17][1])

    x = sum(lst)
    x_ = x / len(lst)
    xi = 0
    for i in lst:
        xi += ((i - x_) * (i - x_))
    v = xi / (len(lst))
    return v


def standaardafwijking():
    lst = []
    open_jayson = open('steam.json')
    data = json.load(open_jayson)
    if input == 'required_age':
        for ding in data:
            lst.append(ding[7][1])
        for ding in data:
            lst.append(ding[17][1])

    output = variantie(lst) ** 0.5

    return output


def frequency(lst):
    lst = []
    open_jayson = open('steam.json')
    data = json.load(open_jayson)
    if input == 'required_age':
        for ding in data:
            lst.append(ding[7][1])
    if input == 'price':
        for ding in data:
            lst.append(ding[17][1])

    fregs = {}
    for i in lst:
        if i in fregs:
            fregs[i] += 1
        else:
            fregs[i] = 1
    return fregs


def modus():
    lst = []
    open_jayson = open('steam.json')
    data = json.load(open_jayson)
    if input == 'required_age':
        for ding in data:
            lst.append(ding[7][1])
    if input == 'price':
        for ding in data:
            lst.append(ding[17][1])

    dic = frequency(lst)
    x = dict(sorted(dic.items(), key=lambda x: x[1]))
    modi = []
    t = 0
    b = list(x.items())
    c = -1
    for i in range(0, len(b)):
        if c == -1:
            modi.append(b[c][0])
            t += b[c][1]
            c -= 1
        else:
            if b[c][1] == t:
                modi.append(b[c][0])
                c -= 1
    return sorted(modi)


def naam_game_1():
    open_jayson = open('steam.json')
    data = json.load(open_jayson)
    game_1 = data[0]
    open_jayson.close()
    return game_1.get('name')


def sorteren_basis(input):
    open_jayson = open('steam.json')
    data = json.load(open_jayson)
    file = open('Sorted output.txt', 'w')
    sorted_data = sorted(data, key=lambda d: d[input])
    file.write('')
    for game in sorted_data:
        file.write(str(game))
        file.write('\n')
    file.close()
    open_jayson.close()


"""def shellsort():
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

        for i in range(0, len(extra_list) - gap):
            temp = extra_list[i][1][1], extra_list[gap + i][1][1]
            if temp[0] > temp[1]:
                extra_list[i], extra_list[gap + i] = extra_list[gap + i], extra_list[i]
            print(i)
            print(str(gap) + 'gap')
            if i == len(extra_list) - gap - 1:
                gap /= 2
                if gap == 2:
                    gap -= 1
                    break
                if isinstance(gap, float) == True:
                    gap = int(gap)
                    gap += 1


    print(extra_list)"""