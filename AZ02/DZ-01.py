import pandas as pd

# DataFrame с данными
data = {
    'Ученик': [f'Ученик {i+1}' for i in range(10)],
    'Математика': [5, 4, 3, 2, 5, 4, 3, 5, 2, 4],
    'Физика': [4, 5, 3, 2, 4, 3, 5, 3, 4, 2],
    'Химия': [3, 3, 4, 5, 2, 5, 4, 3, 4, 2],
    'Литература': [5, 5, 4, 3, 5, 2, 4, 5, 3, 4],
    'История': [2, 3, 4, 5, 3, 4, 5, 2, 4, 3]
}

df = pd.DataFrame(data)

# Выводим первые несколько строк DataFrame
print("Первые несколько строк DataFrame:")
print(df.head())

# Вычисляем среднюю оценку по каждому предмету
mean_scores = df.mean(numeric_only=True)
print("\nСредняя оценка по каждому предмету:")
print(mean_scores)

# Вычисляем медианную оценку по каждому предмету
median_scores = df.median(numeric_only=True)
print("\nМедианная оценка по каждому предмету:")
print(median_scores)

# Вычисляем Q1 и Q3 для оценок по математике
Q1_math = df['Математика'].quantile(0.25)
Q3_math = df['Математика'].quantile(0.75)
print(f"\nQ1 для Математики: {Q1_math}")
print(f"Q3 для Математики: {Q3_math}")

# Рассчитываем IQR для оценок по математике
IQR_math = Q3_math - Q1_math
print(f"IQR для Математики: {IQR_math}")

# Вычисляем стандартное отклонение по каждому предмету
std_deviation = df.std(numeric_only=True)
print("\nСтандартное отклонение по каждому предмету:")
print(std_deviation)