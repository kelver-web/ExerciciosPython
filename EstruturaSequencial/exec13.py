# Tendo como dado de entrada a altura (h) de uma pessoa, construa um algoritmo que calcule seu peso ideal, utilizando as seguintes fórmulas:

# Para homens: (72.7*h) - 58
# Para mulheres: (62.1*h) - 44.7

altura = float(input("Informe a sua altura:  "))

homens = (72.7 * altura) - 58
mulheres = (62.1 * altura) - 44.7

print(f"O peso ideal para os Homens é   -> {homens:.2f}Kg")
print(f"O peso ideal para as mulheres é -> {mulheres:.2f}Kg")
