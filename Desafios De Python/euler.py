import os 
os.system("cls")

__sum__ = 0

for numero in range(entrada):
    
    if numero % 3 == 0 or numero % 5 == 0:
        __sum__ += numero
print(__sum__)

