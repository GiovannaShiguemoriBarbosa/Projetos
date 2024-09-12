print("Tabuada FOR")

numero = int(input("Entre com o número da tabuada:"))

print("Com a coleção")

for i in (1, 2, 3, 4, 5, 6, 7, 8, 9, 10):
  tabuada = numero * i
  print(f"{numero} x {i} = {tabuada}")

# for i in (1,2,3,4,5,6,7,8,9,10,11,12,13):
#     tabuada = numero * i
#     print(f'{numero} X {i} = {tabuada}')

print("Com o range 10")
for i in range(10):
    tabuada = numero * i
    print(f'{numero} X {i} = {tabuada}')

print("Com o range com primeiro numero determinado")
for i in range(1,10):
    tabuada = numero * i
    print(f'{numero} X {i} = {tabuada}')

print("Com o range com primeiro e ultimo numero determinado")
for i in range(1, 11):
    tabuada = numero * i
    print(f'{numero} X {i} = {tabuada}')

print("Com o range e pulo de 2")
for i in range(1, 11, 2):
    tabuada = numero * i
    print(f'{numero} X {i} = {tabuada}')
