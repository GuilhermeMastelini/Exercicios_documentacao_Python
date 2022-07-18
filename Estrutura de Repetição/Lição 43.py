# O cardápio de uma lanchonete é o seguinte:
# Especificação   Código  Preço
# Cachorro Quente 100     R$ 1,20
# Bauru Simples   101     R$ 1,30
# Bauru com ovo   102     R$ 1,50
# Hambúrguer      103     R$ 1,20
# Cheeseburguer   104     R$ 1,30
# Refrigerante    105     R$ 1,00
# Faça um programa que leia o código dos itens pedidos e as quantidades desejadas.
# Calcule e mostre o valor a ser pago por item (preço * quantidade) e o total geral do pedido.
# Considere que o cliente deve informar quando o pedido deve ser encerrado.


produtos = ['Cachorro Quente','Bauru Simples','Bauru com ovo', 'Hambúrguer', 'Cheeseburguer', 'Refrigerante',]
codigo = [100, 101, 102, 103, 104, 105]
preco = [1.2, 1.3, 1.5, 1.2, 1.3, 1]
final = []
total = 0

while True:
    try:
        pedido = int(input('Código do produto: '))
        if pedido == 0:
            break
        index_pedido = codigo.index(pedido)
        quantidade = int(input('Quantidade: '))
        valor_pedido = quantidade * preco[index_pedido]
        total += valor_pedido
        valor_limpo = '{:.2f}'.format(valor_pedido)
        valor_limpo = str(valor_limpo)
        valor_limpo = valor_limpo.replace('.',',')
        valor_unidade = '{:.2f}'.format(preco[index_pedido])
        valor_unidade = str(valor_unidade)
        valor_unidade = valor_unidade.replace('.',',')

        nota  = str(produtos[index_pedido])+ ' uni R$'+ valor_unidade + '     ' + str(quantidade) + 'x' + 'R$ '+ valor_limpo
        final.append(nota)

    except:
        print('Erro')

for i in range(len(final)):
    print(final[i])

total = '{:.2f}'.format(total)
total = str(total)
total = total.replace('.',',')
print(f'Valor total R$ {total}')


