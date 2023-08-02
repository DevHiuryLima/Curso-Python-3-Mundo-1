# DESAFIO 063: Escreva um programa que leia um número n inteiro qualquer e mostre na tela os n primeiros elementos de
# uma Sequência de Fibonacci.

# Ex: 0 → 1 → 1 → 2 → 3 → 5 → 8

print('-' * 30)
print('Sequência de Fibonacci')
numero = int(input('Quantos termos você quer mostrar? '))
termo1 = 0
termo2 = 1

print('~' * 30)
print('{} → {}'.format(termo1, termo2), end='')

i = 3
while i <= numero:
    termo3 = termo1 + termo2
    print('→ {}'.format(termo3), end='')
    termo1 = termo2
    termo2 = termo3
    i += 1
print(' → FIM.')
print('~' * 30)
