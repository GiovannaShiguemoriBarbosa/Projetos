print("Contagem 600 \n")
for i in range(1,601):
    if i % 2 == 0:
        print(i)
#for i in range(601): #incorreto pois comeca no zero

# este tb funciona
# for i in range(2,601,2):
#     print(i)
print("Até logo")

print("Inversao de Numero")
numero = input("Entre com um numero de 4 digitos:")
# #Alcides way of live
# print(numero)
# print(type(numero))
# numero_invertido = numero[::-1]
# print(type(numero_invertido))
# print(numero_invertido)

# dig4   dig3   dig2   dig1
# milhar centena dezena unidade
# 3      7       5       8

# resultado esperado
# unidade dezena centena milhar
# 8        5      7       3

# se eu dividir um numero por 10 (divisao inteira) o resto vai ser sempre a UNIDADE
# numero = 3758
#
# print("Numero original",numero)
# dig1 = numero % 10
# print("Digito1", dig1)
# numero = numero // 10
# print("Novo Numero:", numero)
#
# dig2 = numero % 10
# print("Digito2", dig2)
# numero = numero// 10
# print("Novo Numero 1:", numero)
#
# dig3 = numero % 10
# print("Digito3", dig3)
# numero = numero // 10
# print("Novo Numero 2:", numero)
#
# numero_novo_final = int(str(dig1) + str(dig2) + str(dig3) + str(numero))
# print(numero_novo_final)

# transformando em repeticao
#numero = 3758
numero_invertido = ""
while(numero > 0):
    dig = numero % 10
    numero_invertido = numero_invertido + str(dig)
    print(numero_invertido)
    numero = numero // 10

print("Final", numero_invertido)


print("Estados")
estado = input("Entre com a sigla estado").upper()
if estado == 'SP':
    print('Paulista')
elif estado == 'RJ':
    print('Carioca')
elif estado == 'BA':
    print('Baiano')
else:
    print("Outros Estados")


titulo = "a terça parte".capitalize()
print(f'{titulo:^30}')
# for i in range(3):
#     numero = int(input("Entre com um numero"))
#     total = round(numero / 3, 2)
#     print(f'A terça parte de {numero} é {total}')

# for i in range(3):
#     numero = int(input("Entre com um numero"))
#     print(f'A terça parte de {numero} é {round(numero / 3, 2)}')

# for i in range(3):
#     numero = int(input("Entre com um numero"))
#     total = numero / 3
#     print(f'A terça parte de {numero} é {total:.2f}')
#
for i in range(3):
    print(f'A terça parte do numero é {int(input("Entre com um numero"))/3}')

titulo = "a terça parte".capitalize()
print(f'{titulo:^30}')
# for i in range(3):
#     numero = int(input("Entre com um numero"))
#     total = round(numero / 3, 2)
#     print(f'A terça parte de {numero} é {total}')

# for i in range(3):
#     numero = int(input("Entre com um numero"))
#     print(f'A terça parte de {numero} é {round(numero / 3, 2)}')

# for i in range(3):
#     numero = int(input("Entre com um numero"))
#     total = numero / 3
#     print(f'A terça parte de {numero} é {total:.2f}')
#
for i in range(3):
    print(f'A terça parte do numero é {int(input("Entre com um numero"))/3}')


print("Temporizador")
minutos = int(input("Entre com os minutos"))

print(f'{minutos:02d}:00')

while minutos > 0:
    minutos = minutos - 1
    segundos = 60
    while segundos > 0:
        segundos = segundos -1
        print(f'{minutos:02d}:{segundos:02d}')