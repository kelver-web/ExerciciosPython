# Faça um programa que pergunte o preço de três produtos e informe qual
# produto você deve comprar, sabendo que a decisão é sempre pelo mais barato.


preco_produto1 = float(input('Informe o valor do 1º produto: '))
preco_produto2 = float(input('Informe o valor do 2º produto: '))
preco_produto3 = float(input('Informe o valor do 3º produto: '))

if preco_produto1 < preco_produto2 and preco_produto1 < preco_produto3:
    print(f'Você vai comprar o 1º produto, que custa R${preco_produto1:.2f}')
if preco_produto2 < preco_produto1 and preco_produto2 < preco_produto3:
    print(f'Você vai comprar o 2º produto, que custa R${preco_produto2:.2f}')
else:
    print(f'Você vai comprar o 3º produto, que custa R${preco_produto3:.2f}')
