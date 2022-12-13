# Personalizações na Sintaxe do Print.

n1 = int(input('Digite um número: '))
n2 = int(input('Digite outro número: '))
s = n1 + n2
m = n1 * n2
d = n1 / n2
di = n1 // n2
e = n1 ** n2

print('A soma é {}, o produto é {} e a divisão é {}'.format(s, m, d))  # Mostra os resultados normalmente.

print('Divisão inteira {} e potência {}'.format(di, e))  # Mostra os resultados normalmente.


print('A soma é {}, o produto é {} e a divisão é {:.3f}'.format(s, m, d))  # Mostra o resultado da divisão com 3 casas
# decimais.

print('A soma é {}, o produto é {} e a divisão é {}'.format(s, m, d), end=' ')  # Mostra o mesmo resultado acima, porém
# sem quebrar a linha e dando um espaço ao invés disso.

print('A soma é {}, \no produto é {} \ne a divisão é {}'.format(s, m, d))  # Mostra o resultado com duas quebras de linha
# no meio do print.

print('A soma é {}, o produto é {} e a divisão é {}'.format(s, m, d), end=' >>> ')  # Mostra o resultado sem quebrar a
# linha, dando um '>>>' ao invés disso.
