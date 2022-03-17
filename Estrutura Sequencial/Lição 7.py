# Faça um Programa que calcule a área de um quadrado, em seguida mostre o dobro desta área para o usuário

a = float(input('Dígite o lado do quadrado '))

area= a ** 2
area2 = (a**2) * 2
diagonal = a*(2**(1/2))
perímetro = a*4
print('A área do quadrado é igual à {} \n O dobro da área é igual à {} \n A diagonal do quadrado é igual à {} \n O perímetro do quadrado é igual à {}'.format(area, area2, diagonal, perímetro) )
