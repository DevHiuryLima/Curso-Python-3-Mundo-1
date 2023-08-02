# F Strings

# OBS: A partir da versão 3.6, o Python incluiu uma PEP onde passou a suportar F Strings, que ajudam a simplificar a
# formatação de variáveis no meio de prints e textos dentro de outras váriaveis.

"""
Métodos existentes:

Método no Python 2 - %:
numero = 10
print('Dez é igual a %d.' % (numero))

Método no Python 3 - Format:
numero = 10
print('Dez é igual a {}.'.format(numero))

Método no Python 3.6+ - F String:
numero = 10
print(f'Dez é igual a {numero}.')
"""

nome = 'José'
idade = 33
salario = 987.3

print('EXEMPLO 1:')
print(f'O {nome} tem {idade} anos.\n')

print('EXEMPLO 2:')
print(f'O {nome} tem {idade} anos e ganha R${salario:.2f}.\n')
