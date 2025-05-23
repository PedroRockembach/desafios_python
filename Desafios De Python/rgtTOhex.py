import os

os.system("cls")

r = -20
b = -25
g = -50

if r < 0:
    r = 0

if b < 0:
    b = 0

if g < 0:
    g = 0
   
if r > 255:
    r = 255

if b > 255:
    b = 255

if g > 255:
    g = 255 
hex = (f"{r:02X}") + f"{b:02X}" + f"{g:02X}"
hex = hex.replace('0x','')
    
print(f"{hex}")