import pandas as pd

file_path = 'Quality_of_Life.csv'

# Загрузка данных в DataFrame
df = pd.read_csv(file_path)

# Вывод первых 5 строк данных
print("Первые 5 строк данных:")
print(df.head())

# Вывод информации о данных
print("\nИнформация о данных:")
print(df.info())

# Вывод статистического описания данных
print("\nСтатистическое описание:")
print(df.describe())