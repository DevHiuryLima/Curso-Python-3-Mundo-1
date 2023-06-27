# DESAFIO 044: Elabore um programa que calcule o total a ser pago de um preco, considerando o seu preço normal, e
# condição de opcao:

# À vista no dinheiro/cheque: 10% de desconto
# À vista no cartão: 5% de desconto
# Em até 2x no cartão: preço normal
# 3x ou mais no cartão: 20% de juros

print('{:=^40}'.format(' Loja '))
preco = float(input('Preço da compras: R$'))
print('''FORMAS DE PAGAMENTO
[ 1 ] à vista dinheiro/cheque
[ 2 ] à vista cartão
[ 3 ] 2x no cartão
[ 4 ] 3x ou mais no cartão''')
opcao = int(input('Qual é a opção? '))

if opcao == 1:
    total = preco - (preco * 10 / 100)
elif opcao == 2:
    total = preco - (preco * 5 / 100)
elif opcao == 3:
    total = preco
    parcela = total / 2
    print('Sua compra será parcelada em 2x de R${:.2f} SEM Juros.'.format(parcela))
elif opcao == 4:
    total = preco + (preco * 20 / 100)
    quantidadeParcelas = int(input('Quantas parcelas? '))
    valorParcela = total / quantidadeParcelas
    print('Sua compra será parcelada em {}x de R${:.2f} COM JUROS.'.format(quantidadeParcelas, valorParcela))
else:
    total = preco
    print('Opção inválida! Digite um número de 1 a 3.')

print('Sua compra de R${:.2f} vai custar R${:.2f} no final.'.format(preco, total))
