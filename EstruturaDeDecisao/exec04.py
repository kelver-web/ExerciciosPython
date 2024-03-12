# Faça um Programa que verifique se uma letra digitada é vogal ou consoante.

letra = input("Digite uma letra:  ")


if letra in ('a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U'):
    print(f'A letra [{letra}] é vogal')
else:
    print(f'A letra [{letra}] é consoante')
