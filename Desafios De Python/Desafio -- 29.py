import os 

os.system('cls')

v=float(input('a quantos km por hora seu carro estava?-->'))

if v >= float(80):
    
    print('você foi multado, o limite desta via é 80km/h...')
    print(f'sua multa foi de {float(v-(80))*(7.0)}')
else:
    
    if v <= float(30):
        
        if v <= float(15):
            
            print('vai tomar no cu ta muito devagar poha')
            
        else:
            
            print('seu carro está muito lento, será só um aviso mas cuidado!')
    else:
        
        print('pode seguir, você estava no limite!')
    
