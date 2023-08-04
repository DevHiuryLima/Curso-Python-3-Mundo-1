# DESAFIO 070: Crie um programa que leia o nome e o preço de vários produtos. O programa deverá perguntar se o usuário
# vai continuar. No final, mostre:

# A) Qual é o total gasto na compra.
# B) Quantos produtos custam mais de R$ 1000.
# C) Qual é o nome do produto mais barato.

total = totalmil = menor = contador = 0
maisBarato = ''
while True:
    produto = str(input('Nome do Produto: '))
    preco = float(input('Preço: R$'))

    contador += 1
    total += preco

    if preco > 1000:
        totalmil += 1

    if contador == 1 or preco < menor:
        menor = preco
        maisBarato = produto

    resposta = ' '
    while resposta not in 'SN':
        resposta = str(input('Quer continuar? [S/N] ')).strip().upper()[0]
    if resposta == 'N':
        break
print('{:-^40}'.format(' FIM DO PROGRAMA '))
print(f'O total da compra foi R${total:.2f}')
print(f'Temos {totalmil} produtos custando mais de R$1000.00')
print(f'O produto mais barato foi {maisBarato} que custa R${menor:.2f}')
