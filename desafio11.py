l=float(input("Digite a largura da parede: "))
a=float(input("Digite a altura da parede: "))
area = l * a
tinta = area / 2
print("A área da parede é: {}m²".format(area), ";", end=" ")
print("A quantidade de tinta necessária para pintar a parede é: {}L".format(tinta))