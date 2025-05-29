import os 

os.system("cls")

#listas compostas

pessoas = list()

pessoas.append("Pedro")
pessoas.append(25)

usuariosTotal = list()

usuariosTotal.append(pessoas[:])

pessoas[0] = ("joao")
pessoas[1] = (28)

usuariosTotal.append(pessoas[:])

#print(usuariosTotal)

galera = [["rodrigo",21],["joão",15],["carlos",22],["luiza",28]]

for p in galera:
    
    print(f"{p[0]} tem {p[1]} Anos.")