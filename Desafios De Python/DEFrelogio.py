import time 
from datetime import datetime
from os import system

system("cls")

def relogio ():
    
    while True:
        
        hora_atual = time.strftime('%H:%M:%S')
        dia_atual = datetime.now().strftime(" %d/%m/%Y")
        
        #if hora_atual == '08:13:10':
        #    print(f"ALARMANDO AGORA\nHORA = {hora_atual}")
        #    alarme
        
        print(hora_atual)
        print(dia_atual)
        
        time.sleep(1)
        system("cls")
        
relogio()
        
        
