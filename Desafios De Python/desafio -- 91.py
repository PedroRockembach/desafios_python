import os
import random
from time import sleep
os.system("cls")

jogo = {"jogador":[],"jogadas":[],"desempate":[]}  # Lista de pessoas e jogadas de cada pessooa

for i in range(0,4):
    
    jogo ["jogador"].append((input("Nome do jogador: "))) # add um numero x de coisas a uma lista
    jogo ["jogadas"].append(random.randint(1,6)) # add um numero numero aleatorio 
    
    print("\033[31mPlayer adicionado com sucesso! \033[m")
    
for indice,item in enumerate(jogo["jogador"]): 
        #a função enumerate permite listar coisas como pares onde um é indice e outro é valor
    
    print(f"O jogador {item} e sua rolada foi {jogo["jogadas"][indice]}") 
        #retorna indice e item formatados
    
vencedor = jogo['jogadas'].index(max(jogo['jogadas']))  
    #pega a posição que teve maior valor 
    
ind = [i for i, val in enumerate(jogo['jogadas']) if val == max(jogo['jogadas'])] 
        # faz um for q percorre a lista pegando o valor e indice e compara c o valor maximo, 
# retornando uma lista de indices repetidos ao indice maximo 

if len(ind) > 1: 
        # se ind maior que um(numeros maximo repetidos)
    
    print("Empate, rejogando os dados para os empatados.")
    
    sleep(2)
    
    while True:
        jogo['desempate'].clear()
        
        for i in ind:
            
            nova_jogada = random.randint(1,6)
            
            jogo['desempate'].append(nova_jogada)
            
        for pos, i in enumerate(ind):
            print(f"o jogador {jogo['jogador'][i]} jogou {jogo['desempate'][pos]} no desempate ")
            
        numero_maior = max(jogo['desempate'])    
            
        indice_maior = jogo['desempate'].index(numero_maior)    
            
        maior_valor_desempate = ind[indice_maior]
        

        novos_empates = [i for i, val in enumerate(jogo['desempate']) if val == numero_maior] 
       
               
        if len(novos_empates) > 1:
            
            continue
        
        else:
            
            print(f"O Vencedor final foi \033[1;32m{jogo['jogador'][maior_valor_desempate]}\033[m e seu numero foi {numero_maior}.")
            break
else: 
     
    print(f"O maior valor foi \033[1;32m{max(jogo['jogadas'])}\033[m o vencedor foi {jogo['jogador'][vencedor]}")
    
    

