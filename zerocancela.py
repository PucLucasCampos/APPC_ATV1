import os

soma = 0
ult = 0
pen = 0
zero = 1
cons = 0
desc = 0

os.system('cls')
print("Bem Vindo ao Zero Cancela")
while 1 == 1:
    num = int (input("Número: "))
    if num > 0:
        if pen == 0 or pen!=num:
            pen = ult
        soma += num
        ult = num
        cons+=1
    elif num == 0 and soma>0:
        if zero>3:
            print("só pode 3 zeros parça")
        elif zero<=3:
            soma=soma-ult
            zero+=1
            desc+=1
            cons= cons-1
            ult=pen
    elif num == 0 and soma==0:
        print("Nenhum número para desconciderar")
    elif num < 0:
        break
print("Zero Cancela Finalizado")
print("soma = ", soma)
print("numeros considerados =", cons)
print("numeros desconsiderados =", desc)
        