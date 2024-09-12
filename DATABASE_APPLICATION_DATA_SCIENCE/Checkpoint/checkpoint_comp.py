contador = 0
while True:
    especie = input("Qual a espécie do seu animal?")
    nome = input("Qual o nome do seu animal?")
    if especie not in ['cachorro', 'gato']:
        print("Você trouxe", especie,
              " traga seu cachorro ou gato para ser vacinado.")
        contador = contador - 1
    elif especie in ["gato", "cachorro"]:
        print("Você trouxe ", especie, "podemos vacinar")
        vacina = 1
        while vacina <= 3:
            print(especie, nome, contador + 1)
            for _ in range(1, 4):
                print('Vacina', vacina, 'ok')
                vacina = vacina + 1
        novo = input('Ha mais algum animal para ser vacinado?')
        if novo == "não":
            contador = contador + 1
            print('Total de animais que participaram da campanha: ', contador)
            break
        else:
            print('Vamos recomeçar')
    else:
        print('Vamos recomeçar')
    contador = contador + 1
