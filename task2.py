import csv

# Открываем файл с данными монстров
with open("monster_game.csv", encoding="utf-8") as file:
    reader = csv.DictReader(file, delimiter=",")

    # Считываем данные в список
    data = [_ for _ in reader]

# Сортируем монстров по их "возможности" в обратном алфавитном порядке алгоритмом вставки
for i in range(len(data)):
    for j in range(i):
        if data[i]["opportunity"] > data[j]["opportunity"] or j == i - 1:
            data.insert(j, data.pop(i))
            break

# Создаём шаблоны для вывода текста
text_template = ("{0} имеет возможность: {1},"
                 " вероятность использования возможности равна {2}")

# Выводим данные о первых 3 монстрах
print(*list(map(lambda x: text_template.format(x["MonsterName"],
                                               x["opportunity"],
                                               x["probability"]),
                data))[:3], sep="\n")