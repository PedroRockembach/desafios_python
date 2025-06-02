#desafio 96

import os

#calcula area atraves de uma func

os.system("cls")

def area(lrg,cmp):
    
    area = lrg*cmp 
    print(f"A area do terreno de {lrg} x {cmp} é de {area}m²")

largura = float(input("Digite a largura(m): "))
comprimento = float(input("Digite o comprimento(m): "))

area(largura,comprimento)