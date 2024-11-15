# !!!!!!!!! вариант со своей строкой

def compress_string(s):
    # Проверяем, что строка не пуста
    if not s:
        return ""

    compressed = []
    count = 1  # Счетчик повторений символа

    # Перебираем строку с 1 индекса
    for i in range(1, len(s)):
        if s[i] == s[i - 1]:
            count += 1  # Увеличиваем счетчик для повторяющихся символов
        else:
            # Добавляем символ и его счетчик в результат
            compressed.append(s[i - 1] + str(count))
            count = 1  # Сброс счетчика для нового символа

    # Не забываем добавить последнюю группу символов
    compressed.append(s[-1] + str(count))

    # Объединяем сжатые части в строку и возвращаем результат
    return ''.join(compressed)

# Пример использования:
s = "aaaabbbccaaaaaaaaaaa"
result = compress_string(s)
print(result)