def sum_of_digits_calculate():
    number = int(input('Введите число: '))
    summ = 0
    while number != 0:
        result = number % 10
        summ += result
        number //= 10
    return summ


def amount_calculate():
    number = int(input('Введите число: '))
    count = 0
    while number != 0:
        count += 1
        number //= 10
    return count

difference = (sum_of_digits_calculate()) - (amount_calculate())
print('Разность суммы чисел и количества равно: ', difference)

