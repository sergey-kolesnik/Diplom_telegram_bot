video = []
quantity = int(input('ведите колличество видео карт: '))
number = 1


for _ in range(quantity):
    model = int(input(f'{number} видео карта: '))
    video.append(model)
    number += 1

print('Старый список видео карт: ', video)
buy = int(input('Сколько моделей купили: '))

for _ in range(buy):
    max_model = max(video)
    video.remove(max_model)
print('Новый список список видео карт: ', video)

