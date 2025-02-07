import numpy as np
import matplotlib.pyplot as plt

# Генерация двух наборов случайных данных
x_data = np.random.rand(100)  # 100 случайных чисел для оси x
y_data = np.random.rand(100)  # 100 случайных чисел для оси y

# Создание диаграммы рассеяния
plt.scatter(x_data, y_data, color='blue', alpha=0.5)

# Добавление заголовков и меток осей
plt.title('Диаграмма рассеяния случайных данных')
plt.xlabel('X данные')
plt.ylabel('Y данные')

# Отображение диаграммы
plt.show()