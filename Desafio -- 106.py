from os import system

#Faça um mini-sistema que utilize o Interactive Help do Python. O usuário vai digitar o comando e o manual vai aparecer. 
#Quando o usuário digitar a palavra 'FIM', o programa se encerrará. Importante: use cores.

system("cls")

cores = {
    'vermelho': '\033[31m',
    'verde': '\033[32m',
    'amarelo': '\033[33m',
    'azul': '\033[34m',
    'roxo': '\033[35m',
    'ciano': '\033[36m',
    'branco': '\033[37m',
    'fundo_preto': '\033[7;40m',
    'limpa': '\033[m'
    }

def ajuda(comando):
    titulo(f"Acessando comando {comando}")
    print(f"{cores['verde']}",end='')
    help(comando)
    print(f"{cores['limpa']}")
    
    
def titulo(msg,cor='branco'):
    
    tamanho = len(msg)
    print(f"{cores[cor]}",end='')
    print('='*tamanho)
    print(msg.upper())
    print('='*tamanho) 
    print(f'{cores['limpa']}')
    


#PRINCIPAL

while True:
    titulo('sistema_py_help')
    comando = input('Digite uma função ou metodo: ')
    if comando.lower() == 'nao':
        break
    else:
        ajuda(comando)    
titulo("ATE LOGO",'roxo')
 