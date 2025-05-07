import os 

os.system('cls')

#faça um programa que receba um numero y de entradas e pare quando for pedido(pergunta), o programa deve organizar as entradas
# em um lista na ordem decrescente, também deve listar a quantidade de vezes que o caractere "5" aparece
# retorne também quantos itens tem a lista

n5 = contador = 0
numeros = []

while True:
    
    entrada = int (input ("Digite um numero: "))
    contador +=1
    
    if entrada == 5:
        
        n5 += 1    
    
    if contador == 1 or entrada > numeros[-1]:
    
        numeros.append(entrada)
        
    else:
        pos = 0
            
        while pos < len(numeros):
                
            if entrada <= numeros[pos]:
                    
                numeros.insert(pos,entrada)
                break
            
            pos+=1
            
    continua = str (input ("Deseja Continuar?[S/N]: "))
    
    if continua in "Nn":
    
        print("Finalizando...")
        break 
               
print(f"A lista ordenada em ordem descrecente ficou: {numeros[::-1]}\nO número de cincos na lista é de {n5}\nForam inseridos {contador} termos na lista.")

                