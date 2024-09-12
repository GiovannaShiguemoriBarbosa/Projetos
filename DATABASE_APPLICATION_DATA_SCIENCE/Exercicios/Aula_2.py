print("CNH - desvio condicional simples - sem o else")
idade = int(input("Qual sua idade?"))
if idade >= 18:
  print("Você pode dirigir")
  print("Mas precisa tirar a CNH")

print("Esse comando é sempre excutado")


print("CNH - desvio condicional composto - com o else")
idade = int(input("Qual sua idade?"))
if idade >= 18:
  print("Você pode dirigir")
  print("Mas precisa tirar a CNH")
else:
  print("Você ainda não pode dirigir")
print("Esse comando é sempre excutado")



print("Abastecimento")
bloco = int(input("Qual bloco você mora?"))
if (bloco == 1) or (bloco == 3):
  print("Você é abastecido pela caixa B")
else: # isso está errado  (bloco == 2) or (bloco == 4): o comando else NAO ACEITA NOVA COMPARACAO
  print("Você é abastecido pela caixa A")


print("Abastecimento")
bloco = int(input("Qual bloco você mora?"))
if (bloco % 2 == 0):
  print("Você é abastecido pela caixa A")
else: 
  print("Você é abastecido pela caixa B")


print("Sindico")
bloco = int(input("Qual bloco vc mora? "))
if bloco > 10 :
  print("Sindico Sr Hamilton")
else:
  print("Sindico Sr Jose")


print("Sindico")
bloco = int(input("Qual bloco vc mora? "))
if bloco >= 1 and bloco <= 10:
  print("Sindico Sr Jose")
if bloco > 10 and bloco <= 20:
  print("Sindico Sr Hamilton")

print("Compras")
preco = float(input("Qual o preco da mercadoria? "))
carteira = float(input("Quantos reais eu tenho na carteira? "))
if carteira >= preco:
  print("Posso comprar pois custa", preco, "e eu tenho", carteira)
else:
  falta = preco - carteira
  print("Preciso economizar pois falta", falta)