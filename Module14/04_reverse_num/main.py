def revers_number_calculate(number):           #функция реверса числа
    exp_number_1 = ''
    exp_number_2 = ''
    for symbol in number:                       #цикл который переберает символы в строке до точки
        exp_number_2 += symbol
        if symbol == '.':
            exp_number_1 = exp_number_2
            exp_number_2 = ''
            exp_number_2 += symbol
    exp_number_1 = (exp_number_1[::-1])         #переворачиваем строки
    exp_number_2 = (exp_number_2[::-1])

    number = (exp_number_1.replace('.', '') + '.' + exp_number_2.replace('.', '')) #создаем правильное число в строке
    return (float(number))      #переводим строку в вещественное число

number_N = input('Введите число N: ')
number_K = input('Введите число K: ')


reverse_number_N = revers_number_calculate(number_N)
reverse_number_K = revers_number_calculate(number_K)
result = reverse_number_N + reverse_number_K
print('Первое число наборот: ', reverse_number_N)
print('Второе число наборот: ', reverse_number_K)

print('Сумма: ', result)