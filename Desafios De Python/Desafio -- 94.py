import os

os.system("cls")

velhos = []
idades = []

__dados__ = []
__mulheres__ = []

somaidade = 0

#crie um programa que leia nome, idade e sexo de varias pessoas, guardando os dados de cada pessoa em um dict e todos os dict em uma lista
#por fim mostre quantas pessoas foram cadastradas, a media de idade, uma lista das mulheres, lista de idades acima da media.

while True:
    
    __pessoa__ = {"nome":[],"sexo":[],"idade":[]}
    __pessoa__["nome"].append(str(input("Digite um nome: ")))
    __pessoa__["idade"].append(float(input("Digite a idade: ")))
    #começa a inserir pessoas
    
    idades.append(__pessoa__["idade"][0])
    
    somaidade += __pessoa__["idade"][0]
    #soma das idades
    
    while True:
        
        __pessoa__["sexo"] = str(input("Digite o sexo [M/F]: ")).lower()[0]
        
        if __pessoa__["sexo"] in 'mf':
            
            
            #adiciona qualquer um ao dict pessoa
            if __pessoa__["sexo"] == 'f':
                
                __mulheres__.append(__pessoa__["nome"])
                #se a pessoa que está sendo cadastrada é mulher, adiciona a lista mulheres
                
            break     
        print('Sexo invalido')
            
    __dados__.append(__pessoa__)    
    #adiciona na lista
    
    answer = str(input("Deseja adicionar mais alguem[S/N] "))
        
    if answer in 'Ss': 

        continue
    
    else:
        #faz a media das idades e fecha o loop
        
        mediaidade = somaidade / len(__dados__)    
        print('='*60)
        break
    
print(F" Foram cadastradas {len(__dados__)} pessoas")

for k,pessoa in enumerate(__dados__): 
    #Printa as pessoas da lista    
      
    print(f"\033[31mEssa é a lista {pessoa} - Posição {k}\033[m")
    
print('='*60)    

print(f"A media das idades foi de \033[31m{mediaidade:.2f}\033[m")
#MEDIA

print('='*60) 

#SE HOUVER MULHERES MOSTRA
if len(__mulheres__) > 0: 
    #se houverem mulheres cadastradas
    
    print(f"Estas são as mulheres da lista:") 
    #printa a lista de mulheres
    
    for mulheres in __mulheres__:
        print(mulheres[0])
        
else:
    
    print("A lista não possui mulheres ") 
    
print('='*60)  

#ACIMA DA MEDIA DE IDADE
print("As pessoas com idade acima da média são:")

    #chat gpt salvou muito aqui 
for pessoa in __dados__:
    if pessoa["idade"][0] > mediaidade:
        print(f"{pessoa['nome'][0]} com {pessoa['idade'][0]} anos")

#essa era minha logica que nem anos mostrava       
'''for item in idades:
    if item > mediaidade:
        velhos.append(item)
print("As pessoas mais velhas(com idade acima da media) possuem")
for v in velhos:
    print(f"{v} Anos")   ''' 
print('='*60)     

#APAGA PESSOAS CADASTRADAS
while True:
    delete = input(str(F"Deseja apagar alguma pessoa cadastrada[s/n] ")).lower()

    if delete in 'sS':
        escolha = int(input('Insira numericamente o numero da pessoa a ser deletada: '))
        
        __dados__.pop(escolha)
        
        for k,pessoa in enumerate(__dados__): 
            #Printa as pessoas da lista    
            
            print(f"\033[31mEssa é a nova lista {pessoa} - {k}\033[m")
            
    tf = str(input("Quer apagar mais alguem[s/n] ")).lower()
    
    if tf in 'sS':
        continue
    else:
        break