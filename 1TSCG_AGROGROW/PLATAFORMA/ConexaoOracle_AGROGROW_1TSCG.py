import oracledb
import csv

def conectar_banco():
    try:
        # ESTABELECE A CONEXÃO             #INSERIR USER E PASSWORD
        conn = oracledb.connect(user="", password="", dsn="oracle.fiap.com.br:1521/orcl")
        return conn
    except Exception as e:
        print("Erro", e)
        return None

def consultar_tabela(conn, tabela):
    c_consulta = conn.cursor()
    c_consulta.execute(f"SELECT * FROM {tabela}")
    ldados = list(c_consulta.fetchall())
    c_consulta.close()
    return ldados

def main():
    conn = conectar_banco()
    if conn is None:
        return

    while True:
        print(""" ESCOLHA UMA OPÇÃO
        1 - CONSULTA DA TABELA
        2 - INSERÇÃO DE UM REGISTRO
        3 - SAIR
        """)
        escolha = int(input("Escolha ->:"))

        if escolha == 1:
            print("CONSULTAR TABELA")
            tabela = input("Digite o nome da tabela que deseja consultar: ")
            ldados = consultar_tabela(conn, tabela)
            if len(ldados) == 0:
                print(f'\n **** NÃO HÁ DADOS NA TABELA {tabela} ****')
            else:
                print(ldados)

        elif escolha == 2:
            # Para a tabela T_CLIENTE
            print("INSERINDO DADOS DA TABELA T_CLIENTE")
            cd_cliente = int(input('ENTRE COM O CÓDIGO: '))
            nm_cliente = input('ENTRE COM O NOME: ')
            nr_cpf = int(input('ENTRE COM O NÚMERO DO CPF: '))
            nr_cpf_digito = int(input('ENTRE COM O DÍGITO DO CPF: '))
            nr_rg = int(input('ENTRE COM O NÚMERO DO RG: '))
            nr_rg_digito = int(input('ENTRE COM O DÍGITO DO RG: '))
            ds_email = input('ENTRE COM O EMAIL: ')
            dt_nascimento = input('ENTRE COM A DATA DO NASCIMENTO(YYYY-MM-DD): ')
            ds_genero = input('ENTRE COM O  GÊNERO: ')
            nr_telefone = int(input('ENTRE COM O NÚMERO DO TELEFONE: '))

            # Criação do cabeçalho para a tabela T_CLIENTE no arquivo CSV
            with open('dados_cliente.csv', mode='a', newline='') as arquivo_csv:
                escritor_csv = csv.writer(arquivo_csv)
                escritor_csv.writerow(
                    ["cd_cliente", "nm_cliente", "nr_cpf", "nr_cpf_digito", "nr_rg", "nr_rg_digito", "ds_email",
                     "dt_nascimento", "ds_genero", "nr_telefone"])

            cmd = f"insert into T_CLIENTE (cd_cliente, nm_cliente, nr_cpf, nr_cpf_digito, nr_rg, nr_rg_digito, ds_email, dt_nascimento,  ds_genero, nr_telefone)" \
                  f" values " \
                  f"({cd_cliente}, '{nm_cliente}', {nr_cpf}, {nr_cpf_digito}, {nr_rg}, {nr_rg_digito}, '{ds_email}', TO_DATE('{dt_nascimento}', 'YYYY-MM-DD'), '{ds_genero}', {nr_telefone})"
            print(cmd)
            with conn.cursor() as c_insert:
                c_insert.execute(cmd)
            conn.commit()
            # Salvar os dados em um arquivo CSV separado para a tabela T_CLIENTE
            with open('dados_cliente.csv', mode='a', newline='') as arquivo_csv:
                escritor_csv = csv.writer(arquivo_csv)
                escritor_csv.writerow(
                    [cd_cliente, nm_cliente, nr_cpf, nr_cpf_digito, nr_rg, nr_rg_digito, ds_email, dt_nascimento,
                     ds_genero, nr_telefone])


            # Para a tabela T_TERRITORIO
            print("INSERINDO DADOS DO TERRITORIO")
            cd_territorio = int(input('ENTRE COM O  CÓDIGO DO TERRITÓRIO: '))
            cd_cliente = int(input('ENTRE COM O CÓDIGO DO CLIENTE: '))
            ds_area = input('ENTRE COM A DESCRIÇÃO DA ÁREA: ')
            ds_localizacao = input('ENTRE COM A LOCALIZAÇÃO: ')
            ds_clima = input('ENTRE COM A DESCRIÇÃO DO CLIMA : ')
            ds_solo = input('ENTRE COM A DESCRIÇÃO DO SOLO: ')
            ds_vegetacao = input('ENTRE COM A VEGETAÇÃO: ')
            sg_estado = input('ENTRE COM A SIGLA DO ESTADO: ')

            # Criação do cabeçalho para a tabela T_TERRITORIO no arquivo CSV
            with open('dados_territorio.csv', mode='a', newline='') as arquivo_csv:
                escritor_csv = csv.writer(arquivo_csv)
                escritor_csv.writerow(
                    ["cd_territorio", "cd_cliente", "ds_area", "ds_localizacao", "ds_clima", "ds_solo", "ds_vegetacao",
                     "sg_estado"])

            cmd = f"insert into T_TERRITORIO (cd_territorio, cd_cliente, ds_area, ds_localizacao, ds_clima, ds_solo, ds_vegetacao, sg_estado)" \
                  f" values " \
                  f"({cd_territorio}, {cd_cliente}, '{ds_area}', '{ds_localizacao}', '{ds_clima}', '{ds_solo}', '{ds_vegetacao}','{sg_estado}')"

            print(cmd)

            with conn.cursor() as c_insert:
                c_insert.execute(cmd)
            conn.commit()
            # Salvar os dados em um arquivo CSV separado para a tabela T_TERRITORIO
            with open('dados_territorio.csv', mode='a', newline='') as arquivo_csv:
                escritor_csv = csv.writer(arquivo_csv)
                escritor_csv.writerow(
                    [cd_territorio, cd_cliente, ds_area, ds_localizacao, ds_clima, ds_solo, ds_vegetacao, sg_estado])

            # Para a tabela T_ANALISE_CREDITO
            print("INSERINDO DADOS DA ANALISE DE CRÉDITO")
            cd_analise_cred = int(input('ENTRE COM O CÓDIGO DA ANALISE DE CRÉDITO: '))
            cd_territorio = int(input('ENTRE COM O CÓDIGO DO TERRITÓRIO: '))
            dt_analise = input('ENTRE COM A DATA(YYYY-MM-DD): ')
            ds_credito = input('ENTRE COM A DESCRICAO DO CRÉDITO: ')
            ds_class_score = input('ENTRE COM A DESCRIÇÃO DA CLASSIFICAÇÃO DO SCORE: ')

            # Criação do cabeçalho para a tabela T_ANALISE_CREDITO no arquivo CSV
            with open('dados_analise_credito.csv', mode='a', newline='') as arquivo_csv:
                escritor_csv = csv.writer(arquivo_csv)
                escritor_csv.writerow(
                    ["cd_analise_cred", "cd_territorio", "dt_analise", "ds_credito", "ds_class_score"])

            cmd = f"insert into T_ANALISE_CREDITO (cd_analise_cred, cd_territorio, dt_analise, ds_credito, ds_class_score)" \
                  f" values " \
                  f"({cd_analise_cred}, {cd_territorio}, TO_DATE('{dt_analise}', 'YYYY-MM-DD'), '{ds_credito}', '{ds_class_score}')"

            print(cmd)

            with conn.cursor() as c_insert:
                c_insert.execute(cmd)
            conn.commit()
            # Salvar os dados em um arquivo CSV separado para a tabela T_TERRITORIO
            with open('dados_analise_credito.csv', mode='a', newline='') as arquivo_csv:
                escritor_csv = csv.writer(arquivo_csv)
                escritor_csv.writerow(
                    [cd_territorio, cd_cliente, ds_area, ds_localizacao, ds_clima, ds_solo, ds_vegetacao, sg_estado])

            # Para a tabela T_PRODUTO
            print("INSERINDO DADOS DO PRODUTO")
            cd_produto = int(input('ENTRE COM O CÓDIGO: '))
            ds_produto = input('ENTRE COM A DESCRIÇÃO DO PRODUTO: ')
            ds_completa = input('ENTRE COM A DESCRIÇÃO COMPLETA: ')
            qt_producao = int(input('ENTRE COM A QUANTIDADE: '))
            vl_preco_unitario = int(input('ENTRE COM O PREÇO UNITÁRIO : '))

            with open('dados_produto.csv', mode='a', newline='') as arquivo_csv:
                escritor_csv = csv.writer(arquivo_csv)
                escritor_csv.writerow(
                    ["cd_produto", "cd_cliente", "ds_area", "ds_localizacao", "ds_clima", "ds_solo", "ds_vegetacao",
                     "sg_estado"])

            cmd = f"insert into T_PRODUTO (cd_produto, ds_produto, ds_completa, qt_producao, vl_preco_unitario)" \
                  f" values " \
                  f"({cd_produto}, '{ds_produto}','{ds_completa}', {qt_producao}, {vl_preco_unitario})"

            print(cmd)

            with conn.cursor() as c_insert:
                c_insert.execute(cmd)
            conn.commit()

            # Salvar os dados em um arquivo CSV separado para cada tabela
            with open('dados_produto.csv', mode='a', newline='') as arquivo_csv:
                escritor_csv = csv.writer(arquivo_csv)
                escritor_csv.writerow([cd_produto, ds_produto, ds_completa, qt_producao, vl_preco_unitario])

            # Para a tabela T_EMPREENDEDOR_INDUSTRIA
            print("INSERINDO EMPREENDEDOR INDÚSTRIA")
            cd_empreendedor_ind = int(input('ENTRE COM O CÓDIGO: '))
            nm_negocio = input('ENTRE COM O NOME DO NEGÓCIO: ')
            nr_cnpj = int(input('ENTRE COM O CNPJ: '))
            ds_email = input('ENTRE COM O EMAIL: ')
            nr_telefone = int(input('ENTRE COM O TELEFONE : '))
            ds_tipo = input('ENTRE COM O TIPO (1- INDÚSTRIA ALIMENTÍCIA  ou 2 - OUTROS:')

            with open('dados_empreendedor_industria.csv', mode='a', newline='', encoding='utf-8') as arquivo_csv:
                escritor_csv = csv.writer(arquivo_csv)
                escritor_csv.writerow(
                    ["cd_empreendedor_ind", "nm_negocio", "nr_cnpj", "ds_email", "nr_telefone", "ds_tipo"])

            cmd = f"insert into T_EMPREENDEDOR_INDUSTRIA (cd_empreendedor_ind, nm_negocio, nr_cnpj, ds_email, nr_telefone, ds_tipo )" \
                  f" values " \
                  f"({cd_empreendedor_ind}, '{nm_negocio}',{nr_cnpj}, '{ds_email}', {nr_telefone},'{ds_tipo}')"

            print(cmd)

            with conn.cursor() as c_insert:
                c_insert.execute(cmd)
            conn.commit()

            # Salvar os dados em um arquivo CSV separado para cada tabela
            with open('dados_empreendedor_industria.csv', mode='a', newline='') as arquivo_csv:
                escritor_csv = csv.writer(arquivo_csv)
                escritor_csv.writerow([cd_empreendedor_ind, nm_negocio, nr_cnpj, ds_email, nr_telefone, ds_tipo])

            # Para a tabela T_CONTRATO
            print("INSERINDO DADOS DO CONTRATO")
            cd_contrato = int(input('ENTRE COM O CÓDIGO DO CONTRATO: '))
            cd_cliente = input('ENTRE COM O CÓDIGO DO CLIENTE: ')
            cd_empreendedor_ind = int(input('ENTRE COM O CÓDIGO DO EMPREENDEDOR: '))
            cd_produto = int(input('ENTRE COM O CÓDIGO DO PRODUTO: '))
            qt_requerida = int(input('ENTRE COM A QUANTIDADE REQUERIDA: '))
            qt_comercializada = int(input('ENTRE COM A QUANTIDADE COMERCIALIZADA: '))
            dt_contrato = input('ENTRE COM A DATA DO CONTRATO(YYYY-MM-DD): ')
            ds_validade = input('ENTRE COM A DESCRIÇÃO DA VALIDADE: ')

            with open('dados_contrato.csv', mode='a', newline='') as arquivo_csv:
                escritor_csv = csv.writer(arquivo_csv)
                escritor_csv.writerow(
                    ["cd_contrato", "cd_cliente", "cd_empreendedor_ind", "cd_produto", "qt_requerida",
                     "qt_comercializada", "dt_contrato",
                     "ds_validade"])

            cmd = f"insert into T_CONTRATO (cd_contrato, cd_cliente, cd_empreendedor_ind, cd_produto, qt_requerida, qt_comercializada, dt_contrato, ds_validade)" \
                  f" values " \
                  f"({cd_contrato}, {cd_cliente}, {cd_empreendedor_ind}, {cd_produto}, {qt_requerida}, {qt_comercializada},  TO_DATE('{dt_contrato}', 'YYYY-MM-DD'), '{ds_validade}')"

            print(cmd)

            with conn.cursor() as c_insert:
                c_insert.execute(cmd)
            conn.commit()

            # Salvar os dados em um arquivo CSV separado para cada tabela
            with open('dados_contrato.csv', mode='a', newline='') as arquivo_csv:
                escritor_csv = csv.writer(arquivo_csv)
                escritor_csv.writerow([cd_empreendedor_ind, nm_negocio, nr_cnpj, ds_email, nr_telefone, ds_tipo])


        elif escolha == 3:
            conn.close()
            break

if __name__ == "__main__":
    main()