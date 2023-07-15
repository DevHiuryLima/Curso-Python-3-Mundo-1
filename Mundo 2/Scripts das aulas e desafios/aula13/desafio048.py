# DESAFIO 048: Faça um programa que calcule a soma entre todos os números ímpares que são múltiplos de três e que se
# encontram no intervalo de 1 até 500.

soma = 0
quantidadeNumeros = 0
for numero in range(1, 501, 2):
    if numero % 3 == 0:  # Se o número for divisível por 3. Ou se o resto da divisão do número é igual a zero (mesma coisa).
        quantidadeNumeros = quantidadeNumeros + 1
        soma += numero
print('A soma de todos os {} números solictados {}'.format(quantidadeNumeros, soma))
