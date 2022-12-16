from random import *

digits = '0123456789'
lowercase_letters = 'abcdefghijklmnopqrstuvwxyz'
uppercase_letters = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
punctuation = '!#$%&*+-=?@^_'
chars = ''

password_count = int(input('Введите количество паролей для генерации: '))
password_length = int(input('Введите длину одного пароля: '))
digital = input('Включать ли цифры 0123456789? (y/n) ')
caps = input('Включать ли прописные буквы ABCDEFGHIJKLMNOPQRSTUVWXYZ? (y/n) ')
lowercase = input('Включать ли строчные буквы abcdefghijklmnopqrstuvwxyz? (y/n) ')
characters = input('Включать ли символы !#$%&*+-=?@^_? (y/n) ')
exception = input('Исключать ли неоднозначные символы il1Lo0O? (y/n) ')

if digital == 'y': chars += digits
if caps == 'y': chars += uppercase_letters
if lowercase == 'y': chars += lowercase_letters
if characters == 'y': chars += punctuation
if exception == 'y':
    for i in 'il1Lo0O':
        chars = chars.replace(i, '')

def generate_password(length, chars):
    password = ''.join(sample(chars, length))
    return password

for _ in range(password_count):
    print(generate_password(password_length, chars))