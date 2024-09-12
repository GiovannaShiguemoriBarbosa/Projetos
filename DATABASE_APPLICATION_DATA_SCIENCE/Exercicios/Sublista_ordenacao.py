convidados = []
quantidade = int(input("Quantas pessoas estarão na reunião? "))
convidado = []
if quantidade <= 15:
    print("A reunião pode acontecer no seu apartamento.")
    for i in range(quantidade):
        # for i in range(1,quantidade + 1):
        #nome = input("Qual o nome do convidado {}: ".format(i + 1)).lower()
        # nome = input(f"Qual o nome do convidado {i + 1}: ")
        convidado.append(input("Qual o nome do convidado {}: ".format(i + 1)).lower())
        convidado.append(int(input("Qual o rg do convidado {}: ".format(i + 1))))
        convidados.append(convidado)
        convidado = []
    if "joão" in convidados:
        print("Seu melhor amigo joão está na lista de convidados!")
    else:
        print("Ops, parece que seu melhor amigo joão não foi convidado.")
    print("lista original", convidados)
    #convidados.sort()
    print("lista ordenada", sorted(convidados))
else:
    print("Infelizmente, o síndico proibiu reuniões com mais de 15 pessoas no apartamento.")