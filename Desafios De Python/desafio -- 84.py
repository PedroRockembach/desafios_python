import os 

#faça um programa que leia o nome e peso de varias pessoas e retorne uma lista das mais pesadas(>=100)
# e uma lista das mais leves(<=70) alias de, mostrar o numero de pessoas adicionadas

os.system('cls')

heavy_weight = []
light_weight = []

num = 0

while True:
    
    name = str(input("Enter a name : "))
    weight = int(input("Enter a weight: "))
    
    num+=1
    
    if weight >=70 and weight <100:
        
        light_weight.append(name)
        
    if weight >=100:
        
        heavy_weight.append(name)
        
    asnwer = str(input("Do you want to continue?[Y/N]"))
    
    if asnwer in "Nnnot":
        
        print("Breaking...")
        break
    
print(F"These is the lightest peoples: {light_weight}")
print(F"And these are the heaviest peoples: {heavy_weight}")
print(F"You entered {num} peoples.")
    