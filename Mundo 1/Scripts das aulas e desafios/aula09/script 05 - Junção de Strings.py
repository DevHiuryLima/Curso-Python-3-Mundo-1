frase = 'Curso em Vídeo Python'
frase_separada = frase.split()

frase_junta_hifen = '-'.join(frase_separada)  # Junta as palavras separadas na lista com o caractere "-" como divisor.
print(frase_junta_hifen)   # Exibe a string junta novamente, desta vez com "-" no lugar dos espaços.

frase_junta_espaco = ' '.join(frase_separada) # Junta as palavras separadas na lista usando um espaço como divisor.
print(frase_junta_espaco)  # Exibe a string junta novamente, com o espaço sendo o divisor, como na original.
