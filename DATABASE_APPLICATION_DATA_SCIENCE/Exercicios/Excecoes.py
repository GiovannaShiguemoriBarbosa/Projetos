#Exceções ocorrem quando há uma interrupção durante a EXECUÇÃO DO PROGRAMA
#Programa base - calcular a media de gastos no supermercado
# print('Valor medio de compras')
#
# valor = float(input('Entre com o valor das compras:'))
# qtd = int(input('Entre com a quantidade de itens:'))
#
# media = valor / qtd
#
# print(f'Valor medio das compras R${media:.2f}')
# # entendo exceções
# print('1a versao: Valor medio de compras')
#
# try:
#     valor = float(input('Entre com o valor das compras:'))
#     qtd = int(input('Entre com a quantidade de itens:'))
#
#     media = valor / qtd
#
#     print(f'Valor medio das compras R${media:.2f}')
# except:
#     print('Voce entrou com o valor errado de quantidade')
# print('2 versao: Valor medio de compras')
#
# try:
#     valor = float(input('Entre com o valor das compras:'))
#     qtd = int(input('Entre com a quantidade de itens:'))
#
#     media = valor / qtd
#
#     print(f'Valor medio das compras R${media:.2f}')
# except ZeroDivisionError as e:
#     print('Voce entrou com o valor errado de quantidade')
#     media = 0
#     print(f'Valor medio das compras R${media:.2f}')
# except ValueError as e:
#     print('Você entrou com letras no lugar de numeros')
#     media = 0
#     print(f'Valor medio das compras R${media:.2f}')
# except:
#     print('Erro desconhecido')
#     media = 0
#     print(f'Valor medio das compras R${media:.2f}')
# print('3a versao: Valor medio de compras')
#
# try:
#     media = 0
#     valor = float(input('Entre com o valor das compras:'))
#     qtd = int(input('Entre com a quantidade de itens:'))
#     media = valor / qtd
# except ZeroDivisionError as e:
#     print('Voce entrou com o valor errado de quantidade')
# except ValueError as e:
#     print('Voce entrou com letras no lugar de numeros')
# except:
#     print('Erro desconhecido')
# finally:
#      print(f'Valor medio das compras R${media:.2f}')
print('4a versao: Valor medio de compras  - uso do else')
try:
    media = 0
    valor = float(input('Entre com o valor das compras:'))
    qtd = int(input('Entre com a quantidade de itens:'))
    media = valor / qtd
except ZeroDivisionError as e:
    print('Voce entrou com o valor errado de quantidade')
except ValueError as e:
    print('Voce entrou com letras no lugar de numeros')
except:
    print('Erro desconhecido')
else:
    resp = input('Vc gostaria de entrar no programa de pontos')
    if resp == 's':
        print('Vamos fazer um cadastro')
finally:
     print(f'Valor medio das compras R${media:.2f}')

