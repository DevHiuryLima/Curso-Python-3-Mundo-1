# DESAFIO 062: Melhore o DESAFIO 061, perguntando para o usuário se ele quer mostrar mais alguns termos. O programa
# encerra quando ele disser que quer mostrar 0 termos.

print('Gerador de PA')
print('-=' * 10)
primeiro = int(input('Primeiro termo: '))
razao = int(input('Razão: '))
termo = primeiro
contador = 1
total = 0
mais = 10

while mais != 0:
    total += mais
    while contador <= total:
        print('{} → '.format(termo), end='')
        termo += razao
        contador += 1
    print('PAUSA.')
    mais = int(input('Quantos termos você quer mostrar a mais? '))
print('Prograssão finalizada com {} termos mostrados.'.format(total))
