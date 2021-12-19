video_list = []
quantity = int(input('ведите колличество видео карт: '))
number = 1



for _ in range(quantity):
    print(number, 'видео карта:', end =' ')
    model = int(input(''))
    video_list.append(model)
    number += 1

print('Старый список видео карт: ', video_list)

buy = int(input('Сколько моделей купили: '))

for _ in range(buy):
    max_model = max(video_list)
    video_list.remove(max_model)
print('Новый список список видео карт: ', video_list)

# TODO применить рекомендации от 03 задания
