
numbers = [1, 4, -3, 0, 10]
print('Изначальный список:', numbers)

count = len(numbers)                            #число элементов в списке

for num_i in range(0, count - 1):       #цикл с count - 1 итераций
    for num_j in range(0, count - 1 - num_i):   #цикл с count - 1 итераций минус последнее число
        if numbers[num_j] > numbers[num_j + 1]:  #сравниваем 2 последних числа, если a>b, то меняем их местами
            numbers[num_j], numbers[num_j + 1] = numbers[num_j + 1], numbers[num_j]


print('Отсортированный список:', numbers)