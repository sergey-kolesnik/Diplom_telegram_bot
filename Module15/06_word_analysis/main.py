def unique_symbol_output(word_function):
    word_list = list(word_function)
    list_count = []
    count = 0
    for i in word_list:
        if i not in list_count:
            list_count.append(i)
            count += 1

    print('Уникальных символов:', count)


while True:
    word = input('Введите слово: ')
    unique_symbol_output(word)


