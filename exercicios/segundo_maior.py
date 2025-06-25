from os import system

system("cls")

num = []

for n in range(0,5):
    i = int(input('num = '))
    num.append(i)
num.sort()
print(num[-2])
    