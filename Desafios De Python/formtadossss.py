import os 
os.system("cls")

sequence = "is2 Thi1s T4est 3a"
sequencia = ""
n_possibilidades = ["1","2","3","4","5","6","7","8","9"]
formatado = []
for pos in n_possibilidades:
    
    for i in sequence.split():
        
        if pos in i:
        
            formatado.append(i)
for s in formatado:
    sequencia+=s+' '
print(sequencia)