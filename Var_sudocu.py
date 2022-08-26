import pprint
import random
import os


def list_nicks(name_file):
    """Функция распаковывает имена игроков из тестового файла"""
    path_nick = os.path.join(os.getcwd(), name_file)
    with open(path_nick, mode='r', encoding='utf-8') as file:
        nicks = []
        for line in file:
            nick = str(line.strip())
            nicks.append(nick)
        return nicks


def create_base_dict(nicks):
    """Функция создает словарь, ключами которого являются номера игр,
    а значениями - имена игроков в порядке слотов за столом"""

    base_people_slots = {}
    for i in range(1, 11):

        # i - порядковый номер игры, nick.copy() - копия существующего списка игроков
        # списки являются изменяемыми элементами и если присваивать каждой игре список
        # игроков не копируя его - все столы будут иметь один и тот же порядок игроков
        # так устроена память в питоне
        base_people_slots[i] = nicks.copy()

        # создаем сдвиг игроков относительно слотов за столом
        # здесь мы меняем сам порядок игроков в исходном списке
        shift = nicks[0]
        nicks.remove(shift)
        nicks.append(shift)
    return base_people_slots


def random_vertical(people_slots):
    """Перемешивает слоты игроков (по вертикали)"""
    key = people_slots.keys()
    value = people_slots.values()

    # распаковываю value с помощью цикла, чтобы потом их перемешать
    # в не распакованном виде функция shuffle с данным списком не работает
    values_rasp = []
    for val in value:
        values_rasp.append(val)

    random.shuffle(values_rasp)

    # ввожу i как идентификатор положения элемента в списке значений
    # таким образом идентификатор ключа из списка равен идентификатору значения
    i = 0
    for k in key:
        people_slots[k] = values_rasp[i]
        i = i + 1
    return people_slots


def random_horizontal(people_slots):
    """Перемешивает игроков внутри игр (по горизонтали)"""
    # создаем список идентификаторов x от 0 до 9
    # и перемешиваем их в список random_people_slots
    x = list(range(0, 10))
    random_people_slots = x.copy()
    random.shuffle(random_people_slots)

    # идем по словарю с играми и игроками, и меняем их положение
    # по идентификаторам из списка random_people_slots (меняется порядок игроков внутри игры)
    for key, value in people_slots.items():
        new_value = []
        for r_i in random_people_slots:
            new_value.append(value[r_i])
        people_slots[key] = new_value
    # pprint.pprint(people_slots)
    return people_slots


def write_file_games(write_dict, name_new_file):
    """Запись игр в отдельный файл.
    На вход требуется название файла для записи и
    словарь с парами ключ - номер игры,
    значение - порядок игроков за столом в виде списка"""
    with open(name_new_file, 'w', encoding='utf-8') as file:
        for key, value in write_dict.items():
            file.write('Игра ' + str(key) + ':' + '\n')
            for v in value:
                file.write(str(v) + '\n')
            file.write('\n')


def write_file_slots(write_dict, name_new_file):
    """Запись слотов для игроков в отдельный файл.
    На вход требуется название файла для записи и
    словарь с парами ключ - имя игрока,
    значение - порядок слотов за столом в виде списка"""
    with open(name_new_file, 'w', encoding='utf-8') as file:
        for key, value in write_dict.items():
            file.write(str(key) + '\n')
            i = 1
            for v in value:
                file.write('Игра: ' + str(i) + ' Слот: ' + str(v) + '\n')
                i = i + 1
            file.write('\n')


def result_people_slots(base_people_slots):
    """Создает новый словарь, где ключ - имя игрока, а значение - список его слотов"""
    res_people_slots = {}

    # name - список игроков играющих первую игру
    # берем из словаря по ключу 1 (первая игра)
    name = base_people_slots[1]

    # идем по списку имен и для каждого имени по циклу
    # внутри словаря с играми и имена находим идентификатор
    # положения игрока в каждой игре и записываем эту цифру + 1
    # в список слотов игрока
    for n in name:
        people_slot = []

        for key, value in base_people_slots.items():
            slot = value.index(n)
            people_slot.append(slot + 1)

        res_people_slots[n] = people_slot.copy()

    return res_people_slots


# получаем список игроков из файла
nicks = list_nicks('nick.txt')

# создаем базовый словарь с ключами в виде номера игры и значениями в виде списка имен
base_people_slots = create_base_dict(nicks)

# перемешиваем базовый словарь используя разный порядок горизонтальных и вертикальных функций
random_horizontal(base_people_slots)
random_horizontal(base_people_slots)
random_vertical(base_people_slots)
pprint.pprint(base_people_slots)

# записываем то, что получилось после перемешивания в новый файл с рассадкой
write_file_games(base_people_slots, 'games.txt')

# создаем словарь с порядком игроков за столом
# записываем все это в новый файл
nick_slot = result_people_slots(base_people_slots)
write_file_slots(nick_slot, 'nick_slot.txt')

pprint.pprint(nick_slot)
