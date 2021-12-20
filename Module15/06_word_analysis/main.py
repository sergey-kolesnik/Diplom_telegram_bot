def unique_symbol_output(word_function):
    words = list(word_function)
    counts = []
    count = 0
    for symbol in words:
        if symbol not in counts:
            counts.append(symbol)
            count += 1
    print('Уникальных символов:', count)


while True:
    word = input('Введите слово: ')
    unique_symbol_output(word)

