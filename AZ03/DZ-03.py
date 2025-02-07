import requests
from bs4 import BeautifulSoup
import pandas as pd
import matplotlib.pyplot as plt

# URL страницы
url = "https://www.divan.ru/category/divany-i-kresla"

# Получение страницы
response = requests.get(url)
soup = BeautifulSoup(response.content, 'html.parser')

# Парсинг карточек товаров
cards = soup.find_all(class_='lsooF')

# Списки для хранения данных
product_names = []
prices = []

# Извлечение данных из каждой карточки
for card in cards:
    # Получение названия товара
    name_element = card.find(class_='qUioe')
    if name_element:
        product_name = name_element.get_text(strip=True)
        product_names.append(product_name)

    # Получение цены из тега <meta> с itemprop="price"
    price_element = card.find('meta', itemprop='price')
    if price_element:
        price = price_element['content']
        prices.append(int(price))

# Создание DataFrame
df = pd.DataFrame({
    'Product': product_names,
    'Price': prices
})

# Сохранение в CSV
df.to_csv('divan_prices.csv', index=False)

# Вычисление средней цены
average_price = df['Price'].mean()
print(f'Средняя цена на диваны: {average_price:.2f} ₽')

# Построение гистограммы
plt.figure(figsize=(10, 6))
plt.hist(df['Price'], bins=20, color='blue', edgecolor='black')
plt.title('Гистограмма цен на диваны')
plt.xlabel('Цена (₽)')
plt.ylabel('Количество')
plt.grid(axis='y')

# Показ гистограммы
plt.show()