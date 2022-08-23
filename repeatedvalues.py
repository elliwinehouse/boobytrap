Напишите программу, которая принимает на вход список чисел в одной строке и выводит на экран в одну строку значения, которые встречаются в нём более одного раза.
Для решения задачи может пригодиться метод sort списка.
Выводимые числа не должны повторяться, порядок их вывода может быть произвольным.

numbers = [int(s) for s in input().split()]
newlist = []
i = 0 # счетчик индекса
numbers.sort()
for number in numbers[:-1]:
    if numbers[i] == numbers[i+1]:
        newlist.append(number)
    i+=1
newlist = list(set(newlist))
for elem in newlist:
    print(elem, end = ' ')
