
import os 
os.system('cls')

a=float(input('digite um valor -->'))
b=float(input('digite outro valor -->'))
c=float(input('digite o ultimo valor -->'))

if a<=b+c and b<=a+c and c<=a+b:

    print('Pode ser um triangulo', end=' ')

    if a==b==c:

        print('EQUILATERO')

    elif a!=b!=c:

        print('ESCALENO')

    elif a!=b==c and b!=a==c and c!=b==a:

        print('isosceles')

else: 

    print(' Não pode formar um triangulo')