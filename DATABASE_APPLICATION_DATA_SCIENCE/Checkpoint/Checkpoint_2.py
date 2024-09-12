contador = 0
while contador < 2:
    especie = input("Qual a espécie do seu animal?")
    nome = input("Qual o nome do seu animal?")
    if especie != 'cachorro' and especie != 'gato':
        print("Você trouxe", especie, ". Traga seu cachorro ou gato para ser vacinado.")
    elif especie == "gato" or especie == "cachorro":
        print("Você trouxe ", especie, "podemos vacinar")
        vacina = 1
        while vacina <= 3:
            print(especie, nome, contador + 1)
            print('Vacina', vacina, 'ok')
            vacina = vacina + 1
        novo = input('Há mais algum animal para ser vacinado?')
        if novo == "não":
            print('Todas as 3 vacinas foram aplicadas')
        else:
            print('Você precisará voltar')
    else:
        print('Não podemos vacinar')
    contador = contador + 1

print('Total de animais que participaram da campanha: ', contador)