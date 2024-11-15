
try:
    dl=int(input("Введите длину: "))
    sh=int(input("Введите ширину: "))

    print("Площадь= "+str(dl*sh))

except ValueError:
    print("Пожалуйста, используйте только числа.")