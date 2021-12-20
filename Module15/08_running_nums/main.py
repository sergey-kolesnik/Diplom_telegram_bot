texts = input('ведите бегущую строку: ')
shift = int(input('Сдвиг: '))
print('Изначальный текст: ', texts)

texts = texts[shift:]+texts[:shift]
print('Сдвинутый текст: ', texts)


