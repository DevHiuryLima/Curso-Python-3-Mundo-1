# DESAFIO 050: Desenvolva um programa que leia seis números inteiros e mostre a soma apenas daqueles que forem pares.
# Se o valor digitado for ímpar, desconsidere-o.

soma = 0
quantidadePares = 0

for i in range(1, 7):
    numero = int(input('Digite o {}° número: '.format(i)))
    if numero % 2 == 0:
        soma = soma + numero
        quantidadePares += 1
print('Você digitou {} números pares. A soma deles é {}.'.format(quantidadePares, soma))
