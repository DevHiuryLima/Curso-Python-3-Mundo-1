# DESAFIO 038: Escreva um programa que leia dois números inteiros e compare-os, mostrando na tela uma mensagem:

# O primeiro valor é maior.
# O segundo valor é maior.
# Não existe valor maior, os dois são iguais.

numero1 = int(input('Digite o primeiro número inteiro: '))
numero2 = int(input('Digite o segundo número inteiro: '))

if numero1 > numero2:
    print('{} é maior do que {}!'.format(numero1, numero2))
elif numero1 < numero2:
    print('{} é menor do que {}!'.format(numero1, numero2))
else:
    print('{} e {} são números exatamente iguais!'.format(numero1, numero2))
