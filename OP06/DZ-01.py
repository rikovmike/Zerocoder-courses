
user_input = input("Введите текст для сохранения в файл: ")

with open("user_input.txt", "w", encoding="utf-8") as file:
    file.write(user_input)

print("Текст успешно записан")