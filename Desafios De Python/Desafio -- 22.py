#ler uma nome, escreve-lo em: maiusculo, minusculo, diga quantas letras tem o nome completo(SEM ESPAÇOS)
#e quantas letras tem o primeiro nome

import os

os.system('cls')

nome=input('\033[31mDiga seu primeiro nome -->')

print(nome.upper())
print(nome.lower())

junto=(nome.replace(' ',''))
dividido=nome.split()

print(len(junto))
print(len(dividido[0]))

