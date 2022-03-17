# Numa eleição existem três candidatos. Faça um programa que peça o número total de eleitores.
# Peça para cada eleitor votar e ao final mostrar o número de votos de cada candidato.


l = []
cda = 0
cdb = 0
cdc = 0
nul = 0

while True:
    try:
        a = int(input('Insira o número de eleitores: '))
        break
    except:
        print('Comando inválido')


print('Escolha entre os candidatos: A, B e C')
print()
print('Qualquer entrada diferente será considerada como voto nulo')


for i in range (a):
    b = input('Vote no seu candidato: ').upper()
    b = b.strip()

    if b == 'A':
        cda += 1

    elif b == 'B':
        cdb += 1

    elif b == 'C':
        cdc += 1

    else:
        nul +=1

l.append(cda)
l.append(cdb)
l.append(cdc)
l.append(nul)
l.sort(reverse = True)

print(f'Candidato A, {cda} votos\nCandidato B, {cdb} votos\nCandidato C, {cdc} votos\nNulos {nul} votos')
