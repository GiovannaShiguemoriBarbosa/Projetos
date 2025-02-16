-- Gerado por Oracle SQL Developer Data Modeler 23.1.0.087.0806
--   em:        2024-08-20 11:25:06 BRT
--   site:      Oracle Database 11g
--   tipo:      Oracle Database 11g





-- predefined type, no DDL - MDSYS.SDO_GEOMETRY

-- predefined type, no DDL - XMLTYPE

CREATE TABLE dim_atendimento (
    sk_atendimento    NUMBER NOT NULL,
    nr_duracao_lig    DATE NOT NULL,
    nr_satisfacao_cli VARCHAR2(2) NOT NULL,
    nr_temp_med_atend DATE,
    nm_arq_origem     VARCHAR2(10) NOT NULL,
    nm_atenndente     VARCHAR2(20) NOT NULL
);

COMMENT ON COLUMN dim_atendimento.sk_atendimento IS
    'Esta é a Surrogate Key da Dimensão atendimento. Seu conteúdo deve ser obrigatório e do tipo numérico.';

COMMENT ON COLUMN dim_atendimento.nr_duracao_lig IS
    'Esse atributo irá receber a duração da ligação . O conteúdo desse atributo será preenchido de forma automática pela aplicação';

COMMENT ON COLUMN dim_atendimento.nr_satisfacao_cli IS
    'Esse atributo irá receber o numero de satisfacao do cliente. O conteúdo desse atributo será preenchido de forma automática pela aplicação'
    ;

COMMENT ON COLUMN dim_atendimento.nr_temp_med_atend IS
    'Esse atributo irá receber o tempo medio do atendimento . O conteúdo desse atributo será preenchido de forma automática pela aplicação'
    ;

COMMENT ON COLUMN dim_atendimento.nm_arq_origem IS
    'Este dado representa o nome do arquivo que ocorreu o evento na Dimensão atendimento.';

COMMENT ON COLUMN dim_atendimento.nm_atenndente IS
    'Este dado representa o nome do nome da atendente  que ocorreu o evento na Dimensão atendimento. ';

ALTER TABLE dim_atendimento ADD CONSTRAINT dim_atendimento_pk PRIMARY KEY ( sk_atendimento );

CREATE TABLE dim_cliente (
    sk_cliente       NUMBER NOT NULL,
    nm_nome          VARCHAR2(90) NOT NULL,
    nr_cnpj          NUMBER(14) NOT NULL,
    nr_telefone      NUMBER(11) NOT NULL,
    ds_email         VARCHAR2(25) NOT NULL,
    ds_porte_empresa VARCHAR2(30) NOT NULL
);

COMMENT ON COLUMN dim_cliente.sk_cliente IS
    'Esta é a Surrogate Key da Dimensão cliente. Seu conteúdo deve ser obrigatório e do tipo numérico.';

COMMENT ON COLUMN dim_cliente.nm_nome IS
    'Este atributo irá receber o nome do cliente. Seu conteúdo deve ser obrigatório e do tipo caractere.';

COMMENT ON COLUMN dim_cliente.nr_cnpj IS
    'Este dado representa o número do cnpj  que ocorreu o evento na Dimensão cliente. Seu conteúdo deve ser obrigatório e do tipo numérico'
    ;

COMMENT ON COLUMN dim_cliente.nr_telefone IS
    'Este dado representa o número do telefone  que ocorreu o evento na Dimensão data. Seu conteúdo deve ser obrigatório e do tipo numérico'
    ;

COMMENT ON COLUMN dim_cliente.ds_email IS
    'Este atributo irá receber o email  do cliente. Seu conteúdo deve ser obrigatório e do tipo caractere.';

COMMENT ON COLUMN dim_cliente.ds_porte_empresa IS
    'Este atributo irá receber o porte da empresa  do cliente. Seu conteúdo deve ser obrigatório e do tipo caractere.';

ALTER TABLE dim_cliente ADD CONSTRAINT dim_cliente_pk PRIMARY KEY ( sk_cliente );

CREATE TABLE dim_data (
    sk_data               NUMBER NOT NULL,
    nr_dia                NUMBER NOT NULL,
    nr_ano                NUMBER(4) NOT NULL,
    nm_mes                VARCHAR2(15) NOT NULL,
    nm_feriado            VARCHAR2(30) NOT NULL,
    nm_dia_semana_extenso VARCHAR2(18) NOT NULL
);

COMMENT ON COLUMN dim_data.sk_data IS
    'Esta é a Surrogate Key da Dimensão data. Seu conteúdo deve ser obrigatório e do tipo numérico.';

COMMENT ON COLUMN dim_data.nr_dia IS
    'Este dado representa o dia da semana que ocorreu o evento na Dimensão data. Seu conteúdo deve ser obrigatório e do tipo numérico.'
    ;

COMMENT ON COLUMN dim_data.nr_ano IS
    'Este dado representa o ano que ocorreu o evento na Dimensão data. Seu conteúdo deve ser obrigatório e do tipo numérico. ';

COMMENT ON COLUMN dim_data.nm_mes IS
    'Este dado representa o mes por extenso da semana que ocorreu o evento na Dimensão data. Seu conteúdo deve ser obrigatório e do tipo string.'
    ;

COMMENT ON COLUMN dim_data.nm_feriado IS
    'Este dado representa o nome do feriado que ocorreu o evento na Dimensão data. Seu conteúdo deve ser opcional e do tipo string. '
    ;

COMMENT ON COLUMN dim_data.nm_dia_semana_extenso IS
    'Este dado representa o dia por extenso da semana que ocorreu o evento na Dimensão data. Seu conteúdo deve ser obrigatório e do tipo string.'
    ;

ALTER TABLE dim_data ADD CONSTRAINT dim_data_pk PRIMARY KEY ( sk_data );

CREATE TABLE dim_localizacao (
    sk_localizacao NUMBER NOT NULL,
    nr_cep         NUMBER(8) NOT NULL,
    nm_pais        VARCHAR2(15) NOT NULL,
    nm_bairro      VARCHAR2(35) NOT NULL,
    nm_cidade      VARCHAR2(10) NOT NULL,
    nm_estado      NUMBER(25) NOT NULL,
    nm_logradouro  VARCHAR2(50) NOT NULL
);

COMMENT ON COLUMN dim_localizacao.sk_localizacao IS
    'Esta é a Surrogate Key da Dimensão localização. Seu conteúdo deve ser obrigatório e do tipo numérico.';

COMMENT ON COLUMN dim_localizacao.nr_cep IS
    'Este dado representa o número do ce que ocorreu o evento na Dimensão localização. Seu conteúdo deve ser obrigatório e do tipo numérico.'
    ;

COMMENT ON COLUMN dim_localizacao.nm_pais IS
    'Esta é nome do pais  da empresa cliente  . Seu conteúdo deve ser obrigatório e do tipo string.';

COMMENT ON COLUMN dim_localizacao.nm_bairro IS
    'Esta é nome do Bairro da empresa do cliente . Seu conteúdo deve ser obrigatório e do tipo string.';

COMMENT ON COLUMN dim_localizacao.nm_cidade IS
    'Esta é nome do Estado da empresa do cliente . Seu conteúdo deve ser obrigatório e do tipo string.';

COMMENT ON COLUMN dim_localizacao.nm_estado IS
    'Esta é nome do Estado da empresa do cliente . Seu conteúdo deve ser obrigatório e do tipo string..';

COMMENT ON COLUMN dim_localizacao.nm_logradouro IS
    'Esta é nome do logradouro  da empresa do cliente . Seu conteúdo deve ser obrigatório e do tipo string..';

ALTER TABLE dim_localizacao ADD CONSTRAINT dim_localizacao_pk PRIMARY KEY ( sk_localizacao );

CREATE TABLE dim_sistema (
    sk_sistema        NUMBER NOT NULL,
    cd_sistema        NUMBER NOT NULL,
    nm_sistema        VARCHAR2(50) NOT NULL,
    ds_produto        VARCHAR2(100) NOT NULL,
    nr_quant_vend_sis NUMBER(3) NOT NULL,
    ds_diver_prod     VARCHAR2(50) NOT NULL
);

COMMENT ON COLUMN dim_sistema.sk_sistema IS
    'Esta é a Surrogate Key da Dimensão Sistema. Seu conteúdo deve ser obrigatório e do tipo numérico.';

COMMENT ON COLUMN dim_sistema.cd_sistema IS
    'Esta é código do sistema da Dimensão Vsistemar. Seu conteúdo deve ser obrigatório e do tipo numérico.';

COMMENT ON COLUMN dim_sistema.nm_sistema IS
    'Esta é nome do sistema da Dimensão Sistema. Seu conteúdo deve ser obrigatório e do tipo string.';

COMMENT ON COLUMN dim_sistema.ds_produto IS
    'Os tipos de produtos  possíveis';

COMMENT ON COLUMN dim_sistema.nr_quant_vend_sis IS
    'Esta é numero de sistemas vendidos da Dimensão sistema. Seu conteúdo deve ser obrigatório e do tipo numérico.';

COMMENT ON COLUMN dim_sistema.ds_diver_prod IS
    'Os tipos de produtos diversos';

ALTER TABLE dim_sistema ADD CONSTRAINT dim_sistema_pk PRIMARY KEY ( sk_sistema );

CREATE TABLE fto_eco_nps (
    sk_data             NUMBER NOT NULL,
    sk_sistema          NUMBER NOT NULL,
    sk_cliente          NUMBER NOT NULL,
    sk_localizacao      NUMBER NOT NULL,
    sk_atendimento      NUMBER NOT NULL,
    nr_nota             NUMBER(2) NOT NULL,
    ds_classificador    VARCHAR2(15) NOT NULL,
    nr_taxa_crescimento NUMBER(3) NOT NULL,
    nr_taxa_aband       NUMBER(3) NOT NULL,
    nr_taxa_resp_sist   NUMBER(3) NOT NULL,
    nr_nota_media       NUMBER(2) NOT NULL
);

COMMENT ON COLUMN fto_eco_nps.nr_nota IS
    'Esse atributo irá receber a nota dada ao serviço. O conteúdo desse atributo será preenchido de forma automática pela aplicação';

COMMENT ON COLUMN fto_eco_nps.ds_classificador IS
    'Este atributo irá receberdescricao da classificador.  Este atributo será oriundo da origem de dadosno ambiente operacional, ou seja, da ligação).'
    ;

COMMENT ON COLUMN fto_eco_nps.nr_taxa_crescimento IS
    'Esse atributo irá receber a taxa de crescimento. O conteúdo desse atributo será preenchido de forma automática pela aplicação';

COMMENT ON COLUMN fto_eco_nps.nr_taxa_aband IS
    'Esse atributo irá receber a taxa de abandono. O conteúdo desse atributo será preenchido de forma automática pela aplicação';

COMMENT ON COLUMN fto_eco_nps.nr_taxa_resp_sist IS
    'Esse atributo irá receber a taxa de resposta do sistema. O conteúdo desse atributo será preenchido de forma automática pela aplicação'
    ;

COMMENT ON COLUMN fto_eco_nps.nr_nota_media IS
    'Esse atributo irá receber a nota média dada ao serviço. O conteúdo desse atributo será preenchido de forma automática pela aplicação'
    ;

ALTER TABLE fto_eco_nps
    ADD CONSTRAINT fto_eco_nps_pk PRIMARY KEY ( sk_data,
                                                sk_sistema,
                                                sk_cliente,
                                                sk_localizacao,
                                                sk_atendimento );

ALTER TABLE fto_eco_nps
    ADD CONSTRAINT fto_eco_nps_dim_atendimento_fk FOREIGN KEY ( sk_atendimento )
        REFERENCES dim_atendimento ( sk_atendimento );

ALTER TABLE fto_eco_nps
    ADD CONSTRAINT fto_eco_nps_dim_cliente_fk FOREIGN KEY ( sk_cliente )
        REFERENCES dim_cliente ( sk_cliente );

ALTER TABLE fto_eco_nps
    ADD CONSTRAINT fto_eco_nps_dim_data_fk FOREIGN KEY ( sk_data )
        REFERENCES dim_data ( sk_data );

ALTER TABLE fto_eco_nps
    ADD CONSTRAINT fto_eco_nps_dim_localizacao_fk FOREIGN KEY ( sk_localizacao )
        REFERENCES dim_localizacao ( sk_localizacao );

ALTER TABLE fto_eco_nps
    ADD CONSTRAINT fto_eco_nps_dim_sistema_fk FOREIGN KEY ( sk_sistema )
        REFERENCES dim_sistema ( sk_sistema );



-- Relatório do Resumo do Oracle SQL Developer Data Modeler: 
-- 
-- CREATE TABLE                             6
-- CREATE INDEX                             0
-- ALTER TABLE                             11
-- CREATE VIEW                              0
-- ALTER VIEW                               0
-- CREATE PACKAGE                           0
-- CREATE PACKAGE BODY                      0
-- CREATE PROCEDURE                         0
-- CREATE FUNCTION                          0
-- CREATE TRIGGER                           0
-- ALTER TRIGGER                            0
-- CREATE COLLECTION TYPE                   0
-- CREATE STRUCTURED TYPE                   0
-- CREATE STRUCTURED TYPE BODY              0
-- CREATE CLUSTER                           0
-- CREATE CONTEXT                           0
-- CREATE DATABASE                          0
-- CREATE DIMENSION                         0
-- CREATE DIRECTORY                         0
-- CREATE DISK GROUP                        0
-- CREATE ROLE                              0
-- CREATE ROLLBACK SEGMENT                  0
-- CREATE SEQUENCE                          0
-- CREATE MATERIALIZED VIEW                 0
-- CREATE MATERIALIZED VIEW LOG             0
-- CREATE SYNONYM                           0
-- CREATE TABLESPACE                        0
-- CREATE USER                              0
-- 
-- DROP TABLESPACE                          0
-- DROP DATABASE                            0
-- 
-- REDACTION POLICY                         0
-- 
-- ORDS DROP SCHEMA                         0
-- ORDS ENABLE SCHEMA                       0
-- ORDS ENABLE OBJECT                       0
-- 
-- ERRORS                                   0
-- WARNINGS                                 0
