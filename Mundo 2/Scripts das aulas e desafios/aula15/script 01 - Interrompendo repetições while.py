# Estrutura de Repetição Infinita

"""
EXEMPLO DIDÁTICO:
enquanto Verdadeiro:
    se tem chão:
        passo
    se tem buraco:
        pula
    se tem moeda:
        pega
    se tem troféu:
        pula
        interrompe
pega

EXEMPLO COM PYTHON:
while True:
    if tem_chao:
        passo
    if tem_buraco:
        pula
    if tem_moeda:
        pega
    if tem_trofeu:
        pula
        break
pega
"""

# print('EXEMPLO 1 - Imprime todos os números de 1 a 10, em ordem crescente, usando o comando while.')
# contador = 1
# while contador <= 10:
#     print(contador, '→ ', end='')
#     contador += 1
# print('FIM 1')

# print('EXEMPLO 2 - Pede para o usuário digitar um número infinitas vezes, só parando quando ele digitar 999 (flag).')
# numero = 0
# while numero != 999:
#     numero = int(input('Digite um número: '))
# print('FIM 2')

print('EXEMPLO 4 - Faz o mesmo que o exemplo acima com um loop infinito, porém não soma junto o 999 (flag).')
numero = soma = 0
while True:
    numero = int(input('Digite um número: '))
    if numero == 999:
        break
    soma += numero
print('A soma vale {}.'.format(soma))
print('FIM 4')
