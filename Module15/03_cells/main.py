quantity_cell = int(input('Введите количество клеток: '))

effectiveness = []
number = 1
index = 0
for _ in range(quantity_cell):
    cell = int(input(f'Эффективность {number} клетки: '))
    number += 1
    index += 1
    if index > cell:
        effectiveness.append(cell)

print('Неэффективные значения: ', end='')
for text in effectiveness:
    print(text, end=' ')


