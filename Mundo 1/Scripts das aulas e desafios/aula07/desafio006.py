# DESAFIO 006: Crie um algoritmo que leia um número e mostre o seu dobro, triplo e raiz quadrada.

n = int(input('Digite um número: '))
print('O número digitado foi {}, o dobro é {}, o triplo é {} e a raiz quadrada é {:.2f}.'.format(n, n * 2, n * 3, n ** (1/2)))

# OBS: Para a raiz quadrada também pe possivel usar: pow(n, (1/2)).
