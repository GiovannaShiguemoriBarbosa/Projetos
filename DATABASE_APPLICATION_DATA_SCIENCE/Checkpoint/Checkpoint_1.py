import datetime

# Obtemos a data atual
hoje = datetime.datetime.now()

# Definimos as variáveis para "sim" e "não"
sim = "SIM"
nao = "NÃO"

# Verificamos se hoje é sexta-feira
if hoje.weekday() == 4:
    # Pedimos para o usuário informar se o SNIFF lavou e fez o dever de casa
    lavou_sniff = input("Você lavou o SNIFF?: ").upper()
    fez_dever_casa = input("Você fez o dever de casa?: ").upper()

    # Verificamos se o usuário respondeu "sim" para ambas as perguntas
    if lavou_sniff == sim and fez_dever_casa == sim:
        # Se o SNIFF lavou e fez o dever de casa, exibimos a mensagem
        print("Parabéns! Você lavou o SNIFF e fez o dever de casa. Vamos tomar sorvete na DAMP!")
    else:
        # Se o SNIFF não lavou ou não fez o dever de casa, exibimos a mensagem
        print("Ops! Você precisa lavar o SNIFF e fazer o dever de casa para irmos tomar sorvete na DAMP.")
else:
    # Se não for sexta-feira, exibimos a mensagem
    print("Hoje não é sexta-feira. Ainda não é hora de tomar sorvete na DAMP.")

