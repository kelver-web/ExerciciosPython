# Faça um Programa que leia três números e mostre-os em ordem decrescente.

list_nums = []

for i in range(3):
    num = int(input(f"Informe o {i + 1}º número:  "))
    list_nums.append(num)

print(
    f"""
    Números da lista em ordem decrescente
    {sorted(list_nums, reverse=True)}""")
