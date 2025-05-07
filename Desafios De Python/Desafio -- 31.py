#crie um programa que pergunte a distancia em km de uma viagem e calcule o preço do km sendo que: até 200km seram cobrados
#0,50 e acima disto 0,45
import os

os.system('cls')

print('-=-'*20)

km=float(input('Quantos kilometros foram percorridos? -->'))

if km<200:
    
    c=km*float(0.50)
    print('-=-'*20)
    print(f'você não passou dos 200km, entâo sua tarifa a ser paga é de {c} ')
    print('-=-'*20)

else:
    
    cm=km*float(0.45)
    print('-=-'*20)
    print(f'Por ter passado dos 200km rodados sua tarifa é de {cm} ')
    print('-=-'*20)