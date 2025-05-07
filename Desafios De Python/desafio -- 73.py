import os 

# em que posição está o time do corinthians

os.system('cls')

times = ('Atlético-MG','Bahia','Botafogo','Bragantino','Ceará','Corinthians','Cruzeiro','Flamengo','Fluminense','Fortaleza','Grêmio','Internacional','Juventude','Palmeiras','Santos','Sport','São Paulo','Vasco','Vitória')   
    #crie uma tupla que contenha os 20 primeiros colocados da tabela do campeonato brasileiro de futebol na ordem de colocação

sorted_teams = sorted(times)

for a in range(0,5):
    
    print(f' {times[a]} ',end = ' -> ')
print('os 5 primeiros colocados')
        #após mostre: os 5 primeiros 
        
print('\n')        

for b in range(-1,-5,-1):  #passo ao contrario
    
#print(f"os ultimos times foram {times[-4:]})  <- opção
  
    print(f' {times[b]} ',end = ' -> ')
print('4 Ultimos colodados')
        #os 4 ultimos 
  
print('\n')    
print("Times em ordem alfabetica")    
 
for c in sorted_teams:   # print( a variavel C equivale a identação que sera printada dentro da tupla.)
        
    print(f' ->  {c}')
        #os times em ordem alfabetica  

print('\n')

for conta,c in enumerate(times):   # print( a variavel C equivale a identação que sera printada dentro da tupla.)
  
#print(f'o corinthians está na {times.index("Corinthians")+1}° posição')  <- opção
#>>>> lista.index(item, inicio, fim) <<<<<
 
    if c is 'Corinthians':
    
        print(f'O Corinthians está na {conta+1}° posição.')
            #os times em ordem alfabetica          
