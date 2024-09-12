print('Informacoes de Convidados')
# resp = 's'
# agenda = []
# while resp in ('s','sim'):
#     contato = {}
#     contato['nome'] = input('Entre com o nome: ').capitalize()
#     contato['telefone'] = input('Entre com o telefone: ')
#     contato.update({'estado civil':input('Entre com o estado civil: ')})
#     agenda.append(contato)
#     resp = input('Deseja cadastrar outro contato? ')
agenda = [{'nome': 'Patricia', 'telefone':'99999999'},{'nome':'Silvia','telefone':'777777'}]
print(agenda)
for dicionario in agenda:
    print('dicionario completo', dicionario)
    print('nome',dicionario['nome'])
    if 'Patricia' == dicionario['nome']:
        localizacao_dicionario = agenda.index(dicionario)
        print('localizacao do dicionario completo', localizacao_dicionario)
        #PARA APAGAR O ITEM DE UMA LISTA, EU PRECISO SABER SUA LOCALIZACAO, SEU INDICE
        agenda.pop(localizacao_dicionario)
        #del agenda(localizacao_dicionario)
print(agenda)