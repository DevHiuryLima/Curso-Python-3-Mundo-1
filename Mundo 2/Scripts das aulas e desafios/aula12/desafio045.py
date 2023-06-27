# DESAFIO 045: Crie um programa que faça o computador jogar Jokenpô com você.

from random import randint
from time import sleep

itens = ('Pedra', 'Papel', 'Tesoura')

computador = randint(0, 2)
print('''Suas opções:
[ 0 ] Pedra
[ 1 ] Papel
[ 2 ] Tesoura''')

jogador = int(input('Qual é a sua jogada? '))

if jogador >= 0 and jogador <=2:  # Verifica se o jogador escolheu a opção correta. Entre 0 e 2.

    print('JO')
    sleep(1)
    print('KEN')
    sleep(1)
    print('PO!!!')

    print('-=' * 11)
    print('Computador jogou {}'.format(itens[computador]))
    print('Jogador jogou {}'.format(itens[jogador]))
    print('-=' * 12)

    if computador == 0:  # Computador jogou Pedra
        if jogador == 0:
            print('EMPATE.')
        elif jogador == 1:
            print('JOGADOR VENCEU.')
        elif jogador == 2:
            print('COMPUTADOR VENCEU.')
        else:
            print('JOGADA INVÁLIDA!')
    elif computador == 1:  # Computador jogou Palpel
        if jogador == 0:
            print('COMPUTADOR VENCEU.')
        elif jogador == 1:
            print('EMPATE.')
        elif jogador == 2:
            print('JOGADOR VENCEU.')
        else:
            print('JOGADA INVÁLIDA!')
    elif computador == 2:  # Computador jogou Tesoura
        if jogador == 0:
            print('JOGADOR VENCEU.')
        elif jogador == 1:
            print('COMPUTADOR VENCEU.')
        elif jogador == 2:
            print('EMPATE.')
        else:
            print('JOGADA INVÁLIDA!')

else:
    print('Jogada inválida! Digite [1] Pedra, [2] Papel e [3] Tesoura.')
