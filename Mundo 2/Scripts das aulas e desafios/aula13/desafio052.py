# DESAFIO 052: Faça um programa que leia um número inteiro e diga se ele é ou não um número primo.

numero = int(input('Digite um número: '))
soma = 0

for i in range(1, numero +1):
    if numero % i == 0:
        print('\033[33m', end=' ')  # Deixa o número amarelo se for divisível.
        soma += 1
    else:
        print('\033[31m', end=' ')  # Deixa o número amarelo se for divisível.

    print('{} '.format(i), end=' ')

print('\n\033[mO número {} foi divisível {} vezes'.format(numero, soma))

if soma == 2:
    print('E por isso ele É PRIMO!')
else:
    print('E por isso ele NÃO É PRIMO!')
