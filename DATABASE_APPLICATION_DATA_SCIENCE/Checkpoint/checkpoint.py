especies = ("Gato", "Cachorro")
total_vacinados = 0

while total_vacinados < 2:
    animais = input("Qual a espécie do seu animal (Gato|Cachorro): ")
    nome = input("Qual o nome do animal: ")

    if animais in especies:
        print(f"Você trouxe um {animais} chamado {nome}.")
        for i in range(3):
            input(f"Vacina {i+1} OK")
        total_vacinados += 1
    else:
        print("Espécie inválida.")

print(f"Total de animais que participaram da campanha: {total_vacinados}")
