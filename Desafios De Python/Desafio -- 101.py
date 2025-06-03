from os import system
#from time import sleep

system("cls")

def voto(ano):
    from datetime import datetime
    
    ano_atual = datetime.now().year
    idade = ano_atual - ano
        
    if idade >= 18 and idade < 70:
        return f'Com {idade} anos seu voto é OBRIGATORIO'   
    elif (16 <= idade < 18) or idade > 70:
        return  f'Com {idade} anos seu voto é OPCIONAL'   
    elif idade < 16:
        return f'Com {idade} anos seu voto foi NEGADO'
#Main()

while True:
    nascimento = int(input("Em que ano você nasceu? "))
    print(voto(nascimento))
    continuar = int(input("Voce deseja continuar?[1/0] "))
    if continuar == 0:
        print('FINALIZANDO...')
        break
    else:   
        system("cls")
        continue
    