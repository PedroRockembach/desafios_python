import os 

os.system('cls')

#faça um programa que receba os itens de uma lista, após finalizada, ele deve criar outras duas listas
#nelas deve conter, uma lista de pares e uma lista de impares

numeros = []
numeros_par = []
numeros_impar = []

for lista in range(0,6):
    
    entrada=int(input("Adicione um item a lista: "))
    
    numeros.append(entrada)
    
    if entrada%2==0:
        
        numeros_par.append(entrada)
        
    if entrada%2!=0:
        
        numeros_impar.append(entrada)
  
print(f"Lista total: {numeros}")
print(f"Lista par: {numeros_par}")
print(f"Lista impar: {numeros_impar}")