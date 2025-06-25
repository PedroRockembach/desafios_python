from os import system

system("cls")

votos = ["A", "B", "A", "C", "C", "A", "C", "C", "B", "A"]

votos_dict = {
    "A":[],"B":[],"C":[]
             }

votos_dict["A"] = votos.count("A")
        
votos_dict["B"] = votos.count("B")
    
votos_dict["C"] = votos.count("C")

for chave in votos_dict:
    print(chave,'-',votos_dict[chave])    