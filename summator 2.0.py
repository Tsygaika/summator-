import numpy as np

strok = int(input('Кол-во строк: '))
stolbcov = int(input('Кол-во столбцов: '))

a = np.zeros(strok*stolbcov).reshape(strok, stolbcov)

for i in range(0, len(a)):
    for j in range(0, len(a[i])):
        num = int(input(f'a[{i}][{j}]='))
        a[i][j] = num

while True:
    try:
        s=str(input('Сначала строка,которая изменяется, потом другая строка и коэффициент:'))#например, из первой строки вычесть удвоенную третью это 1,3,-2
        b=s.split(',')
        b[0]=int(b[0])
        b[1]=int(b[1])
        b[2]=int(b[2])
        for i in range(0,len(a[0])):
            a[b[0]-1][i] += b[2]*a[b[1]-1][i]
    except Exception:
        print('Ошибка сохранения массива')

    try:
        for j in range(0,strok):
            for k in range(0,stolbcov):
                print('{0:5}'.format(int(a[j][k])),end=' ')
            print()
    except Exception:
        print('Ошибка вывода массива')
