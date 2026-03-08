n1 = int(input("Digite o primeiro número: "))
n2 = int(input("Digite o segundo número: "))
s = n1 + n2
m = n1 - n2
mult = n1 * n2
d = n1 / n2
e = n1 ** n2
di = n1 // n2
rd = n1 % n2
print("A soma é: {}".format(s), ";", end=" ")
print("A subtração é: {}".format(m), ";", end=" ")
print("A multiplicação é: {}".format(mult), ";", end=" ")
print("A divisão é: {:.3f}".format(d), ";", end=" ")
print("A exponenciação é: {}".format(e), ";", end=" ")
print("A divisão inteira é: {}".format(di), ";", end=" ")
print("O resto da divisão é: {}".format(rd))
