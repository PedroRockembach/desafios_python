import os 

#Listas

os.system("cls")


'''
A principal diferença entre listas e tuplas é que listas podem ser mutaveis | Tuplas usam ( ) e listas [ ]
'''

linhas = ['um','dois','tres','quatro','cinco','seis']

print(f'Lista completa -> {linhas}')

if 'seis' in  linhas:
    linhas.remove('seis')
print(linhas)

linhas2 = list(range(6,12))
print(linhas2)

#linhas2.sort() -> Organiza em ordem numerica crescente
#linhas2.sort(reverse=True) -> Organiza em ordem numerica decrescente