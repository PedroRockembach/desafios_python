import os 

os.system('cls')

#faça um programa que vocÊ digite uma expressão numerica e o programa reconheça se a entrade de parenteses foi feita de
#maneira correta

inicia_parenteses = []
fecha_parenteses = []

expressao = str (input("Digite uma expressão: "))

for c in range(len(expressao)):
      
        if expressao[c] == "(":
            
            inicia_parenteses.append(expressao[c])
            
        if expressao[c] == ")":
            
            fecha_parenteses.append(expressao[c])
            
print(f"parenteses começo: {inicia_parenteses}")
print(f"parenteses final: {fecha_parenteses}")

if len(inicia_parenteses) == len(fecha_parenteses):
    
    print("Você digitou corretamente os parêntes.")
else:
    
    print("Os parênteses possuem algum erro.")