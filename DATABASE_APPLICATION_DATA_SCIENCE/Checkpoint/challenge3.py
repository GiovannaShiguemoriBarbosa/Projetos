import csv
solicitantes = []
resposta_cadastramento = str(input('Deseja se cadastrar? ')).capitalize()

if resposta_cadastramento == 'Sim':
  def cadastrar_solicitante():
      documento = int(input('Informe o CPF/CNPJ do solicitante: '))
      garantia = str(input('Informe a garantia para o emprestimo: '))
      valor_garantia = float(input('Informe o valor da garantia: '))
      return {'Documento do Solicitante': documento, 
              'Garantia Oferecida': garantia, 
              'Valor da Garantia Oferecida': valor_garantia}
  for i in range(5):
      print(f'\nCadastro do Solicitante')
      solicitante = cadastrar_solicitante()
      solicitantes.append(solicitante)

  print(f'\nDados armazenados no arquivo!')
else:
  print('Sem cadastro pendente, arquivo vazio.')
  


nome_arquivo = 'solicitantes.csv'
with open(nome_arquivo, 'w+') as arquivo_csv:
    campos = ['Documento do Solicitante', 'Garantia Oferecida', 'Valor da Garantia Oferecida']
    writer = csv.DictWriter(arquivo_csv, fieldnames=campos, delimiter=';')
    writer.writeheader()
    
    for solicitante in solicitantes:
        writer.writerow(solicitante)


    
