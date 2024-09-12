print("Estacionamento")
custo_hora = 5.00
teto = 35
hora = float(input("Quantas hrs vc ficou estacionado?"))
total = hora * custo_hora
if total >= teto:
    print("Voce deve pagar", teto)
else:
    print("Voce deve pagar", total)

print("Estacionamento")
custo_hora = 5.00
teto = 35
hora = float(input("Quantas hrs vc ficou estacionado?"))
if hora > 0:
    total = hora * custo_hora
    if total >= teto:
        print("Voce deve pagar", teto)
    else:
        print("Voce deve pagar", total)
else:
    print("Hora invalida")

print("Adivinhacao")
cor_esperada = 'AmarEla'
cor = input("Qual cor voce pensou? ").lower()
print(cor)
if cor == cor_esperada.lower():
    print("Adivinhou")
else:
    print("Quem pena, pensei em", cor_esperada)


print("Nota")
nota = float(input("Qual sua nota? "))
if nota >= 0 and nota <= 10:
    if nota >= 6:
        print("Aprovado")
    else:
        if nota >= 4:
            print("Exame")
        else:
            print("Reprovado")
else:
    print("Nota invalida")