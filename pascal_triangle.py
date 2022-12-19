from math import factorial


def pascal(n):
    lst = []
    for i in range(n + 1):
        result = (factorial(n)) // (factorial(i) * factorial(n - i))
        lst.append(result)
    return lst

for i in range(int(input())):
    print(*pascal(i))
