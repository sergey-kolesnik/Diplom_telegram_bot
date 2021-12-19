text_list = input('ведите бегущую строку: ')
shift = int(input('Сдвиг: '))
print('Изначальный текст: ', text_list)

text_list = text_list[shift:]+text_list[:shift]
print('Сдвинутый текст: ', text_list)


