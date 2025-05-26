import os 
os.system("cls")

__label__ = "camelCasing" 
__palavra__ = ''

for letra in __label__:
    
    if ord(letra) >= 65 and ord(letra) <= 90:
        
        __palavra__ += ' '
        __palavra__ += letra
        
    else:
        
        __palavra__ += letra
  
print(__palavra__)