word = input('Введите слово: ')
word_list = list(word)
rev_list = word_list[::-1]


if word_list == rev_list:
    print('Слово является палиндромом')
else:
    print('Слово палиндромом не является')