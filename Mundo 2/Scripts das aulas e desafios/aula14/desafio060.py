# DESAFIO 060: Faça um programa que leia um número qualquer e mostre seu fatorial.
# Ex: 5! = 5 x 4 x 3 x 2 x 1 = 120

from math import factorial

numero = int(input('Digite um número para calcular o Fatorial: '))

# Fazendo com o módulo
# fatorial = factorial(numero)
# print('O fatorial de {} é {}.'.format(numero, fatorial))


# Fazendo no modelo tradicional com while
# i = numero
# f = 1
# print('Calculando {}! '.format(numero), end='')
# while i > 0:
#     print('{}'.format(i), end='')
#     print(' x ' if i > 1 else ' = ', end='')
#     f *= i
#     i -= 1
# print('{}'.format(f))


# Fazendo no modelo tradicional com for
f = 1
print('Calculando {}! '.format(numero), end='')
for i in range(numero, 0, -1):
    print('{}'.format(i), end='')
    print(' x ' if i > 1 else ' = ', end='')
    f *= i
print('{}'.format(f))

