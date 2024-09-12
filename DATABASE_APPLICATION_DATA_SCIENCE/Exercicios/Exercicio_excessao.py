print('Excecoes')

#interrupcao do fluxo normal do programa em execucao

#programa base
print('Media gastos supermercado')
valor_compras = float(input('Entre com o valor de compras:'))
qt_itens = int(input('Entre com a quantidade de itens:'))

preco_medio = valor_compras/qt_itens
print(f'Preço Médio R${preco_medio:.2f}')

#programa com o 1o nivel de exceções
try:
    print('Media gastos supermercado')
    valor_compras = float(input('Entre com o valor de compras:'))
    qt_itens = int(input('Entre com a quantidade de itens:'))

    preco_medio = valor_compras/qt_itens
    print(f'Preço Médio R${preco_medio:.2f}')
except:
    print('Houve uma exceção')

# #programa com o 2o nivel de exceções - tratar excecoes uma por uma
try:
    print('Media gastos supermercado')
    valor_compras = float(input('Entre com o valor de compras:'))
    qt_itens = int(input('Entre com a quantidade de itens:'))

    preco_medio = valor_compras/qt_itens
    print(f'Preço Médio R${preco_medio:.2f}')
except ZeroDivisionError:
    print('Houve uma divisao por zero, informe uma quantidade maior que zero')
except ValueError:
     print('Entre com um valor numerico')

# #programa com o 3o nivel de exceções - tratar excecoes uma por uma e vou tratar a excecao generica
try:
    print('Media gastos supermercado')
    valor_compras = float(input('Entre com o valor de compras:'))
    qt_itens = int(input('Entre com a quantidade de itens:'))

    preco_medio = valor_compras/qt_itens
    print(f'Preço Médio R${preco_medio:.2f}')
except ZeroDivisionError:
    print('Houve uma divisao por zero, informe uma quantidade maior que zero')
 except ValueError:
     print('Entre com um valor numerico')
except Exception as e:
    print(f'Houve uma exceção:Codigo - {e.__class__.__name__} Descricao - {e}')


# #programa com o 4o nivel de exceções -
# #tratar excecoes uma por uma e vou tratar a excecao generica
# #usar os blocos else e finally
try:
    print('Media gastos supermercado')
    #preco_medio = 0
    valor_compras = float(input('Entre com o valor de compras:'))
    qt_itens = int(input('Entre com a quantidade de itens:'))

    preco_medio = valor_compras/qt_itens

except ZeroDivisionError:
    print('Houve uma divisao por zero, informe uma quantidade maior que zero')
except ValueError:
    print('Entre com um valor numerico')
except Exception as e:
    print(f'Houve uma exceção:Codigo - {e.__class__.__name__} Descricao - {e}')
else: #só é executado quando não houver qualquer exceção
    if preco_medio >= 20:
        resp = input('Gostaria de participar do nosso programa de pontos?').upper()
        if resp in ('S', 'SIM'):
            print('Obrigada por participar')
finally: #é executado sempre
    print(f'Preço Médio R${preco_medio:.2f}')

#programa com o 5o nivel de exceções -
#tratar excecoes uma por uma e vou tratar a excecao generica
#usar os blocos else e finally
#com lancamento de excecoes
class NumeroNegativo(Exception):
    pass
try:
    print('Media gastos supermercado')
    preco_medio = 0
    valor_compras = float(input('Entre com o valor de compras:'))
    qt_itens = int(input('Entre com a quantidade de itens:'))

    if valor_compras < 0 or qt_itens < 0:
        #print('Entre com um valor positivo')
        raise NumeroNegativo('!!Valor Negativo!!')

    preco_medio = valor_compras/qt_itens

except ZeroDivisionError:
    print('Houve uma divisao por zero, informe uma quantidade maior que zero')
except ValueError:
    print('Entre com um valor numerico')
except NumeroNegativo as n:
    #print(n)
    print(f'{n.__class__.__name__} {n}')
except Exception as e:
    print(f'Houve uma exceção:Codigo - {e.__class__.__name__} Descricao - {e}')
else: #só é executado quando não houver qualquer exceção
    if preco_medio >= 20:
        resp = input('Gostaria de participar do nosso programa de pontos?').upper()
        if resp in ('S', 'SIM'):
            print('Obrigada por participar')
finally: #é executado sempre
    print(f'Preço Médio R${preco_medio:.2f}')

#Exercicio 1
# Elabore um algoritmo que leia dois números e imprima qual é maior, qual é
# menor; Se eles forem iguais lance uma exceção e termine o programa; 
# Elabore um algoritmo que leia dois números e imprima qual é maior, qual é
# menor; Se eles forem iguais lance uma exceção e termine o programa;
class NumerosIguais(Exception):
    pass

print('Comparar numeros')

try:
    a = int(input('Entre com um numero:'))
    b = int(input('Entre com um numero:'))

    if a > b:
        print('O numero maior é', a)
    elif b > a:
        print('O numero maior é', b)
    else:
        #quando usamos o ValueError - essa nao é uma pratica boa, pois estamos usando uma exceção do Python
        #raise ValueError('Os numeros são iguais')
        raise NumerosIguais('Os numeros são iguais')
except NumerosIguais as n:
    print(n)
except Exception as e:
    print('Houve uma exceção:', e)


# Elabore um algoritmo que leia as 5 primeiras letras do alfabeto (ou A, ou B, ou C,
# ou D) e o e imprima um nome de fruta que comece com essa letra. Caso seja
# digitado um uma outra letra, deverá ser lançada uma exceção;

#versao 1
class FrutaInvalida (Exception):
    pass

print('Frutas')
try:
    letra = input('Entre com uma letra de A a E:').lower()

    if letra == 'a':
        print('Abacaxi')
    elif letra == 'b':
        print('Banana')
    elif letra == 'c':
        print('Caqui')
    elif letra == 'd':
        print('Damasco')
    elif letra == 'e':
        print('Embaúba')
    else:
        raise FrutaInvalida('A letra não é valida')

except FrutaInvalida as f:
    print(f)
except Exception as e:
    print(e)

#versao 2
print('Frutas')
try:
    frutas = {'a': 'Abacaxi', 'b':'Banana', 'c':'Caqui', 'd':'Damasco', 'e':'Embauba'}
    letra = input('Entre com uma letra de A a E:').lower()
    minhafruta = frutas[letra]
    print(f'Minha fruta é {minhafruta}')

except KeyError as f:
    print('Letra Invalida:',f)
except Exception as e:
     print(e)

#Para vários tributos, a base de cálculo é o salário mínimo. Elabore um algoritmo
# que leia o valor do salário mínimo e o valor do salário de uma pessoa. Calcular e
# imprimir quantos salários mínimos essa pessoa ganha; Lance tratamentos de
# exceção condizentes;

class NumeroNegativo(Exception):
    pass
try:
    print('Qtd salarios minimos')
    quantidade_salarios = 0
    valor_salario = float(input('Entre com o valor do seu salario:'))
    valor_sal_minimo = float(input('Entre com o valor do salario minimo atualizado:'))

    if valor_salario < 0 or valor_sal_minimo < 0:
        raise NumeroNegativo('!!Valor Negativo!!')

    quantidade_salarios = valor_salario/valor_sal_minimo

except ZeroDivisionError:
    print('Houve uma divisao por zero, informe um valor de salario minimo mento que zero')
except ValueError:
    print('Entre com um valor numerico')
except NumeroNegativo as n:

    print(f'{n.__class__.__name__} {n}')
except Exception as e:
    print(f'Houve uma exceção:Codigo - {e.__class__.__name__} Descricao - {e}')
finally: #é executado sempre
    print(f'Quantidade de Salarios: {quantidade_salarios:.2f}')
