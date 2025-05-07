import os 

os.system('cls')

#faça um programa que vocÊ digite uma expressão numerica e o programa reconheça se a entrade de parenteses foi feita de
#maneira correta

pilha = []

expressao = str (input("Digite uma expressão: "))

for c in range(len(expressao)):
      
        if expressao[c] == "(":
            
            pilha.append(expressao[c])
            
        if expressao[c] == ")":
            
            if len(pilha) > 0:
                
                pilha.pop()
                
            else:
                print("erro nos parenteses")
                break


if len(pilha) == 0:
    print("Você digitou corretamente os parentes.")
else:
    print("parenteses abertos sem fechamento")    