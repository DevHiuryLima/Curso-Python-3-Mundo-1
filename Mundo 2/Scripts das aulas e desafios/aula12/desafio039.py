# DESAFIO 039: Faça um programa que leia o ano de nascimento de um jovem e informe, de acordo com sua idade, se ele
# ainda vai se alistar ao serviço militar, se é a hora de se alistar, ou se já passou do tempo do alistamento. Seu
# programa também deverá mostrar o tempo que falta ou que passou do prazo.

from datetime import date

anoAtual = date.today().year
anoNascimento = int(input('Ano de Nascimento: '))
idade = anoAtual - anoNascimento
print('Quem nasceu em {} tem  {} anos em {}.'.format(anoNascimento, idade, anoAtual))

if idade == 18:
    print('Você tem que se alistar IMEDIATAMENTE!')
elif idade < 18:
    print('Ainda faltam {} anos para o alistamento.'.format(18 - idade))
    print('seu alistamento será em {}.'.format(anoAtual + (18 - idade)))
elif idade > 18:
    print('Você já deveria ter se alistado há {} anos.'.format(idade - 18))
    print('Seu alistamento foi em {}.'.format(anoAtual - (idade - 18)))
