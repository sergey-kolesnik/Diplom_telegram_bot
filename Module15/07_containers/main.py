def sorting_containers(sorting_containers_list):          #функция обратоной сортировки
    sorting_containers_list.sort(reverse=True)
    print(sorting_containers_list)


number_containers = int(input('\nВведите количество контейнеров: '))
containers_list = []

for _ in range(number_containers):                        #цикл для ввода массы контейнеров
    weight = int(input('Введите массу контейнера: '))     #можно в любом порядке, функция отсортирует
    containers_list.append(weight)


print('\nCуществующий список контейнеров: ',end = ' ')      #вывод существующего списка контейнеров
sorting_containers(containers_list)                       #сделал ради прикола

new_weight_containers = int(input('ведите новый вес контейнера: '))
containers_list.append(new_weight_containers)

print('\nНовый список контейнеров: ',end = ' ')      #вывод нового существующего списка контейнеров
sorting_containers((containers_list))

number = containers_list.index(new_weight_containers)   #вывод номера в списке нового контейнера
print('Номер нового контейнера в списке:', number + 1)

# TODO применить рекомендации от 03 задания

