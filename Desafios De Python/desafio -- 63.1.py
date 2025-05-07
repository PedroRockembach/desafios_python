import os

os.system('cls')
f1=0
f2=1
contador=3
r=0

#fibonacci com while loop
#F{n}=Fn-1+Fn-2

print('-'*25)
print('|      Fibonacci        |')
print('-'*25)


sequencia=int(input('Digite o numéro de termos de fibonacci que você deseja ver: '))

print(f'{f1} -> {f2}',end = ' ')

while contador <= sequencia:
    
    fibonacci = f1+f2
    f1=f2
    f2=fibonacci
    contador +=1
    r+=1
    print(f'-> {fibonacci}', end= ' ')
   
print(f'Fim de sequência, foram mostrados {r} termos. ')
