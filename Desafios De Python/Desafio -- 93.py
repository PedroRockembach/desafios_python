import os 

os.system("cls")

__jogador__ = {"jogador":[],"partidas":[],"gol":[]}

#aproveitamento de um jogador de futebol, pergunte o nome, quantas partidas ele ja jogou e quantidade de gols em x partida 

__jogador__["jogador"] = str(input("Digite o nome do jogador: "))
__jogador__['partidas'] = int(input(f"Quantas partidas {__jogador__['jogador']} jogou? "))

for gols in range(1,__jogador__["partidas"]+1):
    
    __jogador__["gol"].append(int(input(f"Quantos gols foram feitos por ele na {gols}° partida: ")))
    
media = float(sum(__jogador__["gol"])) / float(__jogador__["partidas"])

print(f'''
NOME DO JOGADOR: {__jogador__['jogador']}   
QUANTIDADE DE GOLS NO CAMPEONATO: {sum(__jogador__["gol"])}   
QUANTIDADE DE PARTIDAS NO CAMPEONATO: {__jogador__["partidas"]}
MEDIA DE GOLS POR PARTIDA: {media}
      ''')

for i in range(__jogador__["partidas"]):
    
    print(f"Partida => {i} Gols => {__jogador__['gol'][i]}")