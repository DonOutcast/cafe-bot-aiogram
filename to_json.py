import json

array = []

with open('swearword.txt', encoding='utf-8') as r:
    for i in r:
        name = i.lower().split('\n')[0]
        if name != '':
            array.append(name)

with open('swearword.json', 'w', encoding='utf-8') as e:
    json.dump(array, e)