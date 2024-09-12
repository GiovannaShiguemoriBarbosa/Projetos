# Leia o arquivo disponibilizado em aula e escreva imprima os primeiros 10 carateres
# ▪ Leia o arquivo disponibilizado em aula e separe em linhas. Conte quantas linhas tem o arquivo.
# ▪ Feche o arquivo e verifique se ele está fechado.
# ▪ Leia um arquivo e imprima suas linhas uma a uma. (não use lista)
# ▪ Imprima o arquivo anterior novamente.
# ▪ Transforme o arquivo em uma lista de linhas para serem impressas!
# ▪ Dada a lista abaixo, escreva em um aquivo
# ▪ ListaCapitais = ['São Paulo', 'Rio de Janeiro', 'Belo Horizonte', 'Curitiba’]
# ▪ Escreva um arquivo chamado compras_sexta.txt. Pergunte ao usuário a lista de compras. Escreva
# um item em cada linha

#Professora
#abordagem do READ
print('Imprimindo com abordagem OPEN E CLOSE E READ')
arqEx = open('Fiap_aula_arquivos.txt', 'r', encoding= 'UTF-8')
texto10 = arqEx.read(10)
print(texto10)
arqEx.close()

#Silvia
print('Exercício Arquivos \n')
print('Ler o arquivo e imprimir os dez primeiros caracteres \n')
print('Abrindo Arquivo')
AlunoTxt = open('Fiap_aula_arquivos.txt','r', encoding='UTF-8')
dezPrimeiro = AlunoTxt.readline(10)
print(dezPrimeiro, '\n')
AlunoTxt.close()

#Professora
#abordagem do WITH e SLICING
print('Imprimindo com abordagem do WITH e SLICING')
with open('Fiap_aula_arquivos.txt', 'r', encoding= 'UTF-8') as arqEx:
    texto = arqEx.read()
    #slicing variaveltexto[inicio:fim:passo]
    texto10 = texto[0:10]
    print(texto10)

#Leia o arquivo disponibilizado em aula e separe em linhas. Conte quantas linhas tem o arquivo.
# ▪ Transforme o arquivo em uma lista de linhas para serem impressas!
print('Leia o arquivo disponibilizado em aula e separe em linhas. Conte quantas linhas tem o arquivo.')
with open('Fiap_aula_arquivos.txt', 'r', encoding= 'UTF-8') as arqEx:
    listaLinhas = arqEx.readlines()
    print(listaLinhas)
    qtde_linhas = len(listaLinhas)
    print(f'Qtde Linhas {qtde_linhas:08}')

with open('Fiap_aula_arquivos.txt', 'r', encoding= 'UTF-8') as arqEx:
    qtde_linhas = 0
    for linha in arqEx:
        #o print tem uma variavel interna que marca o final de frase
        #quando imprimimos uma linha, ele automaticamente junta esse final de frase
        #ex: print('uva') ==> 'uva' + '\n'
        #podemos modificar esse caractere
        #ex: print('uva', end = ';') ==> 'uva' + ';'
        print(linha, end='')
        qtde_linhas += 1
    print(f'Qtde Linhas {qtde_linhas:08}')
# ▪ Feche o arquivo e verifique se ele está fechado.
if not(arqEx.closed):
    arqEx.close()


print('Imprimindo 2 x 10 caracteres a partir do inicio')
arqEx = open('Fiap_aula_arquivos.txt', 'r', encoding= 'UTF-8')
for count in range(2):
    arqEx.seek(0)
    print(arqEx.read(10))
arqEx.close()

# ▪ Dada a lista abaixo, escreva em um aquivo
# ▪ ListaCapitais = ['São Paulo', 'Rio de Janeiro', 'Belo Horizonte', 'Curitiba’]
# ▪ Escreva um arquivo chamado compras_sexta.txt. Pergunte ao usuário a lista de compras. Escreva
# um item em cada linha


#Silvia
ListaCapitais = ['São Paulo', 'Rio de Janeiro', 'Belo Horizonte', 'Curitiba']
ArqCapitais = open('ArqCapitais.txt', 'w', encoding='utf-8')
ArqCapitais.writelines(ListaCapitais)
print(ListaCapitais, '\n')
ArqCapitais.close()

# ▪ Escreva um arquivo chamado compras_sexta.txt. Pergunte ao usuário a lista de compras. Escreva
# um item em cada linha
print('Compras de sexta-feira')
arqCompras = open('compras_sexta.txt', 'w', encoding='utf-8')
resp = 's'
while resp in ('s', 'sim'):
    item = input('O que vc precisa comprar? ') + '\n'
    resp = input('Deseja acrescentar + 1 item? ').lower()
    arqCompras.writelines(item)
arqCompras.close()