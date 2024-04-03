import csv

# Открываем файл с данными монстров
with open("monster_game.csv", encoding="utf-8") as file:
    reader = csv.DictReader(file, delimiter=",")

    # Считываем данные в список
    data = [_ for _ in reader]

# Создаём выходной файл
out_file = open("monster_opportunity.csv", "w+", encoding="utf-8")
writer = csv.DictWriter(out_file, fieldnames=["opportunity", "power"], lineterminator="\n")
writer.writeheader()

reg_max_power = -1

# Проверяем каждого монстра
for monster in data:
    op = monster["opportunity"]
    prob = monster["probability"]

    # Высчитываем силу монстра в зависимости от его возможности
    power = (int(prob) * 0.01 * (
        int(monster["health"]) if op == "регенерация" else
        int(monster["attack"]) if op == "усиление атаки" else
        int(monster["attack"]) + int(monster["protection"]) + int(monster["health"]) + int(monster["speed"])
        )
    )

    # Записываем полученные данные в файл
    writer.writerow({
        "opportunity": op,
        "power": round(power, 2)
    })

    # Обновляем максимальное значение силы регенерации
    if op == "регенерация":
        reg_max_power = max(reg_max_power, power)

print(f"Регенерация: {reg_max_power}")
