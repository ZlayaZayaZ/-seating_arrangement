import pprint
import random

slot = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
party_list = ['A', 'B', 'C', 'D', 'E', 'I', 'F', 'G', 'H', 'K']
party_dict = {}
for party in party_list:
    party_dict[party] = slot.copy()
# pprint.pprint(party_dict)

result_games = {}


def people_slot_result(random_int, key, game):
    print(random_int)
    people = key[random_int]

    people_slots = party_dict[people]

    if x in people_slots:

        key.remove(people)
        people_slots.remove(x)

        party_dict[people] = people_slots
        game.append(people)
        return
    else:
        people_slot_result(random_int-1, key, game)


for i in range(1, 10):
    print(f'i = {i}')
    key = party_list.copy()
    game = []
    for x in range(1, 11):
        random_int = random.randint(0, len(key)-1)
        print(key)
        people_slot_result(random_int, key, game)
    print(game)
    result_games[i] = game
pprint.pprint(result_games)
# pprint.pprint(party_dict)
