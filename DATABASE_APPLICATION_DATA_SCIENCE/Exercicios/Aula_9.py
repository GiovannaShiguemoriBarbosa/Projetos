# tupla
# coleções do tipo imutável
# uma vez criada não podemos alterar, ou seja
# Não podemos acrecentar ou retirar elementos, são indexáveis, ou seja
# cada elemento tem seu lugar
# desse jeito elas permitem repetidos e são usadas no comando for
# lembrando que toda coleção é um elemento iterável, eu posso percorrer eles

print("TUPLAS")
minhaTupla = ("sono", "comida", "sol", "sono")
print(minhaTupla)
print(type(minhaTupla))

# 0       1        2       3
# -4      -3       -2     -1
("sono", "comida", "sol", "sono")
print("primeiro elemento:", minhaTupla[0])
# essa chave significa index
print("Ultimo elemento:", minhaTupla[-1])

#slicing
# 0       1        2       3
("sono", "comida", "sol", "sono")
#[de:ate-1]
#[1:3]
pequenaTupla = minhaTupla[1:3]
print(pequenaTupla)
pequenaTupla = minhaTupla[1:2 + 1]

print("Tupla de um elemento só")
tuplaUnica = ('tuplaUnicaFalsiane')
print(type(tuplaUnicaFalsiane))
#no fim de uma string

tuplaUnicaVerdadeira = ("Unica", )
print(tuplaUnicaVerdadeira)
print(type(tuplaUnicaVerdadeira))

#será que eu consigo ordenar uma tupla? não pois ninguém vai mexer
#nao consigo pq ela é imutável
#minhaTupla.sort()
#posso usar sorted em qual elemento do python, ele automaticamente vira lista
novaColecao = sorted(minhaTupla)
print("novaColecao")
print(type(novaColecao))
print("\n")
print(minhaTupla)
# transformando em tupla
novaColecao = tuple(novaColecao)
print("novaColecao")
print(type(novaColecao))

print(sorted(novaColecao))

#inicializador
minhaTuplaVazia = ()
print(minhaTuplaVazia)
#poder vc pode fazer, mas não serve para nada

#operadores aritméticos com tupla
#consigo juntar duas tuplas com operadores aritméticos
meusBrinquedos = ('patins', 'skate', 'bola')
minhasNecessidades = minhaTupla + meusBrinquedos
print(meusBrinquedos)
print(minhasNecessidades)

muitosBrinquedos = meusBrinquedos * 5
print(muitosBrinquedos)

#consigo colocar mais elementos na tupla?
#nãoooo
#dando meus pulos para acrescentar
minhaTupla = list(minhaTupla)
#representação de como eu passo um parametro dentro de uma lista
minhaTupla.append('praia')
print(minhaTupla)
print(type(minhaTupla))

#tupla é indexado
#localizar um elemento

if "sol" in minhaTupla:
  print('tem sol')
  print('o sol mora na casa:', minhaTupla.index('sol'))

#não há como remover itens em tupla, se vc quiser v c tem que converter para lista
#toda manipulação da tupla, seja para adicionar ume elemento
#(append -> adiciona o elemento no final, insert-> que adiciona )
#remover um elemento(pop()-> sem indiceremove no final, com indice remove do localizado, del)
#ordenar (sort ou sorted)
# transforme em lista e reconverto para tupla depois da alteração

print('Quantidade de elementos', len(minhaTupla))

del minhaTupla
print(minhaTupla)

#Slicing
#[DE:ATE:PASSOS]

txt = 'nao sei o que é tremoço'
palavra = txt[0:3]
print(palavra)

palavras = txt[4:]
print(palavras)

palavras = txt[::2]
print(palavras)

print(len(txt))
palavras = txt[-10::]
print(palavras)

palavras = txt[::-1]
print(palavras)

#equivalentes
if len(entradas) > 3:
  entradasprima = entradas[len(entradas) - 3:len(entradas)]
  print(entradas)

  # equivalentes
  entradasprima = entradas[-3:]
  print(entradasprima)
