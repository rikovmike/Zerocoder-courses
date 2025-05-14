"""

Алгоритм:

1. Привести строку к нижнему регистру (чтобы сравнение было регистронезависимым).
2. Вручную отфильтровать только буквы и цифры, пропуская пробелы и знаки препинания.
2. Сравнить символы с начала и конца строки, двигаясь к центру.


"""


def is_palindrome(s: str) -> bool:
    left = 0
    right = len(s) - 1

    while left < right:
        # Пропускаем небуквенные и нецифровые символы слева
        while left < right and not s[left].isalnum():
            left += 1
        # Пропускаем небуквенные и нецифровые символы справа
        while left < right and not s[right].isalnum():
            right -= 1

        # Сравниваем символы в нижнем регистре
        if s[left].lower() != s[right].lower():
            return False

        left += 1
        right -= 1

    return True


print(is_palindrome("А роза упала на лапу азора"))
print(is_palindrome("Это разве палиндром?"))