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
        if s[0:5]=='edit:':
            s = s[5:].split(';')
            a[int(s[0])][int(s[1])] = int(s[2])
        else:
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


'''x1 =1
x2 =2
x3 =-4
x4 =-3
print((45)*x1 + (-28)*x2 + (34)*x3 + (-52)* x4, 9)
print((36)*x1 + (-23)*x2 + (29)*x3 + (-43)* x4, 3)
print((35)*x1 + (-21)*x2 + (28)*x3 + (-45)* x4, 16)
print((47)*x1 + (-32)*x2 + (36)*x3 + (-48)* x4, -17)
print((27)*x1 + (-19)*x2 + (22)*x3 + (-35)* x4, 6)'''
