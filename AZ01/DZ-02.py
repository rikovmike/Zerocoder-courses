import pandas as pd

file_path = 'dz.csv'

# Загрузка данных из CSV в DataFrame
df = pd.read_csv(file_path)

# Проверка первых нескольких строк данных, чтобы убедиться, что все загружено правильно
print("Первые 5 строк данных:")
print(df.head())

# Группировка данных по городу и вычисление средней зарплаты
average_salary_by_city = df.groupby('City')['Salary'].mean()

# Вывод средних зарплат по городам
print("\nСредняя зарплата по городам:")
print(average_salary_by_city)