# DESAFIO 059: Crie um programa que leia dois valores e mostre um menu como o abaixo na tela:

# [ 1 ] Somar
# [ 2 ] Multiplicar
# [ 3 ] Maior
# [ 4 ] Novos Números
# [ 5 ] Sair do Programa

# Seu programa deverá realizar a operação solicitada em cada caso.

from time import sleep

numero1 = int(input('Digite o primeiro valor: '))
numero2 = int(input('Digite o segundo valor: '))
opcao = 0

while opcao != 5:
    print("""    [ 1 ] Somar 
    [ 2 ] Multiplicar
    [ 3 ] Maior
    [ 4 ] Novos números
    [ 5 ] Sair do programa""")

    opcao = int(input('>>>>> Qual é a sua opção? '))

    if opcao == 1:
        soma = numero1 + numero2
        print('A soma entre {} e {} é {}'.format(numero1, numero2, soma))
    elif opcao == 2:
        produto = numero1 * numero2
        print('O resultado de {} x {} é {}'.format(numero1, numero2, produto))
    elif opcao == 3:
        if numero1 > numero2:
            maior = numero1
        else:
            maior = numero2
        print('Entre {} e {} o maior valor é {}'.format(numero1, numero2, maior))
    elif opcao == 4:
        print('Informe os números novamente.')
        numero1 = int(input('Digite o primeiro valor: '))
        numero2 = int(input('Digite o segundo valor: '))
    elif opcao == 5:
        print('Finalizando...')
    else:
        print('Opção inválida! Tente Novamente.')
    print('=-=' * 10)
    sleep(2)
print('Fim do programa! Volte sempre!')
