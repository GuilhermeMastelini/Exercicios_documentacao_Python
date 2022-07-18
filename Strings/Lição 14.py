#Leet spek generator. Leet é uma forma de se escrever o alfabeto latino usando outros símbolos em lugar das
# letras, como números por exemplo. A própria palavra leet admite muitas variações, como l33t ou 1337. O uso do
# leet reflete uma subcultura relacionada ao mundo dos jogos de computador e internet, sendo muito usada para confundir
# os iniciantes e afirmar-se como parte de um grupo. Pesquise sobre as principais formas de traduzir as letras.
# Depois, faça um programa que peça uma texto e transforme-o para a grafia leet speak.

a = input('Mensagem: ')

a = a.lower()
a = a.replace('a','@')
a = a.replace('b','8')
a = a.replace('c','¢')
a = a.replace('d','|)')
a = a.replace('e','3')
a = a.replace('f','|=')
a = a.replace('g','6')
a = a.replace('h','#')
a = a.replace('i','1')
a = a.replace('j','_/')
a = a.replace('k','}<')
a = a.replace('l','£')
a = a.replace('m','|\/|')
a = a.replace('n','{\}')
a = a.replace('o','0')
a = a.replace('p','|º')
a = a.replace('q','9')
a = a.replace('r','|2')
a = a.replace('s','$')
a = a.replace('t','7')
a = a.replace('u','(_)')
a = a.replace('v','\/')
a = a.replace('w',' \/\/ ')
a = a.replace('x','*')
a = a.replace('y','`/')
a = a.replace('z','%')

print(a)