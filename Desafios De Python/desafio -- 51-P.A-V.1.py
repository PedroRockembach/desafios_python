#desenvolva um programa que leia o primeiro termo e a razão de uma p.a
# e por fim mostre os 10 primeiros termos dessa progressão

import os 

os.system('cls')

p=int(input('informe o primeiro termo da pa: '))
r=int(input('agora informe a razão dessa função: '))

for n in range(1,11):
    
    p2=p+(n-1)*r
    print(f'{p2}',end=' → ')
    
print('Fim de Progressão!')
    