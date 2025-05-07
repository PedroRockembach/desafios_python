import os 
from time import sleep

os.system('cls')

#verificador de numeros primos

print('\033[35mBem vindo ao verificador de numeros primos\033[m')

#sleep(2)

print('Carregando...')

#sleep(2)

while True:
    n=int(input('\033[35mInforme o numero a ser verificado: \033[m'))

    cont=0

    for a in range(1,n+1):
        
        if n%a==0:
            
            print(f'\033[32m{a}\033[m',end=' ')
            cont+=1
        else:
            
            print(f'\033[31m{a}\033[m',end=' ')
            
    if cont==1:
        
        print(f'O numero {n} é primo pois só é divisivel por ele mesmo.')        
        
    if cont==2:
        
        print(f'\nO numero {n} possui apenas {cont} divisores, logo ele é PRIMO')
        
    else:
        print(f'\nO numero {n} possui {cont} divisor logo ele NÃO É PRIMO')
        
    resp= str(input('Voce deseja continuar? [S/N]: '))
    
    if resp in 'SsSimsim':
        
        continue
    else:
        
        break
        