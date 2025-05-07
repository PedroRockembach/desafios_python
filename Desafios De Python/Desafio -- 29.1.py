import os 

os.system('cls')

v=int(input('a quantos km por hora seu carro estava?-->'))

if v > int(80):
    print('Seu carro estava muito rapido, isso vai te dar uma multa.')
elif v <= int(40):
    print('Seu carro estava muito devagar, tome cuidado, será um aviso verbal apenas.')
else: 
    print('Seu carro estava dentro dos limites, dirija com cuidado.')    
