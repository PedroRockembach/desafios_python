import os
os.system('cls')

# Thi1s is2 3a T4est

formatado=[]
formatado_novo = ''
n_possiveis = ['1','2','3','4','5','6','7','8','9']
sentence = "is2 Thi1s T4est 3a" 

for pos in n_possiveis:   
    for i in sentence.split():        
        if pos in i:
            formatado.append(i)            
for s in formatado:
    formatado_novo += s + ' '
print (f'{formatado_novo}')  