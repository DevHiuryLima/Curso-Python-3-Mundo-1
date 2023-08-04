# DESAFIO 069: Crie um programa que leia a idade e o sexo de várias pessoas. A cada pessoa cadastrada, o programa deverá
# perguntar se o usuário quer ou não continuar. No final, mostre:

# A) Quantas pessoas têm mais de 18 anos.
# B) Quantos homens foram cadastrados.
# C) Quantas mulheres têm menos de 20 anos.

total18 = totalH = totalM20 = 0
while True:
    idade = int(input('Idade: '))
    sexo = ' '
    while sexo not in 'MF':
        sexo = str(input('Sexo [M/F]: ')).strip().upper()[0]

    if idade >= 18:
        total18 += 1

    if sexo == 'M':
        totalH += 1

    if sexo == 'F' and idade < 20:
        totalM20 += 1

    resposta = ' '
    while resposta not in 'SN':
        resposta = str(input('Quer continuar? [S/N] ')).strip().upper()[0]
    if resposta == 'N':
        break

print(f'Total de pessoas com mais de 18 anos: {total18}.')
print(f'Ao todo temos {totalH} homens cadastrados.')
print(f'E temos {totalM20} mulheres com menos de 20 anos.')
