# Quando quiser importar um módulo no meu script, posso fazer dessas maneiras:

# import <NOME DO MÓDULO> | Importa tudo contido no módulo
# from <NOME DO MÓDULO> import <NOME DA FUNÇÃO> | Importa uma função específica do módulo
# from <NOME DO MÓDULO> import <NOME DA FUNÇÃO 1>, <NOME DA FUNÇÃO 2> | Importa duas ou mais funções específicas do módulo

# Exemplo com um módulo existente:
# import math
# from math import sqrt
# from math import sqrt, ceil

# Praticando
from math import sqrt, floor, ceil
num = int(input('Digite um número: '))
raiz = sqrt(num)
print('A raiz de {} é igual a {}.'.format(num, raiz))
print('A raiz de {} arredondada para baixo é igual a {}.'.format(num, floor(raiz)))
print('A raiz de {} arredondada para cima é igual a {}.'.format(num, ceil(raiz)))


# OBS: Relação de Módulos/Bibliotecas Integradas Disponíveis: https://docs.python.org/3/library/index.html
