#aula 20 

import os 
os.system("cls")

def mostra_linha():
    print("-="*20)
    
#()
def calcula(a,b):
    c = int(a)+int(b)
    return c

'''n1 = str(input("digite um numero: "))
n2 = float(input("digite outro: "))
print(calcula(n1,n2))'''

'''def titulo(a):
    mostra_linha()
    print(f'{a.upper():<7}')
    mostra_linha()'''
'''texto = input("titulo: ")'''

#titulo('processamento de dados')

def titulo(msg):
    mostra_linha()
    print(f"{msg.upper():>22}")
    mostra_linha()
titulo('lifemed')

#desempacota


def somatorio(*num):
    saida = 0
    for i in num:
        saida += i
    print(saida)


somatorio(1,2,3,4,5,6,7,8,9)