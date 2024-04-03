import csv

# Открываем файл с данными монстров
with open("monster_game.csv", encoding="utf-8") as file:
    reader = csv.DictReader(file, delimiter=",")

    # Считываем данные в список
    data = [_ for _ in reader]

# Создаём шаблоны для вывода текста
text_templates = {
    "success": "Вы сможете победить: {0} монстров",
    "fail": "Вы очень слабы. Сходите и наберитесь опыта!"
}

# Программа работает, пока пользователь не введёт "хватит"
while (player_input := input()) != "хватит":
    # Если пользователь ввёл не число, то повторяем ввод
    if not player_input.isdigit():
        continue

    player_attack = int(player_input)

    # Счётчик монстров, которых игрок может убить
    counter = 0

    # Проверяем всех монстров
    for monster in data:
        monster_health = int(monster["health"])
        if monster_health < player_attack and monster_health != 0:
            counter += 1

    # Выводим ответ в зависимости от количества возможных убитых монстров
    print(text_templates["success"].format(counter) if counter > 0 else text_templates["fail"])

