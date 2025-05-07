import os 

os.system('cls')
f1=0
f2=1

#F{n}=Fn-1+Fn-2
#Crie um programa que o usuario digite um numero inteiro N e o programa retorne o N numero de termos na sequencia de fibonacci

print('-'*25)
print('|      Fibonacci        |')
print('-'*25)

sequencia=int(input('Digite o numero de termos que você deseja mostrar: '))

print(f'{f1} -> {f2}',end= ' -> ')

for f in range(1,sequencia):

    fibonacci = f1+f2
    f1 = f2
    f2 = fibonacci

    print(f'{fibonacci}',end=' -> ')

print(f'Fim de sequência, foram mostrados {f} termos')


