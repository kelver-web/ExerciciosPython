# Faça um Programa que peça 2 números inteiros e um número real. Calcule e mostre:

# o produto do dobro do primeiro com metade do segundo .
# a soma do triplo do primeiro com o terceiro.
# o terceiro elevado ao cubo.


num1 = int(input('Informe o 1º numero:  '))
num2 = int(input('Informe o 2º numero:  '))
num3 = float(input('Informe o 3º numero: '))

res1 = (2 * num1) * (num1 / 2)
res2 = (num1 * 3) + num3
res3 = num3 ** 3

print(f"O produto do dobro do primeiro com metade do segundo é = {res1}")
print(f"A soma do triplo do primeiro com o terceiro é = {res2}")
print(f"O terceiro elevado ao cubo é = {res3}")
