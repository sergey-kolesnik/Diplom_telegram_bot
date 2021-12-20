word = input('Введите слово: ')
words = list(word)
rev_word = words[::-1]

if words == rev_word:
    print('Слово является палиндромом')
else:
    print('Слово палиндромом не является')