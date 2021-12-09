number = int(input('Введите число:  '))
coefficient = 1
while coefficient <= number:
    coefficient = coefficient + 1
    if number % coefficient == 0:
        print(coefficient)
        break

