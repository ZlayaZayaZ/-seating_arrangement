import pprint
import random
import os


path_nick = os.path.join(os.getcwd(), 'nick.txt')
with open(path_nick, mode='r', encoding='utf-8') as file:
    nicks = []
    for line in file:
        nick = str(line.strip())
        nicks.append(nick)


def create_base_dict(nicks):
    base_people_slots = {}
    for i in range(1, 11):
        base_people_slots[i] = nicks.copy()
        shift = nicks[0]
        nicks.remove(shift)
        nicks.append(shift)
    return base_people_slots


people_slots = {
    'A': [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],
    'B': [2, 3, 4, 5, 6, 7, 8, 9, 10, 1],
    'C': [3, 4, 5, 6, 7, 8, 9, 10, 1, 2],
    'D': [4, 5, 6, 7, 8, 9, 10, 1, 2, 3],
    'E': [5, 6, 7, 8, 9, 10, 1, 2, 3, 4],
    'K': [6, 7, 8, 9, 10, 1, 2, 3, 4, 5],
    'G': [7, 8, 9, 10, 1, 2, 3, 4, 5, 6],
    'H': [8, 9, 10, 1, 2, 3, 4, 5, 6, 7],
    'X': [9, 10, 1, 2, 3, 4, 5, 6, 7, 8],
    'J': [10, 1, 2, 3, 4, 5, 6, 7, 8, 9]
}


def random_vertical(people_slots):
    key = people_slots.keys()
    value = people_slots.values()
    values_rasp = []
    for val in value:
        values_rasp.append(val)

    random.shuffle(values_rasp)

    i = 0
    for k in key:
        people_slots[k] = values_rasp[i]
        i = i + 1
    return people_slots


def random_horizontal(people_slots):
    x = list(range(0, 10))
    random_people_slots = x.copy()
    random.shuffle(random_people_slots)
    # print(random_people_slots)
    for key, value in people_slots.items():
        new_value = []
        for r_i in random_people_slots:
            new_value.append(value[r_i])
        people_slots[key] = new_value
    # pprint.pprint(people_slots)
    return people_slots


def game(people_slots):
    games_people = {}
    game = list(range(0, 10))
    for i in game:
        for key, value in people_slots.items():
            game[(value[i])-1] = key
        print(game)
        games_people[i+1] = game.copy()
    return games_people


def write_file(write_dict, name_new_file):
    with open(name_new_file, 'w', encoding='utf-8') as file:
        for key, value in write_dict.items():
            file.write(str(key) + '\n')
            for v in value:
                file.write(str(v) + '\n')


def result_people_slots(games_people):
    res_people_slots = {}
    name = games_people[1]
    for n in name:
        people_slot = []
        for key, value in games_people.items():
            slot = value.index(n)
            people_slot.append(slot + 1)
        res_people_slots[n] = people_slot.copy()
    return res_people_slots


base_people_slots = create_base_dict(nicks)
random_horizontal(base_people_slots)
random_horizontal(base_people_slots)
random_vertical(base_people_slots)
pprint.pprint(base_people_slots)
# game = game(base_people_slots)
write_file(base_people_slots, 'games.txt')
# nick_slot = result_people_slots(game)
# write_file(nick_slot, 'nick_slot.txt')
# pprint.pprint(game)
# pprint.pprint(nick_slot)
