import os 
os.system('cls')

dados = []
pessoa = {}
somatorio = 0


while True:
    
    pessoa['nome'] = str(input("nome:"))
    pessoa['idade'] = float(input("idade: "))
    pessoa['idade'] += somatorio
    
    while True:
        pessoa['genero'] = str(input('genero[M/F] ')).lower()[0]
        if pessoa['genero'] in 'mf':
            break
        print("Erro! digite apenas M ou F.")
        
    dados.append(pessoa.copy())
    
    while True:
        answer = str(input("Deseja adicionar mais pessoas[S/N] ")).lower()[0]
        if answer in 'sn':
            break
        print('erro! digite S ou N')
        
    if answer == 'n':
        break
    
for k,item in enumerate(dados):
            
    print(f"{k} {item}")
if pessoa['genero'] == 'f':
    for mulheres in pessoa['nome']:
        print(mulheres)