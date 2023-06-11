# Estrutura Condicional simples de "se" e "senão", o bloco de comando do "se" é executado se a condição for verdadeira
# (True), enquanto o bloco de comandos do "senão" é executado se a condição for falsa (False).

"""
Exemplo de Condicional Simples:
if <CONDIÇÃO>:
    <COMANDOS>

Exemplo de Condicional Composta:
if <CONDIÇÃO>:
    <COMANDOS A>
else:
    <COMANDOS B>
"""
# O espaçamento lateral antes dos comandos dentro de uma Estrutura Condicional é chamado Indentação. Uma indentação pode
# ser criada pressionando a tecla "Tab" (2 teclas abaixo do "Esc").

tempo = int(input('Quantos anos tem seu carro? '))

if tempo <= 3:  # Se a variável "tempo" receber um valor igual ou menor do que 3...
    print('Carro novo!')  # Mostra a menssagem "Carro novo!".
else:  # Senão...
    print('Carro velho!')  # Mostra a menssagem "Carro velho!".

print('--- FIM ---')  # Mostra a menssagem independemente do resultado da condição acima.


