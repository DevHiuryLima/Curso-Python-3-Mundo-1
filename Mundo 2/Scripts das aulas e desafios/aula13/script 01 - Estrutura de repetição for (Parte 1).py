# Estrutura de Repetição com Variável de Controle

"""
EXEMPLO DIDÁTICO:
laço c no intervalo(1,10):
    passo
pega

EXEMPLO COM PYTHON:
for c in range(1,10):
    passo
pega



EXEMPLO DIDÁTICO:
laço c no intervalo(0,3):
    passo
    pula
passo
pega

EXEMPLO COM PYTHON:
for c in range(1,3):
    passo
    pula
passo
pega



EXEMPLO DIDÁTICO:
laço c no intervalo(0,3):
    se moeda:
        pega
    passo
    pula
passo
pega

EXEMPLO COM PYTHON:
for c in range(1,3):
    if moeda:
        pega
    passo
    pula
passo
pega
"""

print('EXEMPLO 1 - Imprime "Oi" 6 vezes.')
for c in range(0, 6):
    print('Oi')
print('FIM 1')

print('EXEMPLO 2 - Imprime todos os números de 1 a 6 (7 - 1), em ordem crescente.')
for c in range(1, 7):
    print(c)
print('FIM 2')

print('EXEMPLO 3 - Imprime todos os números de 6 a 1, em ordem decrescente.')
for c in range(6, 0, -1):
    print(c)
print('FIM 3')

print('EXEMPLO 4 - Imprime todos os números de 0 a 6, em ordem crescente, pulando de 2 em 2.')
for c in range(0, 7, 2):
    print(c)
print('FIM 4')

print('EXEMPLO 5 - Imprime todos os números de 0 a "n" (entrada do usuário).')
n = int(input('Digite um número: '))
for c in range(0, n + 1):
    print(c)
print('FIM 5')

print('EXEMPLO 6 - Imprime todos os números de inicio a fim, pulando uma quantidade de passos a cada iteração (entradas do usuário).')
inicio = int(input('Início: '))
fim = int(input('Fim: '))
pulando = int(input('Passo: '))
for c in range(inicio, fim + 1, pulando):
    print(c)
print('FIM 6')

print('EXEMPLO 7 - Pede para o usuário inserir um valor diferente 4 vezes e soma todos num resultado final.')
soma = 0
for c in range(0, 4):
    numero = int(input('Digite um valor: '))
    soma += numero
print('O somatório de todos os valores foi {}.'.format(soma))
print('FIM 7')
