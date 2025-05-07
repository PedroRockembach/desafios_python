#fatorial é o caralho

import os 
os.system('cls')

n=int(input('Digite um numero para encontrar seu fatorial: '))

c=n
f=1

print(f'{n}! é igual a: ',end='')

while c > 0:
    
    print(f'{c}', end = '')
    print(f' x ' if c > 1  else ' = ', end = '' )
    f*=c
    c -= 1
    
print(f)
    
