a=[[1,1,-1,1,-4,2,3],
   [-3,-2,5,3,-11,-22,176],
   [-2,5,3,2,-13,-26,176],
   [-5,4,5,-3,5,-30,120]]
strok = 4
stolbcov = 7
while True:
    s=str(input('Сначала строка,которая изменяется, потом другая строка и коэффициент:'))#например, из первой строки вычесть удвоенную третью это 1,3,-2
    b=s.split(',')
    b[0]=int(b[0])
    b[1]=int(b[1])
    b[2]=int(b[2])
    for i in range(0,len(a[0])):
        a[b[0]-1][i] += b[2]*a[b[1]-1][i]

    for j in range(0,strok):
        for k in range(0,stolbcov):
            print('{0:5}'.format(a[j][k]),end=' ')
        print()