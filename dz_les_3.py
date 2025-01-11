# Задание 1: Конвертация секунд
# Спрашиваем у пользователя количество секунд
sec = int(input("Введите количество секунд: "))

# Подсчет
hours = sec // 3600
minutes = (sec % 3600) // 60
remaining_sec = sec % 60

# Вывод результата
print(f"В указанном количестве секунд ({sec}):\nЧасов: {hours}\nМинут: {minutes}\nСекунд: {remaining_sec}")


# Задание 2: Конвертация температуры
# Спрашиваем у пользователя температуру в градусах Цельсия
celsius = float(input("Введите температуру в градусах Цельсия: "))

# Подсчет
kelvin = celsius + 273.15
fahrenheit = (celsius * 9/5) + 32
reaumur = celsius * 4/5

# Округляшка при помощи  функции round
kelvin = round(kelvin, 2)
fahrenheit = round(fahrenheit, 2)
reaumur = round(reaumur, 2)

# Вывод результата
print(f"Кельвин: {kelvin} K\nФаренгейт: {fahrenheit}°F\nРеомюр: {reaumur}°Ré")