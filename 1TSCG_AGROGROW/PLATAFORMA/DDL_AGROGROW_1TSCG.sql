        /* NOME E RM*/
-- CYROS ALVES - RM: 98728 
-- GIOVANNA BARBOSA - RM: 99105
-- ISABELA ROMANATO - RM: 550234
-- LARISSA SANTANA - RM: 99398


-- Gerado por Oracle SQL Developer Data Modeler 21.4.2.059.0838
--   em:        2023-08-24 20:18:32 BRT
--   site:      Oracle Database 11g
--   tipo:      Oracle Database 11g


/*DROP TABLE t_analise_credito CASCADE CONSTRAINTS;

DROP TABLE t_cliente CASCADE CONSTRAINTS;

DROP TABLE t_contrato CASCADE CONSTRAINTS;

DROP TABLE t_empreendedor_industria CASCADE CONSTRAINTS;

DROP TABLE t_produto CASCADE CONSTRAINTS;

DROP TABLE t_territorio CASCADE CONSTRAINTS; */

-- predefined type, no DDL - MDSYS.SDO_GEOMETRY

-- predefined type, no DDL - XMLTYPE

CREATE TABLE t_analise_credito (
    cd_analise_cred NUMBER(6) NOT NULL,
    cd_territorio   NUMBER(8) NOT NULL,
    dt_analise      DATE NOT NULL,
    ds_credito      VARCHAR2(850) NOT NULL,
    ds_class_score  CHAR(5) NOT NULL
);

ALTER TABLE t_analise_credito ADD CONSTRAINT pk_t_analise_credito PRIMARY KEY ( cd_analise_cred );

CREATE TABLE t_cliente (
    cd_cliente    NUMBER(10) NOT NULL,
    nm_cliente    VARCHAR2(200) NOT NULL,
    nr_cpf        NUMBER(11) NOT NULL,
    nr_cpf_digito NUMBER(2) NOT NULL,
    nr_rg         NUMBER(9) NOT NULL,
    nr_rg_digito  NUMBER(2) NOT NULL,
    ds_email      VARCHAR2(70) NOT NULL,
    dt_nascimento DATE NOT NULL,
    ds_genero     CHAR(2) NOT NULL,
    nr_telefone   NUMBER(11) NOT NULL
);

ALTER TABLE t_cliente
    ADD CONSTRAINT ck_t_cliente_genero CHECK ( upper(ds_genero) = 'F'
                                               OR upper(ds_genero) = 'M' );

ALTER TABLE t_cliente ADD CONSTRAINT pk_t_cliente PRIMARY KEY ( cd_cliente );

ALTER TABLE t_cliente ADD CONSTRAINT un_t_cliente_cpf UNIQUE ( nr_cpf );

ALTER TABLE t_cliente ADD CONSTRAINT un_t_cliente_email UNIQUE ( ds_email );

ALTER TABLE t_cliente ADD CONSTRAINT un_t_cliente_rg UNIQUE ( nr_rg );

CREATE TABLE t_contrato (
    cd_contrato         NUMBER(6) NOT NULL,
    cd_cliente          NUMBER(10) NOT NULL,
    cd_empreendedor_ind NUMBER(6) NOT NULL,
    cd_produto          NUMBER(6) NOT NULL,
    qt_requerida        NUMBER(9) NOT NULL,
    qt_comercializada   NUMBER(9) NOT NULL,
    dt_contrato         DATE NOT NULL,
    ds_validade         VARCHAR2(15) NOT NULL
);

ALTER TABLE t_contrato ADD CONSTRAINT pk_t_contrato PRIMARY KEY ( cd_contrato );

CREATE TABLE t_empreendedor_industria (
    cd_empreendedor_ind NUMBER(6) NOT NULL,
    nm_negocio          VARCHAR2(50) NOT NULL,
    nr_cnpj             NUMBER(16) NOT NULL,
    ds_email            VARCHAR2(100) NOT NULL,
    nr_telefone         NUMBER(11) NOT NULL,
    ds_tipo             CHAR(2) NOT NULL
);

ALTER TABLE t_empreendedor_industria
    ADD CONSTRAINT ck_empreendedor_ind_ds_tipo CHECK ( ds_tipo = '1'
                                                       OR ds_tipo = '2' );

ALTER TABLE t_empreendedor_industria ADD CONSTRAINT pk_t_empreendedor_industria PRIMARY KEY ( cd_empreendedor_ind );

ALTER TABLE t_empreendedor_industria ADD CONSTRAINT un_empreendedor_email UNIQUE ( ds_email );

ALTER TABLE t_empreendedor_industria ADD CONSTRAINT un_empreendedor_ind_cnpj UNIQUE ( nr_cnpj );

CREATE TABLE t_produto (
    cd_produto        NUMBER(6) NOT NULL,
    ds_produto        VARCHAR2(150) NOT NULL,
    ds_completa       VARCHAR2(850) NOT NULL,
    qt_producao       NUMBER(10) NOT NULL,
    vl_preco_unitario NUMBER(4, 2) NOT NULL
);

ALTER TABLE t_produto ADD CONSTRAINT pk_t_produto PRIMARY KEY ( cd_produto );

CREATE TABLE t_territorio (
    cd_territorio  NUMBER(8) NOT NULL,
    cd_cliente     NUMBER(10) NOT NULL,
    ds_area        VARCHAR2(800) NOT NULL,
    ds_localizacao VARCHAR2(300) NOT NULL,
    ds_clima       VARCHAR2(50) NOT NULL,
    ds_solo        VARCHAR2(50) NOT NULL,
    ds_vegetacao   VARCHAR2(50) NOT NULL,
    sg_estado      CHAR(2) NOT NULL
);

ALTER TABLE t_territorio ADD CONSTRAINT pk_t_territorio PRIMARY KEY ( cd_territorio );

ALTER TABLE t_analise_credito
    ADD CONSTRAINT fk_analise_cred_territorio FOREIGN KEY ( cd_territorio )
        REFERENCES t_territorio ( cd_territorio );

ALTER TABLE t_contrato
    ADD CONSTRAINT fk_contrato_cliente FOREIGN KEY ( cd_cliente )
        REFERENCES t_cliente ( cd_cliente );

ALTER TABLE t_contrato
    ADD CONSTRAINT fk_contrato_empreendedor_ind FOREIGN KEY ( cd_empreendedor_ind )
        REFERENCES t_empreendedor_industria ( cd_empreendedor_ind );

ALTER TABLE t_contrato
    ADD CONSTRAINT fk_contrato_prod FOREIGN KEY ( cd_produto )
        REFERENCES t_produto ( cd_produto );

ALTER TABLE t_territorio
    ADD CONSTRAINT fk_territorio_cliente FOREIGN KEY ( cd_cliente )
        REFERENCES t_cliente ( cd_cliente );



-- Relatório do Resumo do Oracle SQL Developer Data Modeler: 
-- 
-- CREATE TABLE                             6
-- CREATE INDEX                             0
-- ALTER TABLE                             18
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
