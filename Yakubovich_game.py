word = input(' Введите слово: ')
letters = list(word)
Yakubovich_time = ['_' for _ in letters]
attempts = 0
lives = 10 * '❤'
print('')
print('@'*17)
print(' Готов испытать удачу? =) ')
print('@'*17)
while '_' in Yakubovich_time:
    for bukovka in Yakubovich_time:
        print(bukovka, end ='')
    letter_in_word = input(' Какую букву выбираете? =) ')
    if letter_in_word in letters:
        print(f' Откройте букву {letter_in_word}')
        print(lives)
        for i, letter in enumerate(letters):
            if letter == letter_in_word:
                Yakubovich_time[i] = letter_in_word
    elif not letter_in_word:
        print(' Вы ввели пустую строку. Пожалуйста, введите букву! ')
        print(lives)
        continue
    else:
        print(' Такой буквы нет вы потеряли одну жизнь =( ')
        lives = lives[:-1]
        print(lives)
    attempts +=1
    if len(lives) == 0:
        print(' Жизней не осталось, игра окончена =( ')
        print(f' Было загадано слово {word} ')
        print(' Вы расстроили одного Якубовича =( ')
        break
    if '_' not in Yakubovich_time:
        print(' Поздравляем с победой!!! ')
        print(' Количество попыток - ', attempts )
        print(' Якубович Вами гордится! ')