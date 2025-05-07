import os 
from time import sleep

os.system('cls')

#Melhore o desafio 61 perguntando ao usuario se ele quer mostrar mais alguns termos, o programa deve encerrar quando o usuario 
#disser que quer mostrar 0 termos a mais.

print('\033[35mSuper programa gerador de P.A\033[m')

sleep(2)

p=int(input('\033[36mDigite o primeiro termo da sua P.A: '))
r=int(input('Informe a razão da sua P.A: '))
c=1
continua=' '
contagem=10

#bonito

while c < 11:
    
    pa=p+(c-1)*r
    print(f'\033[m{pa}',end=' → ')
    c+=1

print('PAUSA')

while continua != 0:
    
    continua=int(input('deseja continuar? digite o numero de termos a mais: '))
    
    if continua != 0:
        p=pa
        for c in range(2,continua+2):
            
            pa=p+(c-1)*r
            print(f'\033[m{pa}',end=' → ')
            contagem+=1
            
        print('PAUSA')
        
print(f'Fim de programa com {contagem} mostrados ')
