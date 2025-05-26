import os 

os.system("cls")

__pessoa__ = {"nome":[],"sexo":[],"idade":[]}
__dados__ = []
__cadastrados__ = 1

#crie um programa que leia nome, idade e sexo de varias pessoas, guardando os dados de cada pessoa em um dict e todos os dict em uma lista
#por fim mostre quantas pessoas foram cadastradas, a media de idade, uma lista das mulheres, lista de idades acima da media.

while True:
    
    __pessoa__["nome"].append(str(input("Digite um nome: ")))
    __pessoa__["idade"].append(int(input("Digite a idade: ")))

    while True:
        
        sexo = str(input("Digite o sexo [M/F]: ").lower())
        
        if sexo in 'mf':
            
            __pessoa__["sexo"].append(sexo)
            break
        
        else:
            
            print('Sexo invalido')
            
    __dados__.append(__pessoa__) 
       
    answer = str(input("Deseja adicionar mais alguem[S/N] "))
        
    if answer in 'Ss':
        
        __cadastrados__ += 1
        
        continue
    else:
        
        break
    
print(__dados__)          
            



