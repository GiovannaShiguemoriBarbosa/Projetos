#programa com o 4 nivel de exceções -
#tratar excecoes uma por uma e vou tratar a excecao generica
#usar os blocos else e finally
try:
    print('Media gastos supermercado')
    preco_medio = 0
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