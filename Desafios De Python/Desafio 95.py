import os 

os.system("cls")

time = []

#atualizar o 93 p varios jogadores 

while True:
    #while geral, pergunta varios jogadores
    
    jogador = {'nome':[],"gols":[]}
    

    jogador['nome'] = input("Digite o nome do jogador: ")
    jogos = int(input("Quantos jogos ele jogou? "))

    print("="*60)
    
    for partidas in range(1,jogos + 1):
        #pergunta gols por partida#
        
        gols = int(input(f"   Quantos gols na partida {partidas}: "))
        
        jogador["gols"].append(gols)
        
    print("="*60)   
    
    while True:
        #valida saida#
        
        saida = input("VOCÊ DESEJA CONTINUAR? [S/N] ").lower()[0]
        
        if saida in 'sn':
            
            time.append(jogador)
            print("="*60)
            break
        print("erro")
        
    if saida == 'n':
        break
    
print("COD---NOME---------GOLS---------TOTAL")   
 
for k,item in enumerate(time):
    #mostra jogadores internos 
    
    print(f' {k}',end=' -> ')
    
    for v in item.values():
       print(f"{str(v):<10} ",end='')  
    print(f"{sum(item['gols']):>8}")
    
print("-="*30)
while True:
    print('Numeros negativos param')
    seletor = int(input("Voce deseja mostrar os status de um jogador?se sim, qual?[COD] "))
    
    print("-="*30)   
    if seletor < 0:
        break 
    
    elif seletor >= len(time):
        print("JOGADOR INVALIDO")

    else:
        for item in time[seletor].values():
            print(f"{item}")