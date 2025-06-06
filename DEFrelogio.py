import time 
from os import system

system("cls")
def relogio ():
    while True:
        hora_atual = time.strftime('%H:%M:%S')
        
        '''if hora_atual == '08:13:10':
            print(f"ALARMANDO AGORA\nHORA = {hora_atual}")'''
        #alarme
        print(hora_atual)
        time.sleep(1)
        system("cls")
        
