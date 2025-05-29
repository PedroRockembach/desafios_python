import os

os.system("cls")

estado = dict()
brasil = list()

for c in range (0,3):
    
    estado ["UF"] = str (input("Digite um estado:"))
    estado ["sigla"] = str (input("Digite a sigla: "))
    
    brasil.append(estado.copy())  #<- funciona como o [:] em listas, faz a copia/fatiamento
   
for u in (brasil):

    #print(brasil) 
    #print(f"Estado = {u}\nSigla = {v}")
    
    print(f"Estado = {u["UF"]}\nSigla = {u["sigla"]}")
    
    