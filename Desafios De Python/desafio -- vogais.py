### Exercício 1: Contar Vogais
#Escreva um programa que conte o número de vogais em uma string fornecida pelo usuário.
import os 
os.system('cls')
contador=0
vogais=['a','e','i','o','u']
frase=str(input('Digite uma frase para contarmos o numero de vogais: ')).strip().lower()
for l in frase:
    if l in [vogais]:
        contador+=1
