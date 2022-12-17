from random import *
word_list = ["человек", "слово", "лицо", "дверь", "земля", "работа", "ребенок", "история", "женщина", "развитие", "власть", "правительство", "начальник", "спектакль", "автомобиль", "экономика", "литература", "граница", "магазин", "председатель", "сотрудник", "республика", "личность"]

def get_word(list_words):
    random_word = choice(list_words).upper()
    return random_word

def print_word(word_, list_):
    for c in word_:
        if c in list_: print(c, end=' ')
        else: print('_', end=' ')
    print()

def display_hangman(tries):
    stages = [  # финальное состояние: голова, торс, обе руки, обе ноги
        '''
           --------
           |      |
           |      O
           |     \\|/
           |      |
           |     / \\
           -
        ''',
        # голова, торс, обе руки, одна нога
        '''
           --------
           |      |
           |      O
           |     \\|/
           |      |
           |     / 
           -
        ''',
        # голова, торс, обе руки
        '''
           --------
           |      |
           |      O
           |     \\|/
           |      |
           |      
           -
        ''',
        # голова, торс и одна рука
        '''
           --------
           |      |
           |      O
           |     \\|
           |      |
           |     
           -
        ''',
        # голова и торс
        '''
           --------
           |      |
           |      O
           |      |
           |      |
           |     
           -
        ''',
        # голова
        '''
           --------
           |      |
           |      O
           |    
           |      
           |     
           -
        ''',
        # начальное состояние
        '''
           --------
           |      |
           |      
           |    
           |      
           |     
           -
        '''
    ]
    return stages[tries]

def play(word):
    word_completion = '_' * len(word)  # строка, содержащая символы _ на каждую букву задуманного слова
    guessed = False  # сигнальная метка
    guessed_letters = []  # список уже названных букв
    guessed_words = []  # список уже названных слов
    tries = 6  # количество попыток
    print('ну че, сыграем в угадайку слов?\nтебе выпала крутая возможность повесить человека')
    print(display_hangman(tries))
    print(word_completion)
    while True:
        word_input = input('введи букву или слово: ').upper()
        if not word_input.isalpha():
            print('ты вроде не глупый, но вводишь полную залупу, попробуй ещё')
            continue
        if word_input in guessed_words or word_input in guessed_letters:
            print('уже было и тебе не фортануло, думаешь с того момента что-то изменилось?')
            continue
        if len(word_input) > 1:
            if word_input == word:
                print('нифига ты крутыш, молодец, победа твоя!')
                break
            else:
                guessed_words.append(word_input)
                tries -= 1
                print(f'ты что, так жаждешь повесить человека? осталось попыток {tries}')
                print(display_hangman(tries))
                print_word(word, guessed_letters)
                if tries == 0:
                    print(f'лошара, ты проиграл! загаданное слово: {word}')
                    break
                continue

        if word_input in word:
            guessed_letters.append(word_input)
            for c in word:
                if c not in guessed_letters:
                    print('красавчик! угадал букву')
                    print_word(word, guessed_letters)
                    guessed = False
                    break
                guessed = True
            if guessed:
                print_word(word, guessed_letters)
                print('нифига ты крутыш, молодец, победа твоя!')
                break
        else:
            guessed_letters.append(word_input)
            tries -= 1
            print(f'ты что, так жаждешь повесить человека? осталось попыток {tries}')
            print(display_hangman(tries))
            print_word(word, guessed_letters)
        if tries == 0:
            print(f'лошара, ты проиграл! загаданное слово: {word}')
            break

def main():
    print('ку!')
    play(get_word(word_list))
    contin_game = input('еще партию? нажми клавишу "д", если ломаешься, нажми "н": ')
    while True:
        if contin_game == 'д':
            play(get_word(word_list))
            contin_game = input('еще партию? нажми клавишу "д", если ломаешься, нажми "н": ')
        else:
            print('а я и не думала, что ты такой слабак! чао, дурик!')
            break

main()