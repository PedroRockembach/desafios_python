#Progressão aritmetca com while loop

import os 

os.system('cls')

ti=int(input('Informe o primeiro termo da P.A: '))
r=int(input('Informe a razão da P.A: '))
n=1
while n < 11: 
    p2=ti+(n-1)*r
    print(f'{p2}',end=' → ')
    n+=1
print('Fim de Progressão!')
    