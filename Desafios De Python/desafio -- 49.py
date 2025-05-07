import os

os.system('cls')

a=int(input('Digite um numero para ver sua tabuada: '))

for c in range(1,11):
    
    r=c*a
    print(f'{c} X {a} = {r}')