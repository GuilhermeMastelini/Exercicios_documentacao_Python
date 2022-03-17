# Cálculo de pi pelo método de Leibniz
a = int(input('Método de Leibniz. Digite o núro de interações para melhorar a precisão '))
b = 0

for i in range(1, a + 1):
    x = ((-1)**(i-1))*((4)/(2*i - 1))
    b = b + x

print (b)
