# DESAFIO 051:  Desenvolva um programa que leia o primeiro termo e a razão de uma PA. No final, mostre os 10 primeiros
# termos dessa progressão.

termo1 = int(input('Digite o primeiro termo: '))
razao = int(input('Digite a razão: '))
decimoTermo = termo1 + (10 - 1) * razao

for i in range(termo1, decimoTermo + razao, razao):
    print('{}'.format(i), end=' -> ')
print('Acabou.')
