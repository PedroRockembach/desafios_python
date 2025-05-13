import os 

os.system("cls")

boletim = []
aluno = dict()

#pergunta nome do aluno e media e guarda numa lista com dicionario 
#apos printa tudo na tela e printa a media sendo que 
# aprovado > 7 < reprovado 

aluno ["nome"] = str(input("Digite um nome: "))
aluno ["media"] = int(input("Digite a media do aluno: "))

boletim.append(aluno.copy())

'''for nota in aluno.values():
    
    print(f"O nome do aluno é {nota}")
    print(f"A nota dele foi {nota}")'''
    
if aluno["media"] < 7:
    
    aluno ["situacao"] = str("Reprovado")
else:
    
    aluno["situacao"] = "Aprovado"
    
print(f"O nome do aluno é {aluno["nome"]}")
print(f"A média dele foi {aluno["media"]}")
print(f"O aluno foi {aluno["situacao"]}")