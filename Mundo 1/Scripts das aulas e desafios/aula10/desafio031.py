# DESAFIO 031: Desenvolva um programa que pergunte a distância de uma viagem em km. Calcule o preço da preco,
# cobrando R$ 0,50 por km para viagens de até 200 km e R$ 0,45 para viagens mais longas.

distancia = float(input('Qual a distância da sua viagem? '))

if distancia <= 200:
    preco = distancia * 0.50
else:
    preco = distancia * 0.45
print('O preço da sua passagem será de R${:.2f} para uma viagem de {}Km.'.format(preco, distancia))
