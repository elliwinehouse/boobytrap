586A // Когда Серёже было три года, ему подарили на день рождения набор карточек с буквами. 
С их помощью было записано словами любимое число мамы мальчика в двоичной системе счисления. 
Серёжа тотчас же принялся с ними играть, но так как не умел читать, перемешал их в случайном порядке. 
Папа решил привести в порядок карточки. 
Помогите ему восстановить исходное число при условии, что оно было максимально возможным.

Входные данные
Первая строка содержит одно целое число n (1⩽n⩽105) — длина строки. 
Вторая строка содержит строку из строчных латинских букв: «z», «e», «r», «o» и «n».

Гарантируется, что буквы можно переупорядочить таким образом, чтобы они образовывали последовательность слов, 
каждое из которых является либо словом «zero», что соответствует цифре 0, либо словом «one», что соответствует цифре 1.

Выходные данные
Выведите максимально возможное число в двоичной системе счисления. Выводите двоичные цифры, разделяя их пробелами. Лидирующие нули допустимы.

n = int(input())
s = input()
print(('1 ' * s.count('n')) + ('0 ' * s.count('z')))
