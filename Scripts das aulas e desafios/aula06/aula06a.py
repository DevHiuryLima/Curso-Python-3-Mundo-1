n1 = int(input('Digite um valor: '))
n2 = int(input('Digite outro valor: '))
soma = n1 + n2

# Alguns métodos de exibir o resultado.

# print('A soma entre', n1, 'e', n2, 'vale', soma)  # Método antigo, do Python 2.
# print('A soma entre {0} e {1} vale {2}'.format(n1, n2, soma))  # Método novo, do Python 3 com números na organização.
print('A soma entre {} e {} vale {}'.format(n1, n2, soma))  # Método novo, do Python 3.
