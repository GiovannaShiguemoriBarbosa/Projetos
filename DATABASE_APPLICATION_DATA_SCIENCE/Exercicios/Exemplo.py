entradas = list()
o = True
while o:
    entradas.append(input('Qual delicia gourmet sua pessoa gostaria que estivsse no cardapio: ').lower())
    if (int(input('Deseja adicionar outra entrada:\n[1] - Sim\n[2] - Não: '))) == 2:
        o = False
if 'queijo rockerford' not in entradas:
    if (int(input('Queijo Rockerford não está em sua lista de entradas\nDeseja adiciona-lo:\n[1] - Sim\n[2] - Não: '))) == 1:
        entradas.append('queijo rockerford')

entradas = tuple(entradas)
print(f"Suas entradas são: {entradas}")
# Adicionar azeitoas
if 'queijo rockerford' in entradas:
    entradas = list(entradas)
    entradas.insert((entradas.index('queijo rockerford')+1), 'azeitona')
    entradas = tuple(entradas)

print(entradas)
tres_ultimos = entradas[slice(-1, -4, -1)]
print(tres_ultimos)
lista_com_qtd = list()
for x in entradas:
    lista_com_qtd.append([x, int(input('Qual a qtd de itens que tem esse item: '))])
print(lista_com_qtd)
entradas = entradas * 2
print(f'Duplicando para a festa:\n{entradas}')
