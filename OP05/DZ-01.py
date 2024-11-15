def safe_divide(a, b):
    try:
        return a / b
    except ZeroDivisionError:
        return None

# Примеры использования функции
print(safe_divide(10, 2))  # Ожидается 5.0
print(safe_divide(10, 0))  # Ожидается None
print(safe_divide(15, 3))  # Ожидается 5.0
print(safe_divide(7, 0))   # Ожидается None
print(safe_divide(20, 4))  # Ожидается 5.0