# Yakubovich GAME
## ¯\_(ツ)_/¯ Добро пожаловать на Поле чудес с Лёнечкой =) ¯\_(ツ)_/¯
![Hello All](https://github.com/linalaimik/Yakubovich/blob/main/polechudes.png)

Я НАДЕЮСЬ ВЫ ГОТОВЫ ИСПЫТАТЬ СВОЮ УДАЧУ И СЫГРАТЬ ВМЕСТЕ С НАМИ? =)
Этот код только только рождается и готовится. Поэтому будем стараться не расстроить Леонида Аркадьевича)))
Сыграем в виселицу. Да-да, моя виселица вроде и виселица, но при этом еще и поле чудес! Суть игры, думаю, все знают. У Вас будет 10 жизней и 33 буквы, чтобы угадать слово.

### Что тут должно быть:
-   [x] Код демо версия (один загадывает, другой отгадывает)
-   [x] Слова 4-10 букв (лёгкий уровень)
-   [x] Слова 11 и более букв (Хард)
-   [ ] Код для игры с Лёнечкой
-   [ ] ВОЗМОООЖНО добавится отрисовка висельника
-   [ ] В приоритете сделать игру по категориям
-   [ ] В приоритете (2) Сделать базу данных с игроками и вести счёт

### Ниже представлен вариант висельника. Спасибо Луке =)
from random import choice

HANGMAN = (

    """

    ------
    |    |
    |
    |   
    |
    |
    |
    ----------

    """,
    """

    ------
    |    |
    |    O
    |   
    |
    |
    |
    ----------

    """,
    """

    ------
    |    |
    |    O
    |    |
    |
    |
    |
    ----------

    """,
    """

    ------
    |    |
    |    O
    |   /|
    |
    |
    |
    ----------

    """,
    """

    ------
    |    |
    |    O
    |   /|\\
    |
    |
    |
    ----------

    """,
    """

    ------
    |    |
    |    O
    |   /|\
    |   /
    |
    |
    ----------

    """,
    """

    ------
    |    |
    |    O
    |   /|\
    |   / \
    |
    |
    ----------

    """
)














