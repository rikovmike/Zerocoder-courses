import requests

# Определяем URL для отправки POST-запроса
url = "https://jsonplaceholder.typicode.com/posts"

# Создаем словарь с данными для отправки
data = {
    'title': 'foo',
    'body': 'bar',
    'userId': 1
}

# Отправляем POST-запрос с данными
response = requests.post(url, json=data)

# Распечатываем статус-код ответа
print("Статус-код:", response.status_code)

# Распечатываем содержимое ответа в формате JSON
try:
    response_json = response.json()
    print("Содержимое ответа:")
    print(response_json)
except ValueError:
    print("Ответ не является допустимым JSON.")