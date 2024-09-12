#DICIONARIO
# colecoes do tipo chave:valor
# formulario
# Exemplo
# Nome: Patricia
# Sexo: Feminino
# Idade: 18

print('Colecoes - Dicionario')
meuDicionario = {'nome': 'Patricia', 'sexo': 'feminino', 'idade': '18'}
print(meuDicionario)
print(type(meuDicionario))
outroDicionario = dict((('nome', 'Patricia'), ('sexo', 'feminino'), ('idade',18), ('vacina_covid', True)))
print(outroDicionario)
print('\nRecuperar um valor')
meuValor=meuDicionario['nome']
print(meuValor)
outroDicionario = dict((('nome', 'Patricia'), ('sexo', 'feminino'), (18,'idade'), ('vacina_covid', True)))
print(outroDicionario)
meuValor=outroDicionario[18]
print(meuValor)
meuValor = meuDicionario.get('sexo')
print(meuValor)
print('\nRecuperando todos os valores do dicionario sem a chave')
meusValores = meuDicionario.values()
print(meusValores)
print('\nRecuperando todos as chaves do dicionario sem os valores')
minhasChaves = meuDicionario.keys()
print(minhasChaves)
print('\nRecuperando todos os itens')
meusItens = meuDicionario.items()
print(meusItens)
print('\nRecuperando os itens VARRENDO a colecao')
print(meuDicionario)
#ATENCAO: se eu percorro um dicionarios sem especificar o que eu quero ele retorna as CHAVES
for item in meuDicionario:
    print('chaves:', item)
print('\nVarrendo as chaves')
for item in meuDicionario.keys():
    print('chaves:', item)
print('\nVarrendo os valores')
for item in meuDicionario.values():
    print('valores:', item)
print('\nVarrendo os itens')
for item in meuDicionario.items():
    print('valores:', item)
print('\nVarrendo os valores pela chave')
for item in meuDicionario:
    print('valores:', meuDicionario[item])
print('\nVarrendo os itens')
for chave, valor in meuDicionario.items():
    print(f'chave e valor: {chave} e {valor}')
print('\nAdicionando itens no dicionario')
meuDicionario['tipo sanguineo'] = 'ORh-'
print(meuDicionario)
print('\nAlterando valores')
meuDicionario['idade'] = 52
print(meuDicionario)
print('\nUsando o update para alterar valores')
meuDicionario.update({'nome':'Patricia Angelini'})
print(meuDicionario)
print('\nUsando o update para alterar valores - se a chave nao existir ele cria o indice')
meuDicionario.update({'estado civil':'casada'})
print(meuDicionario)
print('\nEliminando Itens')
del meuDicionario['idade']
print(meuDicionario)
print('\nEliminando Itens atraves do popitem - nao usa indice')
meuDicionario.popitem()
print(meuDicionario)
print('\nEliminando Itens atraves do pop - usa chave')
meuDicionario.pop('tipo sanguineo')
print(meuDicionario)
print('\nEliminando todos os itens')
meuDicionario.clear()
print(meuDicionario)
del meuDicionario
meuDicionario = {'nome': 'Patricia', 'sexo': 'feminino', 'idade': '18', 'tipo sanguineo': 'ORh-', 'estado civil': 'casada'}
print('\nLocalizando itens')
print('as chaves')
#atencao, quando eu NAO ESPECIFICO ele varre as CHAVES
if 'tipo sanguineo' in meuDicionario:
    print('Tem dados de tipo sanguineo')
print('os valores')
if 'Patricia' in meuDicionario.values():
    print('Patricia localizada')
print('\nCopiando Dicionarios')
#a copia é necessaria porque se eu IGUALO eu estou apenas apontando a variavel nova para a mesma colecao
copiaDicionario = meuDicionario.copy()
print(copiaDicionario)