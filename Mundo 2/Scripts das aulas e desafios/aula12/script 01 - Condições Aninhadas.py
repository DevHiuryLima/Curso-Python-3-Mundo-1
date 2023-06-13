# Exemplo de Estrutura Condicional Aninhada:

"""
if <CONDIÇÃO 1>:
    <COMANDOS A>
elif <CONDIÇÃO 2>:
    <COMANDOS B>
elif <CONDIÇÃO 3>:
    <COMANDOS C>
else:
    <COMANDOS D>
"""
# OBS: É possível utilizar quantos "elif" forem necessários.

nome = str(input('Qual é o seu nome? '))

if nome.lower() == 'hiury':
    print('Que nome bonito!')
elif nome.lower() == 'pedro' or nome.lower() == 'maria' or nome.lower() == 'paulo':
    print('Seu nome é bem popular no Brasil!')
elif nome.lower() in 'ana cláudia jéssica juliana':
    print('Belo nome feminino!')
else:
    print('Seu nome é bem normal!')
print('Tenha um bom dia, {}!'.format(nome))
