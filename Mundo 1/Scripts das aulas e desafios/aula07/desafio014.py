# DESAFIO 014: Escreva um programa que converta uma temperatura digitada em ºC e converta para ºF.

celsius = float(input('Digite a temperatura em ºC: '))
fahrenheit = 9 * celsius / 5 + 32
print('{:.1f}ºC é igual a {:.1f}ºF!'.format(celsius, fahrenheit))
