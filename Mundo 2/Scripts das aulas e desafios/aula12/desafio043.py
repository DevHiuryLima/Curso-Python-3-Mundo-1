# DESAFIO 043: Desenvolva uma lógica que leia o peso e a altura de uma pessoa, calcule seu IMC e mostre seu status, de
# acordo com a tabela abaixo:

# Abaixo de 18.5: Abaixo do Peso
# Entre 18.5 e 25: Peso Ideal
# 25 até 30: Sobrepeso
# 30 até 40: Obesidade
# Acima de 40: Obesidade Mórbida

peso = float(input('Digite o seu peso (Kg): '))
altura = float(input('Digite o seu peso (m): '))

imc = peso / (altura ** 2)

print('Seu IMC é de {:.1f}'.format(imc))
if imc < 18.5:
    print('Você está ABAIXO do peso!')
elif 18.5 <= imc < 25:
    print('Você está no peso NORMAL. PARABÉNS!')
elif 25 <= imc < 30:
    print('Você está com SOBREPESO!')
elif 30 <= imc < 40:
    print('Você está com OBESIDADE!')
elif imc >= 40:
    print('Você está com OBESIDADE MÓRBIDA. CUIDADO!')
