# DESAFIO 007: Desenvolva um programa que leia as duas notas de um aluno, calcule e mostre a sua média.

nota1 = float(input('Digite a primeira nota: '))
nota2 = float(input('Digite a segunda nota: '))

média = (nota1 + nota2) / 2

print('A média entre {:.2f} e {:.2f} é igual a {:.2f}.'.format(nota1, nota2, média))
