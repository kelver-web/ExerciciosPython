# Faça um Programa que peça a temperatura em graus Fahrenheit, transforme e mostre a temperatura em graus Celsius.
# C = 5 * ((F-32) / 9).


temp_fahrenheit = float(input('Informe a temperatura em graus Fahrenheit:  '))
c = 5 * ((temp_fahrenheit - 32) / 9)

print(f'{temp_fahrenheit}ºF é igual a {c:.2f}ºC')