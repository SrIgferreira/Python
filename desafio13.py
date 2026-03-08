s=float(input("Digite o salário do funcionário: "))
ns = s + (s * 15 / 100)
print("O novo salário do funcionário com 15% de aumento é: R${:.2f}".format(ns))