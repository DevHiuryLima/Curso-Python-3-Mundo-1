# DESAFIO 007: Desenvolva um programa que leia as duas notas de um aluno, calcule e mostre a sua média.

nota1 = float(input('Digite a primeira nota: '))
nota2 = float(input('Digite a segunda nota: '))

soma = nota1 + nota2
media = soma / 2

print('A média entre as notas é {}.'.format(media))
