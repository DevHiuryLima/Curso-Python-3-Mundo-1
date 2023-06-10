frase = 'Curso em Vídeo Python'
frase2 = '   Aprenda Python  '

print(frase.replace('Python', 'Android'))  # Vai procurar e substituir a string 'Python' por 'Android'.
print(frase.upper())  # Exibe toda a string em letras maiúsculas. OBS: Mantém os caracteres que já estão maiúsculos.
print(frase.lower())  # Exibe toda a string em letras minúsculas. OBS: Mantém os caracteres que já estão minúsculas.
print(frase.capitalize())  # Exibe a string capitalizada. Deixa apenas o primeiro caractere da frase em letra maiúscula.
print(frase.title())  # Exibe a string estilo título. Deixa o primeiro caractere de cada palavra em letra maiúscula.
print(frase)  # A string original não foi alterada permanentemente por nenhum dos comandos utilizados acima.

print('-' * 22)  # Linha para separar os comandos direcionados a cada string.

print(frase2.strip())  # Remove todos os espaços excedentes da string. No início e no final da string.
print(frase2.rstrip())  # Remove os espaços excedentes apenas do lado direito da string. Por isso a inclusão do "r" no comando.
print(frase2.lstrip())  # Remove os espaços excedentes apenas do lado esquerdo da string. Por isso a inclusão do "l" no comando.
print(frase2)  # Novamente, a string original não foi alterada permanentemente por nenhum dos comandos utilizados acima.
