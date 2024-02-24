# Faça um Programa que pergunte quanto você ganha por hora e o número de horas trabalhadas no mês. Calcule e mostre o total do seu salário no referido mês.

valor_hora = float(input('Informe o valor ganho por hora:  '))
num_horas_trabalhadas = float(input('Informe o número de horas trabalhadas:  '))
total_salario = valor_hora * num_horas_trabalhadas

print(f"Total salário: R${total_salario:.2f}")