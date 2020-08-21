# Calcule a area de uma parede e descubra a quantidade de tinta necessaria para pinta-la#
altura = float (input('Digite a altura da parede: '))
larg = float (input ('Digite a Largura da parede: '))
area = (altura * larg)
tinta = (area / 2)
print (' A area total é de {}m² e será necessario {} litros de tinta para a pintura.' .format (area, tinta))
