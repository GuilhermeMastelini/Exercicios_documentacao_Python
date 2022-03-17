#Altere o programa anterior para mostrar no final a soma dos números.


while True:
    try:
        a = int(input('Digite o primeiro número: '))
        break
    except:
        print('Comando inválido')

while True:
    try:
        b = int(input('Digite o segundo número: '))
        break
    except:
        print('Comando inválido')
# método computacional
soma = 0

for i in range(a,b+1,1):
    soma += i

print(soma)
 #soma clássica
s = ((a + b)*(b - a + 1))/2
print(s)
