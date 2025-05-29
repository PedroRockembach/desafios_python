#Cores no terminal
#ansi
###text                    background
 
#30      black       preto          40
#31      red           vermelho   41
#32      green       verde         42
#33      yellow      amarelo    43
#34      blue          azul           44
#35      Magenta  Magenta  45
#36      cyan         ciano         46
#37      grey          cinza         47
#97      white        branco     107
import os
os.system('cls')
b=19
a='10/12'
print(f'bom dia, hoje, dia \033[35m{a}\033[m eu faço \033[31m{b}\033[m')