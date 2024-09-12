# convidados = []
# quantidade = int(input("Quantas pessoas estarão na reunião? "))
#
# if quantidade <= 15:
#     print("A reunião pode acontecer no seu apartamento.")
#     for i in range(1, quantidade + 1):
#
#         convidados.append(input(f"Qual o nome do convidado {i}: ").lower())
#         convidados.append(int(input(f"Qual o rg do convidado {i}: ")))
#
#     if "joão" in convidados:
#         print("Seu melhor amigo joão está na lista de convidados!")
#     else:
#         print("Ops, parece que seu melhor amigo joão não foi convidado.")
#
# else:
#     print("Infelizmente, o síndico proibiu reuniões com mais de 15 pessoas no apartamento.")
#

convidados = []
i = 1
resp = 's'
while resp.lower() in ('s', 'sim', 'y', 'yes'):
    convidados.append(input(f"Qual o nome do convidado {i}: ").lower())
    convidados.append(int(input(f"Qual o rg do convidado {i}: ")))
    resp = input('Tem mais um convidado?')
    i += 1
if "joão" in convidados:
    print("Seu melhor amigo joão está na lista de convidados!")
else:
    print("Ops, parece que seu melhor amigo joão não foi convidado.")