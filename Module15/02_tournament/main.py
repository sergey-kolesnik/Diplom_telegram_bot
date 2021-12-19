name_list = ['Артемий', 'Борис', 'Влад', 'Гоша', 'Дима', 'Евгений', 'Женя', 'Захар']
one_day_name = []

# TODO используйте функцию enumerate() сразу в заголовке цикла получите index, name - две переменные сразу
# TODO связку range + len по возможности не используем
# TODO когда можно проитерироваться по списку и получить сразу элемент


for index in range(1, len(name_list) + 1, 2 ):
    one_day_name.append(name_list[index])
print('Первый день: ',one_day_name)