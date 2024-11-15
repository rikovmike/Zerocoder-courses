# Функция для шифрования текста с использованием шифра Цезаря
def caesar_encrypt(text, shift):
    encrypted_text = ""
    for char in text:
        if char.isalpha() and char.isascii():  # Проверяем, является ли символ буквой и относится ли к ASCII
            shift_base = 65 if char.isupper() else 97  # Для заглавных и строчных латинских букв
            encrypted_text += chr((ord(char) - shift_base + shift) % 26 + shift_base)
        else:
            encrypted_text += char  # Оставляем остальные символы без изменений
    return encrypted_text

# Функция для дешифрования текста с использованием шифра Цезаря
def caesar_decrypt(text, shift):
    return caesar_encrypt(text, -shift)

# Пример использования:
text = "Привет, Зерокодер!"
shift = 4

# Шифрование
encrypted_text = caesar_encrypt(text, shift)
print("Зашифрованный текст:", encrypted_text)

# Дешифрование
decrypted_text = caesar_decrypt(encrypted_text, shift)
print("Расшифрованный текст:", decrypted_text)