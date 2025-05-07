import os 
os.system('cls')
s = cont=0

#faça um programa que mostre na tela a soma dos numeros impares multiplos de 3 de 1 500

for c in range(1,501):
    if c%3==0:
        if c%2!=0:
            s+=c
            cont+=1
            
    else:
        continue
print(s)   
print(cont)     
    
