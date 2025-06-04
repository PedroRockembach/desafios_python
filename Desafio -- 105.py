from os import system
from time import sleep
system("cls")

def linha():
    print("-"*30)

def notas(nome='<nome>',nota1=0,nota2=0):
    
    '''
    boletim["nome"].append(nome)
    boletim["nota_um"].append(nota1)
    boletim["nota_dois"].append(nota2)
    boletim["media"].append(media)
    '''
    
    boletim={"nome":[],"nota_um":[],"nota_dois":[],'media':[]}
    
    media = (nota1+nota2)/2

    boletim = {        
        "nome":nome,
        "nota_um":nota1,
        "nota_dois":nota2,
        "media":media        
    }

    
    linha()
    return ( 
            f'As nota do aluno: {boletim["nome"]}\n'
            f'Sua primeira nota foi {boletim["nota_um"]}\n'
            f'A segunda foi {boletim["nota_dois"]}\n'
            f'Sua media foi {boletim["media"]:.2f}\n'
        )
    
#PRINCIPAL 

while True:    
    #WHILE ENTRADA E VALIDAÇÃO DE DADOS
    
    linha()   
    
    nome_entrada = str(input("Digite seu nome: "))        
    nota_um = str(input("Digite sua nota: "))
    nota_dois = str(input("Digite a segunda nota: "))
    
    try:
        nota_um = float(nota_um)
    except ValueError:
        nota_um = 0.0
    #valida entrada de nota 1
    
    try:
        nota_dois = float(nota_dois)
    except ValueError:
        nota_dois = 0.0
        
    if nome_entrada.strip() == '':
        print(notas(nota1=nota_um,nota2=nota_dois))    
    else:
        print(notas(nome_entrada,nota_um,nota_dois))    
    #valida entrada de nome 
    
    linha()
        
    #valida entrada de nota 2
    while True:
        #WHILE DE VALIDAÇÃO DE SAIDA
        
        saida = str(input("Voce deseja continuar? [s/n] "))[0].lower()
        if saida in 'sn':
            system("cls")
            break
            
        print("ERRO!")
    if saida == 'n':
        print("Programa de validação de notas finalizado ")
        break
    


    
    
    