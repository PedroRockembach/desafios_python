import serial
import os 
import time

arduino = serial.Serial(port='COM4',timeout=1)
time.sleep(2)

def envia_ang(angulo):
    comando = f'{angulo}\n' #adiciona o quebra linha
    arduino.write(comando.encode()) # o .encode transforma em bytes
    
while True:
    angulo = input("digite um angulo: ")
    if angulo.isdigit():
        envia_ang(angulo)
    else:
        print("digite um valor valido")
    
    
