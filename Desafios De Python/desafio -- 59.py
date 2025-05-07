import os
from time import sleep

os.system('cls')

#faça um programa que peça dois numeros e mostre um menu pedindo p selecionar se deseja, somar, multiplicar, mostrar o maior
#perguntar se deseja trocar os numeros iniciais ou sair

print('Insira somente numeros inteiros \n [1, 15, -5, -16...] == ✔\n [1.2, 6.9 Cinco...] == X')

n1=int(input('informe o primeiro valor: '))
n2=int(input('Informe o segundo valor: '))

e=''

while  e!= int(5):
    
    print('=-='*20)
    print(' [ 1 ] Somar \n [ 2 ] Multiplicar\n [ 3 ] Maior \n [ 4 ] Novos numeros \n [ 5 ] Sair'), print('=-='*20)
    e=int(input('Qual opção deseja? '))
    
        #print('Opção Invalida, por favor digite uma opção da forma descrita.')
        
    if e == 1:
        
        print(f'A soma entre {n1} + {n2} = {n1+n2}')
        
    elif e == 2:
        
        print(f'A razão entre {n1} x {n2} = {n1*n2}')
        
    elif e == 3:
        
        if n1>=n2:
            
            maior=n1
            
            print(f'O maior valor entre {n1} e {n2} é {maior}')
            
        elif n1==n2:
            
             print('Os dois numeros são iguais, não possuindo um maior que outro')
             
        else:
            
            maior=n2
            print(f'O maior valor entre {n1} e {n2} é {maior}')
            
    elif e == 4:
        
        print('Informe os novos valores:')
        n1=int(input('informe o primeiro valor: '))
        n2=int(input('Informe o segundo valor: '))
        
    elif e == 5:
        
        print('Finalizando...')
        sleep(3)
        
        break
    
    else:
        
        print('Opção Inválida, Por favor digite um valor válido')
    sleep(2)
print('Finalizado.')
