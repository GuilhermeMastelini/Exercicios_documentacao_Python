#Número por extenso. Escreva um programa que solicite ao usuário a digitação de um número até 99 e
# imprima-o na tela por extenso.

uni = ['zero','um','dois','três','quatro','cinco','seis','sete','oito','nove']

dez_uni = ['dez','onze','doze','treze','quatorze','quinze','dezesseis','dezesete','dezoito','dezenove']

dezenas = ['vinte','trinta','quarenta','cinquenta','sessenta','setenta','oitenta','noventa']


while True:

    try:
        a = int(input('Digite o número: '))

        if a < 0 :
            print('Números negativos não são suportados.')

        elif a > 99:
            print('Números acima de 100 não são suportados')

        else:

            if 0 <= a < 10:
                print(uni[a])

            elif 10 <= a <= 19:
                print(dez_uni[a-10])

            else:
                a = str(a)
                a_1 = int(a[0])
                a_2 = int(a[1])


                if a_2 == 0:
                    print(dezenas[a_1-2])
                else:
                    print(f'{dezenas[a_1-2]} e {uni[a_2]} ')

    except:
        print('Comando Inválido')

    print()

