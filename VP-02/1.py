# Подсчет количества чисел от 1 до 2024, содержащих цифру "3"
count = 0

# Перебираем все числа от 1 до 2024
for num in range(1, 2025):
    # Преобразуем число в строку и проверяем наличие цифры '3'
    if '3' in str(num):
        count += 1

# Выводим результат
print("Количество чисел, содержащих цифру 3:", count)