from os import system

system("cls")

def ficha(nome='<desconhecido>',gols='0'):
    print(f"Jogador: {nome}")
    print(f"Gols: {gols}")

#principal[]

nome = input("Digite o nome do jogador: ").capitalize()
gols = input('Quantos gols ele marcou?')

if gols.isnumeric():
    gols = int(gols)
else: 
    gols = 0
if nome.strip() == '':
    ficha(gols=gols)
else:
    ficha(nome,gols) 

