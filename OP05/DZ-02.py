def get_integer_input():
    while True:
        user_input = input("Введите целое число: ")
        try:
            # Попытка преобразовать введенное значение в целое число
            number = int(user_input)
            print(f"Вы ввели целое число: {number}")
            break  # Выход из цикла, если ввод корректный
        except ValueError:
            print("Невозможно преобразовать введенное значение в целое число. Попробуйте снова.")

# Запуск программы
get_integer_input()