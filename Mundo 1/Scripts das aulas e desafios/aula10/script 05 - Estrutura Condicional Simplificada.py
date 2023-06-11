nota1 = float(input('Digite a primeira nota: '))
nota2 = float(input('Digite a segunda nota: '))

media = (nota1 + nota2) / 2

print('A sua média foi {:.1f}!'.format(media))
# Terceira Condicional - Simplificada
print('MEUS PARABÉNS!!' if media >= 6.0 else 'ESTUDE MAIS, É SÉRIO!')
