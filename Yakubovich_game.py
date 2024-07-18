import random
import codecs


word = None
def Yakubovich_game():
    global word
    lvl_game()
    print(f' Количество букв в слове = {len(word)} ')
    print(' 🐍 Удачи 🐍 ')
    letters = list(word)
    Yakubovich_time = ['_' for _ in letters]
    attempts = 0
    lives = 10 * '❤'
    print('')
    print( '@'*19)
    print('😈Игра начинается😈 ')
    print( '@'*19)
    print()
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
            print(f' Было загадано слово:  {word} ')
            print(' Вы расстроили одного Якубовича =( ')
            break
        if '_' not in Yakubovich_time:
            print(f' Вы угадали слово:  {word} ')
            print(' Поздравляем с победой!!! ')
            print(' Количество попыток - ', attempts )
            print(' Якубович Вами гордится! ')
            

def after_game():  
    print('Хотите ещё один раунд?')  
    while True:  
        choice = input('Да(д)/Нет(н)')  
        if choice == 'д':  
            Yakubovich_game()  
        elif choice == 'н':  
            print('Эх, жаль терять такого хорошего игрока')  
            print('С нетерпением ждём вас снова')  
            break  
        else:  
            print(' Некорректный ввод ')  
        
 
def lvl_game():
    global word
    while True:
        print('Выберите уровень сожности:')
        print('* Light : от 4 до 10 букв в слове *')
        print('@ Hard : 10 и более букв в слове @')
        level = input('Light(л) / Hard(х) ')
        if level == 'л':
            print(' Вы выбрали лёгкий уровень ')
            with codecs.open('words-light.txt', 'r', 'utf-8') as f:
                word = random.choice(f.readlines())
                word = word.replace('\n', '')
                word = word.replace('\r', '')
                break
        elif level == 'х':
            print(' Вы выбрали сложный уровень ')
            with codecs.open('words-hard.txt.', 'r', 'utf-8') as f:
                word = random.choice(f.readlines())
                word = word.replace('\n', '')
                word = word.replace('\r', '')
                break
        else:
            print(' Некорректный ввод ')
        
    
print('#'*33)
print('###  Добро пожаловать в игру  ###')
print('#'*33)
print('@'*4, ' Мы с Вами сыграем в ') 
print('@'*4, 'виселицу/Полечудес/Якубович-тайм ')
print('@'*4, 'Называйте как хотите ')
while True:
    print('@'*4, ' Знаете ли вы правила? ')
    action = input(' да(д)/нет(н)')
    if action == 'д':
        print('Отлично, начинаем ')
        Yakubovich_game()
        after_game()
        break
    elif action == 'н':
        print('Правила: ')
        print(' 1) Вы выбираете уровень сложности')
        print(' 2) Получаете слово ')
        print(' 3) Угадываете слово по буквам ')
        print(' 4) Если ошибётесь 10 раз - проиграете')
        Yakubovich_game()
        after_game()
        break
    else:
        print(' Некорректный ввод ')
