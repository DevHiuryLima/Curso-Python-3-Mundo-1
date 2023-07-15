# DESAFIO 054: Crie um programa que leia o ano de nascimento de sete pessoas. No final, mostre quantas pessoas ainda não
# atingiram a maioridade e quantas já são maiores.

from datetime import date

anoAtual = date.today().year
totalMaiores = 0
totalMenores = 0

for pessoa in range(1, 8):
    nascimento = int(input('Digite o ano de nascimento da {}° pessoa: '.format(pessoa)))
    idade = anoAtual - nascimento

    if idade >= 21:
        totalMaiores = totalMaiores + 1
    else:
        totalMenores += 1

print('Ao todo tivemos {} pessoas maiores de idade.'.format(totalMaiores))
print('E também tivemos {} pessoas menores de idade.'.format(totalMenores))
