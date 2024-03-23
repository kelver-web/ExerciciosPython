# Faça um Programa que leia três números e mostre o maior e o menor deles.


num1 = float(input('Digite o 1º número:  '))
num2 = float(input('Digite o 2º número:  '))
num3 = float(input('Digite o 3º número:  '))


if num1 > num2 and num1 > num3:
    print(f'O maior número é {num1:.0f}')
if num2 > num1 and num2 > num3:
    print(f'O maior número é {num2:.0f}')
if num3 > num1 and num3 > num2:
    print(f'O maior número é {num3:.0f}')
if num1 < num2 and num1 < num3:
    print(f'O menor número é {num1:.0f}')
if num2 < num1 and num2 < num3:
    print(f'O menor número é {num2:.0f}')
if num3 < num1 and num3 < num2:
    print(f'O menor número é {num3:.0f}')
if num1 == num2 and num1 == num3 and num2 == num1 and num2 == num3 and num3 == num1 and num3 == num2:
    print('Os números são iguais')
