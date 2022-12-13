n = input('Digite algo: ')


print(n.isnumeric())  # Verifica se o que foi digitado é ou pode se tornar um valor numérico.
# Retorna 'True' se sim e 'False' se não.

print(n.isalpha())  # Verifica se o que foi digitado é alfabetico, ou seja se é letra ou contém apenas letras.
# Retorna 'True' se sim e 'False' se não.

print(n.isalnum())  # Verifica se o que foi é alfanúmerico (alfabetico com número).
# Retorna 'True' se sim e 'False' se não.

print(n.isupper())  # Verifica se o que foi digitado contém apenas letras maiúsculas.
# Retorna 'True' se sim e 'False' se não.

# Existem ainda outros métodos "is", como "islower()", "isspace()" etc.
