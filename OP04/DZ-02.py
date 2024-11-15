def square(side):
    perimeter = 4 * side
    area = side ** 2
    diagonal = (2 ** 0.5) * side
    return perimeter, area, diagonal


result = square(5)
print(result)