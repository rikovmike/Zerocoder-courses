# Функция для выполнения арифметических операций
def calculator():
    print("Введите два числа:")
    num1 = float(input("Первое число: "))
    num2 = float(input("Второе число: "))

    print("Выберите операцию:")
    print("1. Сложение (+)")
    print("2. Вычитание (-)")
    print("3. Умножение (*)")
    print("4. Деление (/)")

    operation = input("Введите номер операции (1/2/3/4): ")

    if operation == '1':
        result = num1 + num2
        print(f"{num1} + {num2} = {result}")
    elif operation == '2':
        result = num1 - num2
        print(f"{num1} - {num2} = {result}")
    elif operation == '3':
        result = num1 * num2
        print(f"{num1} * {num2} = {result}")
    elif operation == '4':
        if num2 != 0:
            result = num1 / num2
            print(f"{num1} / {num2} = {result}")
        else:
            print("Ошибка: Деление на ноль!")
    else:
        print("Некорректный ввод операции.")

# Запуск калькулятора
calculator()