frase = 'Curso em Vídeo Python'

print(len(frase)) # Exibe a quantidade de caracteres de uma string (nesse caso, 21).
print(frase.count('o')) # Exibe a quantidade de vezes que o caractere "o" minúsculo (entre parênteses) aparece na string
# (no caso, 3).
print(frase.count('o', 0, 13)) # O mesmo caso acima, porém aqui foi incluído um fatiamento do índice [0] ao [13]-1,
# exibindo "1".
print(frase.count('o', 0, 14))  # O mesmo caso acima, porém aqui o índice final ficou sendo [14]-1, exibindo "2".
print(frase.find('deo'))  # Exibe o índice inicial (11, no caso) do texto "deo" (entre parênteses).
print(frase.find('Android'))  # Quando se procura na string algo que não está presente, o valor exibido é "-1".
print('Curso' in frase)  # Verifica se o que está entre aspas está presente na string, e se sim, exibe "True".
