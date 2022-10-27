Требуется вывести квадрат, состоящий из N×N клеток, заполненных числами от 1 до N2 по спирали (см. примеры).

Входные данные
Программа получает на вход одно число n.

Выходные данные
Программа должна вывести матрицу, заполненную числами от 1 до N2 по спирали, при этом между числами может быть любое количество пробелов. 
Не допускается начинать спираль в ином, кроме верхнего левого, углу, закручивать спираль против часовой стрелки или изнутри наружу.

Sample Input:
3

Sample Output:
1 2 3
8 9 4
7 6 5

n = int(input())
mas = [[0]*n for i in range(n)] # заполняем матрицу нулями
count = 1 # счетчик с единицы
x, y = 0, -1 # текущее положение нашей ячейки по строкам/столбцам
d_row, d_column = 0, 1 # -1 0 1 переменные движения по строкам/столбцам
length = len(str(n**2))
while count <= n**2:
    if 0<=x+d_row<n and 0<=y+d_column<n and mas[x+d_row][y+d_column] == 0:
        x += d_row
        y += d_column
        mas[x][y] = count
        count += 1
    else:
        if d_column == 1:
            d_column = 0
            d_row = 1
        elif d_row == 1:
            d_row = 0
            d_column = -1
        elif d_column == -1:
            d_column = 0
            d_row = -1
        elif d_row == -1:
            d_row = 0
            d_column = 1
for row in mas:
    for elem in row:
        print(str(elem).rjust(length), end=' ')
    print()

ИЛИ:
n = int(input())
lst = [[0] * n for i in range(n)]
i, j, di, dj = 0, 0, 0, 1
for k in range(n * n):
    lst[i][j] = k + 1
    if lst[(i + di) % n][(j + dj) % n]:
        di, dj = dj, -di
    i, j = i + di, j + dj
for line in lst: 
    print(*line)
