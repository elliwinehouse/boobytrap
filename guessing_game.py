from random import *

def is_valid(num):
    return num.isdigit() and 1 <= int(num) <= 100

def numeric_input():
    while True:
        n = input()
        if  is_valid(n) == False:
            print('А может быть все-таки введем целое число от 1 до 100?')
        else: return int(n)

def number_comparison(up_number):
    number = randint(1, up_number)
    print(number)
    count = 0
    while True:
        n = numeric_input()
        count += 1
        if n < number:
            print('Не, надо число побольше, попробуйте еще разок')
        elif n > number:
            print('Не, введите число поменьше, попробуйте еще разок')
        else:
            print('Вы угадали, поздравляем!')
            print(f'Число ваших попыток: {count}')
            break

def continue_game():
    answer = input("Хотите продолжить ('да'/'нет')? ")
    while True:
        if (answer.isalpha()) and (answer in ['да', 'нет']):
            if answer == 'нет':
                print('Спасибо, что играли в числовую угадайку. Еще увидимся...')
                return False
            elif answer == 'да':
                return True
        else:
            print("Не тупите, ответом может стать только 'да' или 'нет'!")
            answer = input("Хотите продолжить ('да'/'нет')? ")

def game():
    print('Добро пожаловать в числовую угадайку!')
    print('Правила очень просты: задаете диапазон, в котором генерируется случайное число, ваша задача его угадать:)')
    while True:
        print('Введите, в каком диапазоне вы хотите угадывать числа.\nПредел от 1 до 100! ')
        x = numeric_input()
        print(f'Введите число от 1 до {x}: ')
        number_comparison(x)
        if continue_game(): continue
        else: break

game()