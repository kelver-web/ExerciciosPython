# João Papo-de-Pescador, homem de bem, comprou um microcomputador para controlar o rendimento diário de seu trabalho. Toda vez que ele traz um peso de peixes maior que o estabelecido pelo regulamento de pesca do estado de São Paulo (50 quilos) deve pagar uma multa de R$ 4,00 por quilo excedente. João precisa que você faça um programa que leia a variável peso (peso de peixes) e calcule o excesso. Gravar na variável excesso a quantidade de quilos além do limite e na variável multa o valor da multa que João deverá pagar. Imprima os dados do programa com as mensagens adequadas.


peso = float(input('\nInforme o peso:  '))
excesso = peso - 50
multa = 4.00 * excesso

print(f"Peso: {peso}Kg")
print(f"Multa por excesso: R$4.00")

if peso > 50:
    print(f"Execsso de peso {excesso}Kg")
    print(f'Você ultrapassou o limete de peso, valor da multa é de R${multa:.2f}')
else:
    print(f"Obrigado por usar nosso programa!")