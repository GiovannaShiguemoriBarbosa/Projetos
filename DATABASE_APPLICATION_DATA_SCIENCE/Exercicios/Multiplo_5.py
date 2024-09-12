print("Multiplo 5")

n1 = int(input("Entre com o primeiro número: "))
n2 = int(input("Entre com o segundo número: "))

for i in range(n1, n2 + 1, 1):
  if i % 5 == 0:
    print(i)

#este caso nao funciona pois 
#NAO TEMOS COMO GARANTIR QUE O PRIMEIRO NUMERO INFORMADO SERA MULTIPLO DE 5
# for i in range(n1, n2 + 1, 5):
#     print(i)