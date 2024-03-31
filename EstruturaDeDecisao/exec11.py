'''
As Organizações Tabajara resolveram dar um aumento de salário aos seus
colaboradores e lhe contraram para desenvolver o programa que calculará
os reajustes.

Faça um programa que recebe o salário de um colaborador e o reajuste segundo
o seguinte critério, baseado no salário atual:

salários até R$ 280,00 (incluindo) : aumento de 20%
salários entre R$ 280,00 e R$ 700,00 : aumento de 15%
salários entre R$ 700,00 e R$ 1500,00 : aumento de 10%
salários de R$ 1500,00 em diante : aumento de 5% Após o aumento ser realizado,
informe na tela:

o salário antes do reajuste;
o percentual de aumento aplicado;
o valor do aumento;
o novo salário, após o aumento.
'''


salario = float(input("Informe o valor do salário:  "))

reajuste = 0
novo_valor = 0

if salario <= 280:
    valor_aumento = salario * 0.20
    novo_valor = salario + valor_aumento
    percentual = 20

if salario > 280 and salario <= 700:
    valor_aumento = salario * 0.15
    novo_valor = salario + valor_aumento
    percentual = 15

if salario > 700 and salario <= 1500:
    valor_aumento = salario * 0.10
    novo_valor = salario + valor_aumento
    percentual = 10

if salario > 1500:
    valor_aumento = salario * 0.05
    novo_valor = salario + valor_aumento
    percentual = 5

print(f'''
O salário antes do valor_aumento: R${salario:.2f}
Percentual de aumento: {percentual}%
Valor do aumento: R${valor_aumento:.2f}
Salário após o aumento: R${novo_valor:.2f}
''')
