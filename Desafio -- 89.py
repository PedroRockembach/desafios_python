import os 

#Faça um programa que receba duas notas de cada aluno e salve todas as informações em uma lista completa, por fim mostre um boletim mostrando a media de cada aluno e 
#pergunte ao usuario se o mesmo gostaria de ver alguma nota separadamente

os.system("cls")
boletim = [[],[],[]] #Nome - Prova 1 - Prova 2

while True:
    
    print("="*30)
    
    nome = str (input("Digite seu nome: "))
    
    prova_um = float (input("Digite a nota da primeira prova: "))
    prova_dois = float (input("Digite a nota da segunda prova: "))
    
    boletim[0].append(nome)
    boletim[1].append(prova_um)
    boletim[2].append(prova_dois)
    
    saida = str(input("Desaja continuar? [S/N] ")).lower()
    
    if saida in "nnao":
        
        break
  
print("="*30)

print(f"Boletim Escolar Semestral:\n{"nO":<3}{"Nome":>10}{"Nota":>14}")

print("-"*30)

for b in range(len(boletim[0])):
    
    print(f"{b:<4}{boletim[0]:>10}{(boletim[1]+boletim[2])/2:>12}")
    
print("="*30)
    