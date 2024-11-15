# Функция для шифрования текста с использованием шифра Цезаря
def caesar_encrypt(text, shift):
    encrypted_text = ""
    for char in text:
        if char.isalpha():  # Проверяем, является ли символ буквой
            if 'A' <= char <= 'Z':  # Заглавные латинские буквы
                shift_base = ord('A')
                encrypted_text += chr((ord(char) - shift_base + shift) % 26 + shift_base)
            elif 'a' <= char <= 'z':  # Строчные латинские буквы
                shift_base = ord('a')
                encrypted_text += chr((ord(char) - shift_base + shift) % 26 + shift_base)
            elif 'А' <= char <= 'Я':  # Заглавные кириллические буквы
                shift_base = ord('А')
                encrypted_text += chr((ord(char) - shift_base + shift) % 32 + shift_base)
            elif 'а' <= char <= 'я':  # Строчные кириллические буквы
                shift_base = ord('а')
                encrypted_text += chr((ord(char) - shift_base + shift) % 32 + shift_base)
        else:
            encrypted_text += char  # Оставляем другие символы без изменений
    return encrypted_text

# Функция для дешифрования текста с использованием шифра Цезаря
def caesar_decrypt(text, shift):
    return caesar_encrypt(text, -shift)

# Пример использования:
text = "Привет, Зерокодер!"
shift = 3

# Шифрование
encrypted_text = caesar_encrypt(text, shift)
print("Зашифрованный текст:", encrypted_text)

# Дешифрование
decrypted_text = caesar_decrypt(encrypted_text, shift)
print("Расшифрованный текст:", decrypted_text)