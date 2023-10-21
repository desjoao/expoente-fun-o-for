p = 1
n = int(input('Insira um valor numérico inteiro e maior do que zero: '))
e = int(input('Insira um expoente inteiro e maior do que 1: '))
if n <= 0:
    print ('Valor inválido, pois menor ou igual a zero')
elif e <= 1:
    print ('Valor inválido, pois menor ou igual a um')
else:
    for i in range (1, e+1):
        p = p * n
    print (p)
