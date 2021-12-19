number = int(input('Введите число: '))
number_list = []

for check in range(1, number + 1, 2):
    number_list.append(check)


print('Список нечетных чисел от 1 до', number,  ':', number_list)


