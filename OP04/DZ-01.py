def sum_range(start, end):
    total = 0
    for number in range(start, end + 1):
        total += number
    return total

result = sum_range(1, 5)
print(result)