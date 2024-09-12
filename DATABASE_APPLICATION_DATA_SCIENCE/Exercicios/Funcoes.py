#Funcoes

#sao pedacoes de codigo, divididos para organizar o projeto
#vantagens
#1.especializacao
#2.reaproveitamento (bibliotecas)
#3.separacao do escopo - as variaveis criadas dentro
# de uma funcao sao vistas apenas dentro da funcao

#Normalmente fazemos uma separacao
#PROCEDURE ou PROCEDIMENTO aquele trecho de codigo q nao retorna valor
#FUNCTION ou FUNCAO aquele trecho de codigo que RETORNA (RETURN) valor

#em Python não há essa separacao de nome, tudo chama FUNCAO

#Normalmente as funcoes sao definidas no inicio do arquivo .py e
# utilizadas depois no programa principal
# porque?
# porque assim como as variaveis eu preciso mencionar
# o nome para que o python saiba do que se trata
# ou seja, eu nao posso usar uma funcao, sem ter construido a funcao

#em algumas literaturas encontramos autores que defendem que
# as funcoes devem ser definidas (DEF) proximo ao seu uso

# a funcao é divida em 2 partes: a sua construcao propriamente dita, e o seu uso
#1a parte construcao
def OlaMundo():
    print('Ola Mundo')
#2a parte uso
OlaMundo()

nmGlobal = 'Patricia'
def Soma2():
    res = 1 + 5
    print(res)
    #consigo imprimir essa variavel pois ela esta no programa principal - ESCOPO GLOBAL
    #e foi definida antes da especificacao da funcao
    print(nmGlobal)
    #nao consigo imprimir essa variavel pois
    #apesar dela estar no programa principal - ESCOPO GLOBAL
    #ela foi definida DEPOIS da especificacao da funcao
    #print(nmGlobal2)
Soma2()
nmGlobal2 = 'Lis'
#NUNCA CONSIGO USAR UMA VARIAVEL QUE FOI DEFINIDA DENTRO DA FUNCAO - ESCOPO LOCAL
#print(res)

#Parametros sao um jeito de conversar entre ESCOPO GLOBAL E ESCOPO LOCAL

def Soma3(p1, p2):
    res = p1 + p2
    print(res)
Soma3(1, 5)

#parametros default: sao parametros padrao que caso eu nao passe
# nenhum valor na hora do uso, ele já tem um valor padrao
def Soma4(p1, p2=100):
    res = p1 + p2
    print(res)
Soma4(1, 5)
Soma4(9)

#nao funciona definir parametros default no meio de parametros comuns
# def Soma4(p1, p2=100, p3):
#     res = p1 + p2 + p3
#     print(res)

#porem funciona ter varios parametros default
def Soma5(p1, p2=100, p3=8):
    res = p1 + p2 + p3
    return(res)
#Quando é funcao, ou seja, quando há retorno de valor,
# eu posso usar a funcao dentro de outra funcao
# como no exemplo abaixo o print
print(Soma5(4))
print(Soma5(2, 56))
print(Soma5(2, 56, 99))

#suponha que eu queira fazer uma funcao que ora eu use com 3 parametros,
#ora eu use com 5, ora eu use com 42 parametros
#COM ESSE NUMERO DE PARAMETROS NAO É VIAVEL FICAR FAZENDO PARAMETROS DEFAULT
#Soma6(2, 4)
#Soma6(3,6,2,66,42,8,9,0,-1,988)
#como fazer?

#Quantidade de parametros variavel
print('Quantidade de parametros variaveis')
def Soma6(*p):
    #print(p)
    res = 0
    for parcela in p:
        #res += parcela
        res = res + parcela
    return(res)

print(Soma6(2, 4))
print(Soma6(3,6,2,66,42,8,9,0,-1,988))

#fazer uma funcao que multiplique N termos
def Mult(*p):
    #print(p)
    res = 1
    for parcela in p:
        #res += parcela
        res = res + parcela
    return(res)

print(Mult(2, 4))
print(Mult(3,6,2,66,42,8,9,0,-1,988))

#map
print('Map')
print('Funcao simples que adiciona o numero 1 a cada valor passado')
def AdUm(valor):
    res = valor + 1
    return(res)
print(AdUm(5))

listaValores = [7, 9, 34, 25]
print(listaValores)
listaValoresNova = []
for elemento in listaValores:
    resultado = AdUm(elemento)
    listaValoresNova.append(resultado)
    #listaValoresNova.append(AdUm(elemento))
print(listaValoresNova)

#o map acaba com esse loop automatizando a chamada de uma
# funcao para um elemento iteravel
print('lista nova de valores usando o MAP')
listaValoresNova = list(map(AdUm, listaValores))
print(listaValoresNova)

#CRIA UMA FUNCAO Q CALCULA 20% DE DESCONTO
#USANDO O MAP APLIQUE A FUNCAO AOS PRECOS
precos = [45, 22, 567, 99]
#E EXIBA UMA LISTA DE PRECOS COM DESCONTO precos_desconto
def Desc20(valor):
    res = valor * 0.8
    return(res)
precos_desconto = list(map(Desc20, precos))

print(precos)
print(precos_desconto)

def Desc(valor, desc):
    if desc > 1:
        desc = desc / 100
    res = valor * (1-desc)
    return(res)

precos = [45, 22, 567, 99]
descontos = [0.2, 0.2, 0.2, 0.2]
precos_desconto = list(map(Desc, precos, descontos))
print(precos)
print(descontos)
print(precos_desconto)

precos = [45, 22, 567, 99]
descontos = [0.2, 0.1, 0.35, 0.2]
precos_desconto = list(map(Desc, precos, descontos))
print(precos)
print(descontos)
print(precos_desconto)

#FUNCOES LAMBDA
#Sao funcoes de 1 linha para serem definidas e usadas imediatamente
#Normalmente essas funcoes nao possuem nome - a medida que as definimos ja as utilizamos
def Soma3(p1, p2):
    res = p1 + p2
    return(res)
print(Soma3(1, 5))
print('Funcoes Lambda')
ldSoma3 = lambda p1, p2 : p1 + p2
print(ldSoma3(1,5))
print((lambda p1, p2 : p1 + p2)(1,5))
print((lambda n1, n2: n1 + ' venceu o campeonato de ' + n2)('Lis','Skate'))
ldMaior = lambda n1, n2: n1 if n1>n2 else n2
print(ldMaior(7,5))

#Fazer um lambda para calcular o oposto de um numero
print((lambda x : -x)(-15))

#Fazer um lambda para calcular o inverso de um numero
print((lambda y : 1/y)(-15))

#Lambda + Map sao o casamento perfeito
print('Lambda e Map')
#lambda para calcular a metade de um numero
listaOriginal = [5, 6, 7, 8]
print(listaOriginal)
ldMetade = lambda x: x/2
for item in listaOriginal:
    print(ldMetade(item))

print('Usando o lambda e  varrrendo a lista')
#melhorando o codigo
listaMetade = []
for item in listaOriginal:
    listaMetade.append(ldMetade(item))
print(listaOriginal)
print(listaMetade)

print('Casamento Perfeito')
ldMetade = lambda x: x/2
listaOriginal = [5, 6, 7, 8]
listaMetade = list(map(ldMetade, listaOriginal))
print(listaOriginal)
print(listaMetade)

print('Casamento mais que Perfeito')
listaOriginal = [5, 6, 7, 8]
listaMetade = list(map((lambda x: x/2), listaOriginal))
print(listaOriginal)
print(listaMetade)

print('Casamento mais que Perfeito de uma linha so')
listaMetade = list(map((lambda x: x/2), ([5, 6, 7, 8])))
print(listaMetade)

print('Casamento perfeito com 2 parametros')
listaDivididos = list(map((lambda x,y: x/y), [5, 6, 7, 8], [2, 3, 4, 2]))
print(listaDivididos)
