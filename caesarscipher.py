https://stepik.org/lesson/611485/step/16?unit=606807
И так, ваша задача создать функцию caesar_cipher , которая принимает на вход текст и значение сдвига.

Внутри функции caesar_cipher  необходимо последовательно пройтись по каждому символу и преобразовать его по следующим правилам:

если символ является знаком пунктуации, оставляем его как есть
если это буква, то сместить ее при помощи ранее написанной функции shift_letter 
Закодированный текст необходимо вернуть в качестве ответа. 

glow = []
def shift_letter(letter: str, shift: int) -> str:
    'Функция сдвигает символ letter на shift позиций'
    global glow
    answer = chr(((ord(letter) - 97 + shift) % 26) + 97)
    glow.append(answer)

def caesar_cipher(text: str, offset: int) -> str:
    'Шифр цезаря'
    global glow
    for i in text:
        if i.isalpha():
            shift_letter(i, offset)
        else: glow.append(i)
    glow = ''.join(''.join(glow))
    return glow
