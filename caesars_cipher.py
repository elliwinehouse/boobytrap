whats_direction = input('что мы должны сделать: шифровать или дешифровать? \n').lower()
while whats_direction != 'шифровать' and whats_direction != 'дешифровать':
    whats_direction = input("ты совсем дурачок? напиши 'шифровать' либо 'дешифровать'. \n").lower()

whats_language = input('какой нужен язык: русский или английский? \n').lower()
while whats_language != 'русский' and whats_language != 'английский':
    whats_language = input("ты совсем дурачок? напиши 'русский' либо 'английский'. \n").lower()

whats_step = input('на сколько символовов мы сдвигаем буквы по алфавиту? ответ напиши числом. \n')
while whats_step.isdigit() != True:
    whats_step = input('ты совсем дурачок? напиши число! \n')

whats_text = input('какой текст нужно использовать сейчас? \n')
while whats_text.isspace() == True:
    whats_text = input('ты совсем дурачок? введи текст! \n')

def caesar(direction, language, step, text):
    upper_eng_alphabet = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    lower_eng_alphabet = 'abcdefghijklmnopqrstuvwxyz'
    upper_rus_alphabet = 'АБВГДЕЖЗИЙКЛМНОПРСТУФХЦЧШЩЪЫЬЭЮЯ'
    lower_rus_alphabet = 'абвгдежзийклмнопрстуфхцчшщъыьэюя'

    for i in range(len(text)):
        if language == 'русский':
            alphas = 32
            low_alphabet = lower_rus_alphabet
            upp_alphabet = upper_rus_alphabet
        if language == 'английский':
            alphas = 26
            low_alphabet = lower_eng_alphabet
            upp_alphabet = upper_eng_alphabet

        if text[i].isalpha():
            if text[i] == text[i].lower():
                place = low_alphabet.index(text[i])
            if text[i] == text[i].upper():
                place = upp_alphabet.index(text[i])

            if direction == 'дешифровать':
                index = (place - int(step)) % alphas
            elif direction == 'шифровать':
                index = (place + int(step)) % alphas

            if text[i] == text[i].lower():
                print(low_alphabet[index], end='')
            if text[i] == text[i].upper():
                print(upp_alphabet[index], end='')

        else: print(text[i], end='')

caesar(whats_direction, whats_language, whats_step, whats_text)