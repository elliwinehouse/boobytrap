Напишите программу, на вход которой подаётся прямоугольная матрица в виде последовательности строк. 
После последней строки матрицы идёт строка, содержащая только строку "end" (без кавычек, см. Sample Input).

Программа должна вывести матрицу того же размера, у которой каждый элемент в позиции i, j 
равен сумме элементов первой матрицы на позициях (i-1, j), (i+1, j), (i, j-1), (i, j+1). 
У крайних символов соседний элемент находится с противоположной стороны матрицы.

В случае одной строки/столбца элемент сам себе является соседом по соответствующему направлению.

matrix = []
while True:
    str = input()
    if str == 'end':
        break
    row = str.split()
    for i in range(len(row)):  # преобразование элементов в число
        row[i] = int(row[i])
    matrix.append(row)

row = len(matrix)
column = len(matrix[0])
new = [[0]*column for i in range(row)]

for i in range(row):
    for j in range(column):
        if j < column-1 and i < row-1:
            new[i][j] = matrix[i][j+1] + matrix[i][j-1]+ matrix[i+1][j] + matrix[i-1][j]
        elif j >= column-1 and i < row-1:
            new[i][j] = matrix[i][0] + matrix[i][j - 1] + matrix[i + 1][j] + matrix[i - 1][j]
        elif i >= row-1 and j < column - 1:
            new[i][j] = matrix[i][j+1] + matrix[i][j - 1] + matrix[0][j] + matrix[i - 1][j]
        else:
            new[i][j] = matrix[i][0] + matrix[i][j - 1] + matrix[0][j] + matrix[i - 1][j]

for i in new:
    print(*i)

ИЛИ:
  
a = []
while True: 
    str = input()
    if str == 'end':
        break
    row = str.split()    
    for i in range(len(row)): # преобразование элементов в число
        row[i] = int(row[i])
    a.append(row)
for i in range(len(a)):    # старт вывода новой матрицы
    for j in range(len(a[i])):
        print(a[i-1][j] + a[i-len(a)+1][j] + a[i][j-1] + a[i][j-len(a[i])+1], end=' ')
    print()
    
ИЛИ:
  
c = []
while True:
    a = [i for i in input().split()]
    if a == ['end']:
        break
    c.append(a)
n, m = len(c), len(c[0])
for i in range(n):
    for j in range(m):
        x = int(c[i][j-1]) + int(c[i][j+1-m]) + int(c[i-1][j]) + int(c[i+1-n][j])
        print(x, end=' ')
    print()
