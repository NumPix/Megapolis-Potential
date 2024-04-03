import csv

# Открываем файл с данными монстров
with open("monster_game.csv", encoding="utf-8") as file:
    reader = csv.DictReader(file, delimiter=",")

    # Считываем данные в список
    data = [_ for _ in reader]

# Создаем словарь с данными о атаках каждого класса монстров
monster_class_attack_data = {}

# Проверяем каждого монстра и обновляем словарь
for monster in data:
    monster_class = monster["MonsterName"].split()[-1]
    monster_attack = int(monster["attack"])

    if monster_class in monster_class_attack_data:
        monster_class_attack_data[monster_class].append(monster_attack)
    else:
        monster_class_attack_data[monster_class] = [monster_attack]

# Создаём шаблоны для вывода текста
text_template = "{0} монстров класса {1}, средняя сила атаки {2}"

# проверяем каждый класс монстров и выводим его среднее значение атаки
for monster_class, attack_data in monster_class_attack_data.items():
    avg_attack = sum(attack_data) / len(attack_data)
    print(text_template.format(len(attack_data), monster_class, round(avg_attack, 2)))
