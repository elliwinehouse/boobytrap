Напишите программу, которая получает на вход три целых числа, по 
одному числу в строке, и выводит на консоль в три строки сначала 
максимальное, потом минимальное, после чего оставшееся число.

На ввод могут подаваться и повторяющиеся числа.

# put your python code here
a = int(input())
b = int(input())
c = int(input())

print(max(a,b,c))
print(min(a,b,c))
if a<=b<=c:
    print(b)
elif b<=c<=a:
    print(c)
elif c<=a<=b:
    print(a)
elif c<=b<=a:
    print(b)
elif a<=c<=b:
    print(c)
elif b<=a<=c:
    print(a)
