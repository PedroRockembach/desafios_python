#manipulação de texto, fatiamento de string e indexação
import os
os.system('cls')
frase='matheus tirou 9 em sistemas eletronicos'
print(frase[0:39])
print(frase[14:39])#print de 14:39// sempre um caractere a mais
print(frase[1:40:2])#print de 1 a 40 pulando de 2 em 2
print(frase[:7])#se nao colocar nada antes dos : ele começa do zero
print(frase[28:])#final não indicado, ele vai até o fim
print(len(frase))# mostra o numero de endereços
print(frase.count('h',0,7))#conta o numero de caracteres definidos em intervalo de 0 a 7
print((frase.find('eletronicos')))#acha a string inserida e lhe mostra aonde começa seu index
print('matheus' in frase)
print(frase.replace('matheus','joao pedro'))#troca a palavra matheus por "joao pedro"
print(frase.replace('matheus','joao pedro').upper())#upper transforma as minusculas em maiusculas e replace troca os indices desejados
print(frase.capitalize())
print(frase.title())
frase2='  Quando comecei as aulas do guanabara, nao sAbIa nAdA  '
print(frase2.strip().capitalize())


