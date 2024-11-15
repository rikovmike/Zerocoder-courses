
#ДЗ 2 из урока OP04

def square(side):
    try:
        perimeter = 4 * side
        area = side ** 2
        diagonal = (2 ** 0.5) * side
        return perimeter, area, diagonal
    except TypeError as e:
        return "Используйте только числовые параметры!"


print("Попытка 1")
result = square('df')
print(result)

print("Попытка 2")
result = square(5)
print(result)