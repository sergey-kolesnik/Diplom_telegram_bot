films_list = ['Крепкий орешек', 'Назад в будущее', 'Таксист',
         'Леон', 'Богемская рапсодия', 'Город грехов',
         'Мементо', 'Отступники', 'Деревня']

new_films = []
quantity = int(input('Какое количество фильмов хотите добавить: '))
for _ in range(quantity):
    film = input('Введите название фильма: ')
    if film in films_list:
        new_films.append(film)
    else:
        print('Ошибка: фильма', film, 'у нас нет.')

print('Список ваших фильмов:', ' '.join(new_films))