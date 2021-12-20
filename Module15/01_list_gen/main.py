number = int(input('Введите число: '))
numbers = []

for check in range(1, number + 1, 2):
    numbers.append(check)

print('Список нечетных чисел от 1 до', number,  ':', numbers)


