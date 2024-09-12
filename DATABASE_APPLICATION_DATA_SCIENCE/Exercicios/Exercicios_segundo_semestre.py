#3) Escreva um programa em Python que solicite 5
# numeros e armazene em variáveis diferentes
# (uma variável para cada número) e imprima em ordem crescente
# a = int(input('Entre com 1 numero')) # 10
# b = int(input('Entre com 1 numero')) # 9
# c = int(input('Entre com 1 numero')) # 8
a = 10
b = 9
c = 8
#saida esperada 8, 9, 10
print(a, b, c)
# é uma abordagem, mas fica mais dificil com muitos numeros
# if a > b:
#     if b > c:
#         print(c)
#     else:
#         print(b)
# o melhor é trocar os numeros nas variaveis
# 10 > 9
if a > b:
    #se isso acontecer, o a vai tomar o lugar de b e vice versa
    aux = a # 10
    a = b # 9
    print ('parcial ab', a, b)
    b = aux # 10
#  9 > 8
if a > c:
    #se isso acontecer, o a vai tomar o lugar de b e vice versa
    aux = a # 9
    a = c # 8
    print ('parcial ac', a, c)
    c = aux # 9
#  10 > 9
if b > c:
    #se isso acontecer, o a vai tomar o lugar de b e vice versa
    aux = b # 10
    b = c # 9
    print ('parcial bc', b, c)
    c = aux # 10
print(a, b, c)