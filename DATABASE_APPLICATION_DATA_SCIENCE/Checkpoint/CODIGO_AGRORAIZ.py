print('Bem-vindo a central AgroRaiz\n')
nome = str(input('Informe o nome produtor: ')).upper()
endereco = str(input('Qual o Endereço da propriedade? ')).upper()
prod_ou_cop = str(input('Produtor Rural ou Cooperativa: ')).upper()


print('Finalidades possiveis para emprestimo:\n')
print('Opção A: para Crédito de Custeio')
print('Opção B: para Crédito para Investimento')
print('Opção C: para outros tipos de crédito')
A = 'Crédito de Custeio'
B = 'Crédito para Investimento'
C = 'outros tipos de crédito'


finalidade_emprestimo = str(input('Escolha dentre as opções acima para qual é a finalidade do emprestimo:\n ')).upper()
if finalidade_emprestimo == 'A':
    fases = str(input('Em que fase sua produção está? (plantio, manutenção, colheita): ')).upper()
    colheita = int(input('Qual é a previsão da colheita (formato mmaaaa): '))
    print(f'O produtor {nome} situado no endereco: {endereco}. Solicita {A}, sua produção esta em {fases} e com colheita prevista para {colheita}. Crédito para {prod_ou_cop}')
elif finalidade_emprestimo == 'B':
    investimento = str(input('O créito será destinado para bens ou servios? ')).upper()
    print(f'O produtor {nome} situado no endereco: {endereco} solicita {B}, para investir em {investimento}. Crédito para {prod_ou_cop}')
elif finalidade_emprestimo == 'C':
    print(f'O produtor {nome} situado no endereco {endereco} solicita {C}, para isso serão necessarias mais informacoes sobre o produtor. Crédito para {prod_ou_cop}')
else:
    print('Dados cadastrados de maneira invalida.')