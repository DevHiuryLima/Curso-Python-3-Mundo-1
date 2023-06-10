frase = 'Curso em Vídeo Python'

frase_dividida = frase.split()  # Atribui à variável "frase_dividida" a lista de palavras contidas em "frase".

# ÍNDICES REFEITOS
# [C] [u] [r] [s] [o]   [e] [m]   [V] [í] [d] [e] [o]   [P] [y] [t] [h] [o] [n]
# [0] [1] [2] [3] [4]   [0] [1]   [0] [1] [2] [3] [4]   [0] [1] [2] [3] [4] [5]
# [        0        ]   [  1  ]   [        2        ]   [          3          ]

print(frase_dividida[0])  # Exibe o primeiro item da lista criada acima, que consequentemente é a palavra 'curso'.
print(frase_dividida[2][3])  # Exibe a terceira letra no segundo item da lista. Ou seja, a palvra 'Vídeo' letra 'e'.
print(frase_dividida[3][0])  # Exibe a primeira letra da quarta palavra na lista.
print(frase_dividida[3][0:3])  # Exibe da primeira até a terceira letra da quarta palavra na lista.
print(frase_dividida[0][::2])  # Exibe da primeira até a última letra da primeira palavra na lista, pulando de 2 em 2.
