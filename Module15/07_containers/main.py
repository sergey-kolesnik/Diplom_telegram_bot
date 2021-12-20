def sorting_containers(sorting_containerses):
    sorting_containerses.sort(reverse=True)
    print(sorting_containerses)


number_containers = int(input('\nВведите количество контейнеров: '))
containerses = []

for _ in range(number_containers):
    weight = int(input('Введите массу контейнера: '))
    containerses.append(weight)


print('\nCуществующий список контейнеров: ', end=' ')
sorting_containers(containerses)

new_weight_containers = int(input('ведите новый вес контейнера: '))
containerses.append(new_weight_containers)

print('\nНовый список контейнеров: ', end=' ')
sorting_containers(containerses)

number = containerses.index(new_weight_containers)
print('Номер нового контейнера в списке:', number + 1)


