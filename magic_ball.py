from random import *

answers = ["Бесспорно", "Мне кажется - да", "Пока неясно, попробуй снова", "Даже не думай",
           "Предрешено", "Вероятнее всего", "Спроси позже", "Мой ответ - нет",
           "Никаких сомнений", "Хорошие перспективы", "Лучше не рассказывать", "По моим данным - нет",
           "Можешь быть уверен в этом", "Да", "Сконцентрируйся и спроси опять", "Весьма сомнительно"]

print('Привет, Мир, я магический шар, и я знаю ответ на любой твой вопрос.')
print(f"Приветствую, {input('Как тебя зовут? ')}!")

def base():
    while True:
        ask = input('Задай мне любой вопрос: ')
        print(choice(answers))
        break
    another_question()

def another_question():
    another = input('Ты хочешь спросить еще разок?\nВведи "да" или "нет": ')
    if another == "да": base()
    elif another == "нет": print('Возвращайся если возникнут вопросы!')

base()