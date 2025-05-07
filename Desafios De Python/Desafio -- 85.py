import os 

#crie um programa que o usuario possa cadastrar 7 valores e os cadastre em uma lista unica que mantenha separado os valores pares e impares, por fim mostre os valores pares e impares em ordem crescente
os.system("cls")

dados_total = [[],[]]

for c in range(1,8):
    
    num = int(input("insira um numero: "))
    
    if num % 2 == 0:
        
        dados_total[0].append(num)
    else:
        
        dados_total[1].append(num)       
    
print(sorted(dados_total[0]))
print(sorted(dados_total[1]))