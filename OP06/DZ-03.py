import random

def select_students(student_list, number_of_students):
    # Проверяем, чтобы количество выбираемых студентов не превышало размер списка
    if number_of_students > len(student_list):
        raise ValueError("Количество выбираемых студентов превышает размер списка.")

    # Случайным образом выбираем уникальные имена
    selected_students = random.sample(student_list, number_of_students)
    return selected_students

# Пример списка учащихся
students = [
    "Алексей", "Мария", "Сергей", "Анна", "Дмитрий",
    "Екатерина", "Иван", "Татьяна", "Павел", "Ольга",
    "Николай", "Елена", "Анастасия", "Максим", "Светлана"
]

# Количество студентов, которых нужно выбрать
number_to_select = 5

try:
    selected_students = select_students(students, number_to_select)
    print("Выбранные студенты для ответа на уроке:")
    for student in selected_students:
        print(student)
except ValueError as e:
    print(e)