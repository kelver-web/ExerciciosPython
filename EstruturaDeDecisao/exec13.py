'''
Faça um Programa que leia um número e exiba o dia correspondente da semana.
(1-Domingo, 2- Segunda, etc.), se digitar outro valor deve aparecer valor
inválido.
'''

days_of_week = [
    'Domingo', 'Segunda-Feira', 'Terça-Feira', 'Quarta-Feira',
    'Quinta-Feira', 'Sexta-Feira', 'Sábado',
]

num = int(input('Digite um número entre [1 e 7] e veja o dia da semana: '))

for i in range(len(days_of_week)):
    if i + 1 == num:
        print(f'Digitou [{num}] [{num}-{days_of_week[i]}]')
