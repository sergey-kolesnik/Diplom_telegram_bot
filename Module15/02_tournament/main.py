names = ['Артемий', 'Борис', 'Влад', 'Гоша', 'Дима', 'Евгений', 'Женя', 'Захар']
one_day_name = []


for index, name in enumerate(names):
    if index % 2 == 0:
        one_day_name.append(name)
print('Первый день: ', one_day_name, end=' ')