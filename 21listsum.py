Напишите программу, на вход которой подаётся список чисел одной строкой. Программа должна для каждого элемента этого списка вывести сумму двух его соседей. 
Для элементов списка, являющихся крайними, одним из соседей считается элемент, находящий на противоположном конце этого списка. 
Например, если на вход подаётся список "1 3 5 6 10", то на выход ожидается список "13 6 9 15 7" (без кавычек).
Если на вход пришло только одно число, надо вывести его же.
Вывод должен содержать одну строку с числами нового списка, разделёнными пробелом.

numbers = [int(s) for s in input().split()]
i = 0 # счетчик индекса
newlist = []
for number in numbers:
    if len(numbers) == 1:
        for n in numbers:
            print(n)
        break
    elif i == 0:
        amount = (numbers[-1] + numbers[1])
    elif i == len(numbers)-1:
        amount = (numbers[i-1] + numbers[0])
    else:
        amount = (numbers[i-1]+numbers[i+1])
    i += 1
    newlist.append(amount)
for element in newlist:
    print(element, end = ' ')
