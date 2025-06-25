from os import system

system("cls")

'''O exercício introduz o conceito de manipulação de strings e dicionários.

Como fazer?
Crie um programa que conte quantas vezes cada palavra aparece em uma frase.'''

phrase = str(input("frase = ")).split()

occurrence = {}

for word in phrase:  
    if word in occurrence:
        occurrence[word] += 1
    else:
        occurrence[word] = 1
for item in occurrence:
    print(item,'-', occurrence[item])