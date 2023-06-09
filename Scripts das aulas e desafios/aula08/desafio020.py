# DESAFIO 020: O mesmo professor do desafio anterior quer sortear a ordem de apresentação de trabalhos dos alunos. Faça
# um programa que leia o nome dos quatro alunos e mostre a ordem sorteada.

from random import shuffle

nome1 = str(input('Primeiro aluno: '))
nome2 = str(input('Segundo aluno: '))
nome3 = str(input('Terceiro aluno: '))
nome4 = str(input('Quatro aluno: '))
lista = [nome1, nome2, nome3, nome4]

shuffle(lista)
print('A ordem de apresentação será: ')
print(lista)

