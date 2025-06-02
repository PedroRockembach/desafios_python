def lista(a):
    lista_funcao = []
    lista_funcao.append(a)
    return lista_funcao


while True:
    
    entrada = int(input("digite um numero: "))
    lista(entrada)
    
    if entrada < 0:
        break
print(lista_funcao)    
