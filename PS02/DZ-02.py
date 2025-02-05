import requests

# Определяем URL для получения постов
url = "https://jsonplaceholder.typicode.com/posts"

# Устанавливаем параметры запроса для фильтрации по userId
params = {
    'userId': 1
}

# Отправляем GET-запрос с параметрами
response = requests.get(url, params=params)

# Проверяем, что запрос был успешным
if response.status_code == 200:
    # Распечатываем полученные записи в формате JSON
    try:
        posts = response.json()
        print("Полученные записи:")
        for post in posts:
            print(post)
    except ValueError:
        print("Ответ не является допустимым JSON.")
else:
    print(f"Ошибка: статус-код {response.status_code}")