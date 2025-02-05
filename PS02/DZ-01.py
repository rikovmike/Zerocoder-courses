import requests

# Определяем URL для поиска репозиториев на GitHub
url = "https://api.github.com/search/repositories"

# Устанавливаем параметры запроса для поиска репозиториев с кодом на HTML
params = {
    'q': 'language:Python'
}

# Отправляем GET-запрос
response = requests.get(url, params=params)

# Распечатываем статус-код ответа
print("Статус-код:", response.status_code)

# Распечатываем содержимое ответа в формате JSON
try:
    response_json = response.json()
    print("Содержимое ответа в формате JSON:")
    print(response_json)
except ValueError:
    print("Ответ не является допустимым JSON.")