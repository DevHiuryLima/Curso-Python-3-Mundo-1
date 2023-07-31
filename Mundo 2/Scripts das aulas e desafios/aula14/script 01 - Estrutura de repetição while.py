# Estrutura de Repetição com Teste Lógico

"""
EXEMPLO DIDÁTICO:
enquanto não maçã:
    passo
pega

EXEMPLO COM PYTHON:
while not maçã:
    passo
pega



EXEMPLO DIDÁTICO:
enquanto não maçã:
    se tem_chao:
        passo
    se tem_buraco:
        pula
    se tem_moeda:
        pega
pega

EXEMPLO COM PYTHON:
while not maçã:
    if tem_chao:
        passo
    if tem_buraco:
        pula
    if tem_moeda:
        pega
pega
"""

print('EXEMPLO 1 - Imprime todos os números de 1 a 9, em ordem crescente, usando o laço while.')
c = 1
while c < 10:
    print(c)
    c += 1
print('FIM 1')

print('EXEMPLO 2 - Pede para o usuário inserir um valor N vezes (indefinido), só parando quando 0 for digitado.')
numero = 1
while numero != 0:  # Flag/Condição de Parada
    numero = int(input('Digite um valor: '))
print('FIM 2')

print('EXEMPLO 3 - Pede para o usuário inserir um valor N vezes (indefinido) até que "r" assuma um valor diferente de "S".')
resposta = 'S'
while resposta == 'S':
    numero = int(input('Digite um valor: '))
    resposta = str(input('Quer continuar [S/N]? ')).upper()
print('FIM 3')

print('EXEMPLO 4 - Pede para o usuário inserir N valores (indefinido) e diz quantos destes são pares e quantos são ímpares.')
numero = 1
par = impar = 0
while numero != 0:
    numero = int(input('Digite um valor: '))

    if numero != 0:
        if numero % 2 == 0:
            par += 1
        else:
            impar += 1
print('Você digitou {} números pares e {} números ímpares!'.format(par, impar))
print('FIM 4')
