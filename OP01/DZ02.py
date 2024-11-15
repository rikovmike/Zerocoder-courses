try:
    name = input("Введите ваше имя: ")
    age = int(input("Введите ваш возраст: "))

    # Рассчитаем количество прожитых месяцев, дней и часов
    months = age * 12
    days = age * 365
    hours = days * 24

    print(f"Привет {name}! Тебе {age} лет.")
    print(f"Это примерно {months} месяцев, {days} дней и {hours} часов.")

except ValueError:
    print("Пожалуйста, введите корректный возраст.")