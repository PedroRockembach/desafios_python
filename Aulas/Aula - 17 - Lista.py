import os 

#Listas

os.system("cls")


'''
A principal diferença entre listas e tuplas é que listas podem ser mutaveis | Tuplas usam ( ) e listas [ ]
'''

linhas = ['um','dois','tres','quatro','cinco']

print(f'Lista completa -> {linhas}')
print(f'Especifico -> {linhas[2]}')

#.append() --> adiciona no final da lista

linhas.append('seis')

print(f'Append -> {linhas}')

#.insert(posição,item) --> adiciona em algum lugar da lista, especificado pelo primeiro item

linhas.insert(0,'seis')

print(f'Insert -> {linhas}')

#del(posição) --> apaga o item daquela posição

del linhas[0]

print(f'del -> {linhas}')

#lanche.pop() --> geralmente apaga o ultimo, mas pode ter um parametro especifico

linhas.pop(1)

print(f'pop -> {linhas}')

#lanche.remove(item) --> geralmente apaga o ultimo, mas pode ter um parametro especifico

linhas.remove('seis')

print(f'remove -> {linhas}')