#Coleções
#nada mais sao que um jeito de armazenar
# varios dados em uma unica variavel
#caracteristicas
#os objetos/elementos de uma colecao podem ser de um
#mesmo tipo ou podem ser de tipos diferentes
#isso afeta alguns comportamentos como no caso do SORT
#TODA COLECAO É UM ELEMENTO ITERAVEL - que eu posso percorrer
#com um for por exemplo e acessar cada um dos elementos
#Existem varios tipos de coleções uma delas é LISTA
#é a mais poderosa das coleções
#ela permite varios tipos de operacoes
#Caracteristicas
#mutavel - ela nasce de um jeito e posso fazer algumas operações
#que vão mudando a lista
#expansivel, seja pelo acrescimo de um elemento ou de uma outra lista
#ordenadas
#indexas
#permitem duplicados
#permitem tipos de dados diferentes
print('Listas\n')
minhaLista = ['cafe', 'acucar', 'agua']
print(minhaLista)
print(type(minhaLista))
minhaLista = ['cafe', 'acucar', 'agua', 'cafe', 'cafe']
print(minhaLista)
print('Lista permite acessar elementos atraves do indice')
# 0         1       2       3       4
# -5       -4      -3      -2       -1
#['cafe', 'acucar', 'agua', 'cafe', 'cafe']
print('Primeiro elemento da lista', minhaLista[0])
print('Ultimo elemento da lista', minhaLista[4])
print('Terceiro elemento da lista', minhaLista[2])
print('Primeiro elemento da lista indice negativo', minhaLista[-5])
print('Ultimo elemento da lista indice negativo', minhaLista[-1])
print('Terceiro elemento da lista indice negativo', minhaLista[-3])
#Slicing lista
#           # 0         1       2       3       4
minhaLista = ['cafe', 'acucar', 'agua', 'cafe', 'cafe']
print('Criando listas a partir de outra lista')
                        #[de:ate +1]
pequenaLista = minhaLista[1:3+1]
print(pequenaLista)
print('Tamanho da lista', len(pequenaLista))
#mutavel ou expansivel
print('Acrescentando elementos na lista')
print('no final')
#append acrescenta um elemento no final da lista
minhaLista.append('baunilha')
print(minhaLista)
print('em uma determinada posicao')
#insert acrescenta um elemento no em uma determinada posicao da lista
minhaLista.insert(4,'nibs de cacau')
print(minhaLista)
#Coleções
#nada mais sao que um jeito de armazenar
# varios dados em uma unica variavel
#caracteristicas
#os objetos/elementos de uma colecao podem ser de um
#mesmo tipo ou podem ser de tipos diferentes
#isso afeta alguns comportamentos como no caso do SORT
#TODA COLECAO É UM ELEMENTO ITERAVEL - que eu posso percorrer
#com um for por exemplo e acessar cada um dos elementos
#Existem varios tipos de coleções uma delas é LISTA
#é a mais poderosa das coleções
#ela permite varios tipos de operacoes
#Caracteristicas
#mutavel - ela nasce de um jeito e posso fazer algumas operações
#que vão mudando a lista
#expansivel, seja pelo acrescimo de um elemento ou de uma outra lista
#ordenadas
#indexas
#permitem duplicados
#permitem tipos de dados diferentes
print('Listas\n')
minhaLista = ['cafe', 'acucar', 'agua']
print(minhaLista)
print(type(minhaLista))
minhaLista = ['cafe', 'acucar', 'agua', 'cafe', 'cafe']
print(minhaLista)
print('Lista permite acessar elementos atraves do indice')
# 0         1       2       3       4
# -5       -4      -3      -2       -1
#['cafe', 'acucar', 'agua', 'cafe', 'cafe']
print('Primeiro elemento da lista', minhaLista[0])
print('Ultimo elemento da lista', minhaLista[4])
print('Terceiro elemento da lista', minhaLista[2])
print('Primeiro elemento da lista indice negativo', minhaLista[-5])
print('Ultimo elemento da lista indice negativo', minhaLista[-1])
print('Terceiro elemento da lista indice negativo', minhaLista[-3])
#Slicing lista
#           # 0         1       2       3       4
minhaLista = ['cafe', 'acucar', 'agua', 'cafe', 'cafe']
print('Criando listas a partir de outra lista')
                        #[de:ate +1]
pequenaLista = minhaLista[1:3+1]
print(pequenaLista)
print('Tamanho da lista', len(pequenaLista))
#mutavel ou expansivel
print('Acrescentando elementos na lista')
print('no final')
#append acrescenta um elemento no final da lista
minhaLista.append('baunilha')
print(minhaLista)
print('em uma determinada posicao')
#insert acrescenta um elemento no em uma determinada posicao da lista
minhaLista.insert(4,'nibs de cacau')
print(minhaLista)

print('Removendo elementos na lista')
print('do final')
#pop sem indice elimina um elemento no final da lista
minhaLista.pop()
print(minhaLista)
print('de uma determinada posicao')
#pop com indice elimina um elemento de uma determinada posicao
minhaLista.pop(3)
print(minhaLista)
#posso fazer a mesma coisa com o del
del minhaLista[-1]
print(minhaLista)

print('Substituicao de elemento')
#substituindo um elemento
minhaLista[3] = 'canela'
print(minhaLista)
print('Operacoes de Lista com lista')
#um construtor da classe list é o simbolo de colchete []
#outro construtor é a propria funcao list
outraLista = list(('chantilly', 'baunilha'))
print(outraLista)
print(type(outraLista))
print('Extendendo uma lista')
minhaLista.extend(outraLista)
print(minhaLista)
pequenosMimos = ['raspas de limao', 'flor de sal']
print(pequenosMimos)
print(outraLista)
meusComplementosCafe = outraLista + pequenosMimos
print(meusComplementosCafe)
meusComplementosCafe = pequenosMimos + outraLista
print(meusComplementosCafe)
print('Encontrando um elemento e eliminando o elemento')
meusComplementosCafe.remove('flor de sal')
print(meusComplementosCafe)

print('Encontrando um elemento na lista')
print(minhaLista)
print('Descobrindo o indice de um elemento')
print('Onde esta o chantilly?')
print('posicao:',minhaLista.index('chantilly'))
print('substituindo o chantilly')
minhaLista[minhaLista.index('chantilly')] = 'flor de sal'
print(minhaLista)

teste = ['cafe', 'cafe', 'cafe']
print(teste)
teste[teste.index('cafe')] = 'agua'
print(teste)
print('Como toda lista é um elemento iteravel eu consigo usar o IN')
print(minhaLista)
if 'flor de sal' in minhaLista:
    print('oba, meu cafe ta chique')
print('Percorrer uma lista e imprimir todos os elementos um a um')
for elemento in minhaLista:
    print(elemento)
    #strings sao como listas, eu posso acessar via um indice
    print('primeira letra',elemento[0])

print('Listas sao ORDENAVEIS desde que todos os elementos sejam do MESMO TIPO')
print(minhaLista)
minhaLista.sort()
print(minhaLista)
minhaListaHeterogenea = ['check point', 'dia das maes', 1971, True, False]
print(minhaListaHeterogenea)
#minhaListaHeterogenea.sort()
print('Limpando toda a lista')
minhaListaHeterogenea.clear()
print(minhaListaHeterogenea)
del minhaListaHeterogenea
#print(minhaListaHeterogenea)
#Exercicios
# ▪ Acabou a pandemia, chegou o dia e você está ajudando a montar a lista de uma pequena
# reunião no seu apartamento. Conversando com o seu síndico ele proibiu que houvesse mais
# de 15 pessoas no seu apartamento. Faça um algorimo que peça a quantidade de pessoas da
# sua reunião. E utilizando a função FOR peça o nome dos convidados um a um. Certifique-se
# que seu melhor amigo João está na sua lista
