name_list = ['Артемий', 'Борис', 'Влад', 'Гоша', 'Дима', 'Евгений', 'Женя', 'Захар']
one_day_name = []

for index in range(1, len(name_list) + 1, 2 ):
    one_day_name.append(name_list[index])
print('Первый день: ',one_day_name)