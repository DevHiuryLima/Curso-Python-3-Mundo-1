# DESAFIO 022: Crie um programa que leia o nome completo de uma pessoa e mostre:

# O nome com todas as letras maiúsculas e minúsculas.
# Quantas letras ao todo (sem considerar espaços).
# Quantas letras tem o primeiro nome.

nome = input('Digite seu nome completo: ')

print('Seu nome em letras maiúsculas é: {}'.format(nome.upper()))
print('Seu nome em letras minúsculas é: {}'.format(nome.lower()))
print('seu nome tem ao todo {} letras.'.format( len(nome) - nome.count(' ')) )  # Pega o tamanho da string nome
# (atráves do len(nome )), menos a quantidade de espaços que tem no nome (feito com nome.count(' ')).

# print('Seu primeiro nome tem {} letras.'.format(nome.find(' ')))
primeiro_nome = nome.split()[0]  # Separa dentro de uma lista os nomes inteiro, porém estou buscando somente o índice 0.
print('Seu primeiro nome é {} e ele tem {} letras.'.format(primeiro_nome, len(primeiro_nome)))
