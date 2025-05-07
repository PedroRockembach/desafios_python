import os 
os.system('cls')
#fatorial com for
n=int(input('Digite um numero para encontrar seu fatorial:  '))
for c in range(n-1,0,-1):
    print(f'{c} x' if c > 1 else '1 =',end=' ')
    n*=c
    c-=1
print(n)