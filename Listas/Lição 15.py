# Faça um programa que leia um número indeterminado de valores, correspondentes a notas,
# encerrando a entrada de dados quando for informado um valor igual a -1 (que não deve ser armazenado).
# Após esta entrada de dados, faça:

# Mostre a quantidade de valores que foram lidos;
# Exiba todos os valores na ordem em que foram informados, um ao lado do outro;
# Exiba todos os valores na ordem inversa à que foram informados, um abaixo do outro;
# Calcule e mostre a soma dos valores;
# Calcule e mostre a média dos valores;
# Calcule e mostre a quantidade de valores acima da média calculada;
# Calcule e mostre a quantidade de valores abaixo de sete;
# Encerre o programa com uma mensagem;

print('Isira notas de 0 à 10\n Digite -1 para encerrar')
print()

l = []

while True:
    try:
        a = input('Digite aqui: ')
        a = a.strip()
        a = a.replace(',','.')
        a = float(a)



        if a == -1:
            break

        elif 0 <= a and a <= 10:
            l.append(a)

        else:

            print('Valor fora do intervalo')

    except:
        print('Comando inválido')

print()

print(f'Foram lidos {len(l)} valores')

print('Os valores informados foram:\n')
print(*l, sep= '; ')
print()


for i in range (len(l)):
    print(l[(i+1)*(-1)])


print()
print('A soma dos valores é ', sum(l))
print()

print('A média dos valores é', sum(l)/len(l))
print()

s = 0

for i in l:

    if i > sum(l)/len(l):
        s += 1

print(f'Há {s} elementos acima da média')
print()

s_2 = 0
for i in l:
    if i < 7:
        s_2 += 1

print(f'Há {s_2} elementos abaixo de 7')
print()

print('FIM')
