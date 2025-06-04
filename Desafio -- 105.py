from os import system
from time import sleep
system("cls")

def linha():
    print("-"*30)

def notas(nome='<nome>',nota1=0,nota2=0,situ=True):
    """Função que aceita uma entrada de note e duas numericas e retorna o "boletim" de um aluno

    Args:
        nome (str, optional): Nome do aluno. Defaults to <nome>.
        nota1 (float, optional): Primeira Nota. Defaults to 0.
        nota2 (float, optional): Segunda Nota. Defaults to 0.
        situ (bool, optional): Variavel opcional para mostrar no fim a situação final do aluno em media 7 . Defaults to True.

    Returns:
        retorna:
        nome:
        nota 1:
        nota 2:
        media:
        if situ==true
        aprovado/reprovado
    """
    
    #opção para adicionar em dict
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
    
    mensagem =(
            f'As nota do aluno: {boletim["nome"]}\n'
            f'Sua primeira nota foi {boletim["nota_um"]}\n'
            f'A segunda foi {boletim["nota_dois"]}\n'
            f'Sua media foi {boletim["media"]:.2f}\n'
            )
    if situ:
        if media >= 7:
            mensagem +='O aluno foi \033[32mAPROVADO\033[m\n'
        else:
            mensagem +='O aluno foi \033[31mREPROVADO\033[m\n'
    return mensagem
        
#PRINCIPAL 

while True:    
    #WHILE ENTRADA E VALIDAÇÃO DE DADOS
    
    linha()   
    
    nome_entrada = str(input("      Digite seu nome: "))        
    nota_um = str(input("       Digite sua nota: "))
    nota_dois = str(input("     Digite a segunda nota: "))
    
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
    


    
    
    