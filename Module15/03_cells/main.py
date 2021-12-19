quantity_cell = int(input('Введите количество клеток: '))

effectiveness_List = []
number = 1
index = 0
for _ in range(quantity_cell):
    print('Эффективность', number, 'клетки: ' ,end = '')
    # TODO пустых инпутов быть не должно
    cell = int(input(''))
    number += 1
    index += 1
    if index > cell:
        effectiveness_List.append(cell)

print('Неэффективные значения: ', end = '')
for i in effectiveness_List:
    print(i, end = ' ')

# TODO не должно быть подчеркиваний
# TODO однобуквенные переменные называть развернуто

