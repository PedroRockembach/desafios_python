import os 
os.system("cls")

pin = '125344'

if pin.isdigit():
    pin=str(pin)
    digitos = len(pin)
    if digitos == 4 or digitos == 6:
        print(True)
    else:
        print(False)
else:
    print(False)