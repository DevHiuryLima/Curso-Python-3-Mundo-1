# DESAFIO 016: Crie um programa que leia um número real qualquer pelo teclado e mostre na tela a sua porção inteira.

# Ex: Digite um número: 6.127
# O número 6.127 tem a parte inteira 6.

from math import trunc

numero = float(input('Digite um valor: '))
print('O valor digitado foi {} e a porção inteira é {}!'.format(numero, trunc(numero)))
