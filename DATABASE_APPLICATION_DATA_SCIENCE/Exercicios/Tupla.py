#Tupla
# coleções do tipo IMUTAVEL
# Uma vez criada, não podemos alterar, ou seja
# Não podemos acrescentar ou retirar elementos
# Indexáveis (ou seja, cada elemento tem seu lugar)
# Permitem repetidos
# São muito usadas no comando for
# Lembrando que toda coleção é um elemento ITERAVEL
#
print('TUPLAS')
minhaTupla = ('sono', 'comida', 'sol', 'sono')
print(minhaTupla)
print(type(minhaTupla))
# 0          1       2       3
# -4        -3      -2      -1
#('sono', 'comida', 'sol', 'sono')
print('Primeiro elemento:', minhaTupla[0])
print('Ultimo elemento:', minhaTupla[-1])
print('Segundo elemento:', minhaTupla[-3])
#slicing
# 0          1       2       3
#('sono', 'comida', 'sol', 'sono')
        #[de:ate-1]
        #[1:3]
pequenaTupla = minhaTupla[1:3]
print(pequenaTupla)
pequenaTupla = minhaTupla[1:2+1]
print('Tupla de um elemento só')
tuplaUnicaFalsiane = ('Falsinha')
tuplaUnicaFalsiane = 'Falsinha'
print(tuplaUnicaFalsiane)
print(type(tuplaUnicaFalsiane))
#no fim das contas é uma string
tuplaUnicaVerdadeira = ('Unica',)
print(tuplaUnicaVerdadeira)
print(type(tuplaUnicaVerdadeira))
tuplaUnicaVerdadeira1 =  minhaTupla[2:3]
print(tuplaUnicaVerdadeira1)

#será que eu consigo ordernar uma tupla?
#nao consigo pq ela é imutavel
#minhaTupla.sort()
print('\n')
print(minhaTupla)
novaColecao = sorted(minhaTupla)
print(novaColecao)
print(type(novaColecao))
novaColecao = tuple(novaColecao)
print(novaColecao)
print(type(novaColecao))
print(sorted(minhaTupla))
# 0          1       2       3
#('sono', 'comida', 'sol', 'sono')
meuJeitoTupla = (minhaTupla[2:3], minhaTupla[0:1], minhaTupla[1:2])
print(meuJeitoTupla)
#inicializador
minhaTuplaVazia = ()
print(minhaTuplaVazia)
# poder vc pode fazer mas nao é útil
#operadores aritmeticos com tupla
#há possibilidade de combinar duas tuplas com o operador +
meusBrinquedos = ('patins', 'skate', 'bola')
minhasNecessidades = minhaTupla + meusBrinquedos
print(meusBrinquedos)
print(minhasNecessidades)
muitosBrinquedos = meusBrinquedos * 5
print(muitosBrinquedos)
#consigo colocar mais elementos na tupla?
#nao! ela imutavel
#dando meus pulos para acrescentar
minhaTupla = list(minhaTupla)
minhaTupla.append('praia')
print(minhaTupla)
print(type(minhaTupla))
minhaTupla = tuple(minhaTupla)
print(minhaTupla)
print(type(minhaTupla))

#tupla é indexado
#localizar um elemento
if 'sol' in minhaTupla:
    print('tem sol')
    print('o sol mora na casa:', minhaTupla.index('sol'))
#não há como remover itens em tupla, se vc quise vc tem q converter para lista
#toda manipulacao da tupla seja para
#adicionar um elemento (append -> adiciona o elemento no final, insert -> q adiciona em uma derminada posicao)
#remover um elemento (pop() -> sem indice remove do final, 
#com indice remove da localizado passade por ex pop(3) remove o terceiro elemento,
#del[1], remove('sol') para um determinado elemento
#ordenar (sort ou sorted)
#transformo em lista e reconverto para tupla depois da operacao.
print('Quantidade de elementos:', len(minhaTupla))
del minhaTupla
#print(minhaTupla)