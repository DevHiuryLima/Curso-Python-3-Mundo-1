"""
Sempre que for necessário representar uma cor no terminal.

Devo começar com o código \033[m
Entre o '[' e o 'm' devo colocar o código da cor. Porém também pode ser colocado até 3 tipos de códigos.


Exemplo:
\033[<ESTILO_DO_TEXTO>;<COR_DO_TEXTO>;<COR_DO_FUNDO>m


Exemplo praticando:
\033[0;33;44m

Lista de Estilos do Texto:
0 = None (Sem Estilo)
1 = Bold (Em Negrito)
4 = Underline (Sublinhado)
7 = Negative (Cores Invertidas)

Lista de Cores do Texto:
30 = Preto
31 = Vermelho
32 = Verde
33 = Amarelo
34 = Azul
35 = Magenta
36 = Ciano
37 = Cinza
97 = Branca
# OBS: Esses são os novos códigos para as cores até o momento 12/06/2023


Lista de Cores do Fundo:
40 = Branco
41 = Vermelho
42 = Verde
43 = Amarelo
44 = Azul
45 = Magenta
46 = Ciano
47 = Cinza
"""

print('\033[0;97;41mTexto em branco com fundo vermelho.')
print('\033[4;31;43mTexto sublinhado em amarelo com fundo vermelho.')
print('\033[1;35;43mTexto negrito em roxo com fundo amarelo.')
print('\033[;97;42mTexto em branco com fundo verde.')  # OBS: Não foi passado nenhum estilo de texto, por isso só tem dois códigos.
print('\033[mTexto em cinza com fundo preto.')  # OBS: Esse é o padrão do terminal.
print('\033[7;97mTexto em preto com fundo branco.')

print('\033[m\n')  # Pula linha deixando as cores padrão do terminal.

print('\033[31mTexto em vermelho.')
print('\033[31;43mTexto em vermelho e fundo amarelo.')
print('\033[1;31;43mTexto negrito em vermelho e fundo amarelo.')
print('\033[1;31;43mTexto negrito em vermelho e fundo amarelo apenas até o final do texto.\033[m') # Coloco o '\033[m' para a cor de fundo não ir até o final.
print('\033[4;97;45mTexto em branco sublinhado e fundo roxo apenas até o final do texto.\033[m')
print('\033[97mTexto em branco')
print('\033[37mTexto em cinza')  # No padrão do terminal, por isso não muda nada

print('\033[7;97mTexto em preto e fundo branco.')
print('\033[0;33;44mTexto em amarelo e fundo azul.')  # OBS: O zero não passa nenhum estilo de texto.
print('\033[7;33;44mTexto em azul e fundo amarelo.\033[m')  # Invertendo o que está acima.
# print('\033[1;7;30mTexto preto em negrito e fundo branco apenas até o final do texto.')

print('\033[m\n')  # Pula linha deixando as cores padrão do terminal.

valor1 = 3
valor2 = 5
print('Os valores são \033[0;32m{}\033[m em verde e \033[0;31m{}\033[m em vermelho.'.format(valor1, valor2))

print('\033[m\n')  # Pula linha deixando as cores padrão do terminal.

nome = 'Hiury'
print('Olá! Muito prazer em te conhecer, {}{}{}!'.format('\033[4;34m', nome, '\033[m'))

print('\033[m\n')  # Pula linha deixando as cores padrão do terminal.

cores = {
    'limpa': '\033[m',
    'azul': '033[34m',
    'amarelo': '\033[33m',
    'pretoebranco': '\033[7;97m' # Coloco a cor do texto branca o fundo padrão do terminal (preto), porém uso o 7 para inverter.
}

print('Olá! Muito prazer em te conhecer, {}{}{}!'.format(cores['pretoebranco'], nome, cores['limpa']))
