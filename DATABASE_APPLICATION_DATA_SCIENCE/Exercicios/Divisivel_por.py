print("Divisivel por...")

numero = int(input("Entre com o numero: "))

#Comandos equivalentes
# for i in range(101):
# for i in range(0,101):
# for i in range(0,101,1):

for i in range(101):
  if i % numero == 0:
    print(i)