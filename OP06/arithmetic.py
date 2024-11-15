def add(a, b):
    """Возвращает сумму a и b."""
    return a + b

def subtract(a, b):
    """Возвращает разность a и b."""
    return a - b

def multiply(a, b):
    """Возвращает произведение a и b."""
    return a * b

def divide(a, b):
    """Возвращает частное a и b. Если b равно 0, возвращает сообщение об ошибке."""
    if b == 0:
        return "Ошибка: деление на ноль!"
    return a / b