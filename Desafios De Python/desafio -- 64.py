e = soma = cont =  media = 0
maior = float('-inf')
menor = float('+inf')

while e != 999:
    
    e=int(input('\nDigite um valor inteiro: [999 Para parar]'))
    
    if e != 999:
        
        soma+=e 
        cont+=1   
        
    elif cont == 0:
        
        print('Por favor, digite pelo menos UM valor valido, após isso a finalização sera permitida')
        e=0
            
    else:
        
        continue

media = soma/cont       
print(f'\033[32mA soma dos {cont} valores inseridos é de {soma} e a media entre eles é {media}\033[m ')