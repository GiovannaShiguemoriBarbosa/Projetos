saldo = 96.84
resto = 0
print('como descobrir as notas de 50,00??')
print('saldo:', saldo, 'resto:', resto)
if saldo > 50:
    #resultado = saldo / 50
    #print(resultado)
    qtde_cedulas = saldo // 50
    print('Qtde nota de 50:', qtde_cedulas)
    saldo = saldo - 50 * qtde_cedulas
    #print(saldo)
if saldo > 20:
    qtde_cedulas = saldo // 20
    print('Qtde nota de 20:', qtde_cedulas)
    saldo = saldo - (qtde_cedulas * 20)
    #print(saldo)
if saldo > 10:
    qtde_cedulas = saldo // 10
    print('Qtde nota de 10:', qtde_cedulas)
    saldo = saldo - (qtde_cedulas * 10)
    #print(saldo)
if saldo > 5:
    qtde_cedulas = saldo // 5
    print('Qtde nota de 5:', qtde_cedulas)
    saldo = saldo - (qtde_cedulas * 5)
    #print(saldo)
if saldo > 2:
    qtde_cedulas = saldo // 2
    print('Qtde nota de 2:', qtde_cedulas)
    saldo = saldo - (qtde_cedulas * 2)
    #print(saldo)
if saldo > 1:
    qtde_cedulas = saldo // 1
    print('Qtde nota de 1:', qtde_cedulas)
    saldo = saldo - (qtde_cedulas * 1)
    print(saldo)
saldo = saldo * 100
print(saldo)
if saldo > 50:
    qtde_moedas = saldo // 50
    print('Qtde moedas de 50:', qtde_moedas)
    saldo = saldo - 50 * qtde_moedas
    #print(saldo)
if saldo > 25:
    qtde_moedas = saldo // 25
    print('Qtde moedas de 25:', qtde_moedas)
    saldo = saldo - 25 * qtde_moedas
    #print(saldo)
if saldo > 10:
    qtde_moedas = saldo // 10
    print('Qtde moedas de 10:', qtde_moedas)
    saldo = saldo - 10 * qtde_moedas
    #print(saldo)
if saldo > 5:
    qtde_moedas = saldo // 5
    print('Qtde moedas de 5:', qtde_moedas)
    saldo = saldo - 5 * qtde_moedas
    #print(saldo)
if saldo > 1:
    qtde_moedas = saldo // 1
    print('Qtde moedas de 1:', qtde_moedas)
    saldo = saldo - 1 * qtde_moedas
    #print(saldo)
