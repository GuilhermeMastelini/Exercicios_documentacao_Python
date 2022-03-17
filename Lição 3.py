#Faça um programa que leia e valide as seguintes informações:
#Nome: maior que 3 caracteres;
#Idade: entre 0 e 150;
#Salário: maior que zero;
#Sexo: 'f' ou 'm';
#Estado Civil: 's', 'c', 'v', 'd
import Limpeza

l = []
vernome = False
veridade = False
versalario = False
versexo = False
verestado_civil = False

while vernome == False:
    nome = input('Digite aqui se nome: ')
    if len(nome) >= 3:
        l.append(nome)
        vernome = True
    else:
        print('O nome deve conter pelo menos três caracteres')
        print('Tente novamente')

while veridade == False:
    idade = input('Digite sua idade: ')
    try:
        idade = Limpeza.limp(idade)
    except:
        idade = -1
    if (idade >= 0) and (idade <= 150):
        l.append(idade)
        veridade = True
    else:
         print('A idade deve ser entre 0 e 150 anos')
         print('Tente novamente')

while versalario == False:
    salario = input('Digite seu salario: R$ ')
    try:
        salario = salario.replace('.','')
        salario = Limpeza.limp(salario)
    except:
        salario = -1
    if salario >= 0:
        l.append(salario)
        versalario = True
    else:
        print('O salario deve ser um número maior ou igual a zero')
        print('Tente novamente')

while versexo == False:
    sexo = input('Digite o Sexo\n (M) para masculino \n (F) para feminino ')
    sexo = sexo.strip()
    sexo = sexo.upper()

    if (sexo == 'M') or (sexo == 'F'):
        l.append(sexo)
        versexo = True
    else:
        print('Comando Invalido\n preencha com M ou F')
        print('Tente novamento')

while verestado_civil == False:
    estado_civil = input('Digite o estado civil\n (c) Casado \n (s) Solteiro \n (v) Viuvo \n (d) Divorciado ')
    estado_civil = estado_civil.strip()
    estado_civil = estado_civil.upper()
    verx = (estado_civil == 'C') or (estado_civil == 'S') or (estado_civil == 'V') or (estado_civil == 'D')

    if verx == True:
        l.append(estado_civil)
        verestado_civil = True
    else:
        print('Comando Invalido')
        print('Tente novamente')

print(l)