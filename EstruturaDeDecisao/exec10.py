# Faça um Programa que pergunte em que turno você estuda.
# Peça para digitar
# M-matutino ou V-Vespertino ou N- Noturno.
# Imprima a mensagem "Bom Dia!", "Boa Tarde!" ou "Boa Noite!"
# ou "Valor Inválido!", conforme o caso.


print(" == Digite o turno em que você estuda ==")
options = input('''
[M] matutino
[V] vespertino
[N] noturno
''')

if options in 'Mm':
    print("Bom dia!")
if options in 'Vv':
    print("Boa tarde!")
if options in 'Nn':
    print("Boa noite!")
