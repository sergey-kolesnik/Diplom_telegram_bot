
number_list = [1, 4, -3, 0, 10]
print('Изначальный список:', number_list)

count = len(number_list)                            #число элементов в списке

for num_i in range(0, count - 1):       #цикл с count - 1 итераций
    for num_j in range(0, count - 1 - num_i):   #цикл с count - 1 итераций минус последнее число
        if number_list[num_j] > number_list[num_j + 1]:  #сравниваем 2 последних числа, если a>b, то меняем их местами
            number_list[num_j], number_list[num_j + 1] = number_list[num_j + 1], number_list[num_j]


print('Отсортированный список:', number_list)

# TODO применить рекомендации от 03 задания
# TODO применить рекомендации от 03 модуля
