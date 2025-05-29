import os 

#aula dezesseis - Tuplas
#variaveis compostas do python 
#tuplas - Listas - dicionarios

os.system('cls')

lanche = ('haburger', 'suco', 'pizza', 'pudim')
for c in enumerate(lanche):
    print(f'Eu vou comer {c}.')
    
A=(1,2,3,4,5,6)
B=(7,8,9,2,0)
C=A+B
print(C)
print(C.count(2),'<--- Numero de "2" na tupla C')
del(C)
print(C)