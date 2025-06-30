

def resumo(num,a,d): 
    print("-"*30)
    print("RESUMO DOS VALORES".center(30))
    print("-"*30)
    print(f'Valor analisado {moeda(num)}'.center(30))
    print("-"*30)
    print(f'''
    DOBRO      \t{moeda(dobro(num))}
    ACRESCIMO  \t{moeda(aumentar(num,a))}
    DESCONTO   \t{moeda(diminui(num,d))}
    METADE     \t{moeda(metade(num))}
        '''.center(30))
    print("-"*30)    
    
def aumentar(num,porc):
    acrescimo = num + (num*(porc/100))
    return acrescimo

def diminui(num,desc):
    desconto = num - (num*(desc/100))
    return desconto

def dobro(num):
    return num * 2

def metade(num):
    return num / 2

def moeda(num, din = 'R$',formata = True):
    if formata:
        return f'{din}{num:>.2f}'.replace('.',',')
    else:
        return f'{num:.2f}'
    
def dados_monetarios(entrada):
    validade = False
    while not validade:
        msg = str(input(entrada)).replace(',','.').strip()
        
        if msg.isalpha() or entrada.strip() == '':
            print("\033[31mERRO! digite apenas numeros validos!\033[m")
        else:
            validade = True
            return float(entrada)     