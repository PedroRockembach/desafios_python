#Faça um programa que identifique o nome silva
import os

os.system('cls')

nome=input('\033[31mBom dia, qual seu nome? -->\033[m').strip()

if 'silva' in nome:
    print('Que interessante, seu nome contem silva, o meu tambem!')
else: 
    print('Belo nome, uma pena não ser um silva')
    
os.system('pause')