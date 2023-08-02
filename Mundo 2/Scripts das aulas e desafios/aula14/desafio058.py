# DESAFIO 058: Melhore o jogo do DESAFIO 028 onde o computador vai "pensar" em um número entre 0 e 10. Só que agora o
# jogador vai tentar adivinhar até acertar, mostrando no final quantos palpites foram necessários para vencer.

from random import randint

numeroPensado = randint(0, 10)
acertou = False
tentativas = 0

print('Sou seu computador... Acabei de pensar em número entre 0 e 10.')
print('Será que você consegue adivinhar qual foi? ')

while not acertou:
    palpite = int(input('Qual é o seu palpite? '))

    tentativas += 1

    if palpite == numeroPensado:
        acertou = True
    else:
        if palpite < numeroPensado:
            print('Mais... Tente mais uma vez.')
        if palpite > numeroPensado:
            print('Menos... Tente mais uma vez.')

print('Acertou com {} tentativas. Parabéns!'.format(tentativas))
