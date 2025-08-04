import os 

def maior_ocorrencia(dic):
    """Retorna uma lista  com as maiores ocorrenciais de um dicionario

    Args:
        dic (dict): o dicionario que sera varrido

    Returns:
        list: lista somente com o maior valor ou empates
    """
    maior = float('-inf')
    mais_ocorrencia = []
    for chave,valor in dic.items():
        '''print(f"chave: {chave} valor: {valor}")'''
        
        if  valor > maior:

            mais_ocorrencia.clear()
            mais_ocorrencia.append(chave)     
            maior = valor
                    
        elif valor == maior:
            mais_ocorrencia.append(chave)  
    return mais_ocorrencia

def remove_pontuacao(frase,*to_remove ):
    """Remove da "frase" a/s string que estiver no to_remove 

    Args:
        frase (string): frase ou palavra que ira ser transformada

    Returns:
        string: é a frase sem os argumentos do to_remove
    """
    nova_frase = frase
    for i in to_remove:
        
        nova_frase = nova_frase.replace(i,'')
        
    return nova_frase

os.system("cls")
ocorrencias = {}
repete = []

'''
🧠 Desafio: Detector de Palavras Isoladas
Crie um programa que analise uma frase digitada pelo usuário e informe:

Quais palavras aparecem apenas uma vez na frase.

Quais palavras mais se repetem (empate incluso).

A quantidade total de palavras únicas (não repetidas).

📝 Regras:
Ignore letras maiúsculas/minúsculas (case insensitive).

Remova pontuação (como ".", ",", "!", "?") antes da contagem.

Exiba os resultados organizadamente.
'''

frase = str(input("digite uma frase: ")).lower()

frase_nova = remove_pontuacao(frase,',','.','!','?')

frase_divida = frase_nova.split()

for palavra in frase_divida:
    
    if palavra in ocorrencias:
        ocorrencias[palavra] += 1
    else:
        ocorrencias[palavra] = 1
        
for chave,valor in ocorrencias.items():
    if valor == 1:
        repete.append(chave)        
        
x = maior_ocorrencia(ocorrencias)
            
print(f"PALAVRA(S) COM MAIS OCORRENCIA:")

for palavra in x: 
    print(f">> '{palavra}' - {ocorrencias[palavra]}")

print("PALAVRAS QUE APARECEM UMA VEZ")

for palavra in sorted(repete): 
    print(f">> '{palavra}' ")

print(f"NUMERO DE PALAVRAS UNICAS: {len(repete)}")