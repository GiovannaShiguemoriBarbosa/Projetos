#Media
# nota1 = 8.68
# nota2 = 9.1
# media = (nota1 + nota2) / 2
# print("A media é", media, "-", type(media))
# print("A media é", int(media), "-" ,type(int(media)))
# print("A media é", round(media), "-", type(media))
# print("A media é", round(media, 1), "-", type(media))

nota1 = float(input("Entre com a primeira nota "))
print(type(nota1))
nota2 = float(input("Entre com a segunda nota "))
print(type(nota2))
media = (nota1 + nota2) / 2
print("A media é", media)


# #Taximetro
# custoKM = 4.16
# KMRodado = 8
# ValorTotal = custoKM * KMRodado
# print(type(ValorTotal))
#
# print("O valor total a ser pago é", ValorTotal)
# print("O valor total a ser pago é", str(ValorTotal))
# print("O valor total a ser pago é " + str(ValorTotal))
# print(len("O valor total a ser pago é " + str(ValorTotal)))
# #print(len(ValorTotal))


#Taximetro
custoKM = 4.16
KMRodado = float(input("Entre com a quantidade de KM rodados "))
ValorTotal = custoKM * KMRodado
print(type(ValorTotal))

print("O valor total a ser pago é", ValorTotal)
