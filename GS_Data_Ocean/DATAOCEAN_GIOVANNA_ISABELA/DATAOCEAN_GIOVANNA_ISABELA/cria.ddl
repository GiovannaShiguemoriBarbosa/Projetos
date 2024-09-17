-- Gerado por Oracle SQL Developer Data Modeler 21.4.2.059.0838
--   em:        2024-06-04 10:38:06 BRT
--   site:      Oracle Database 11g
--   tipo:      Oracle Database 11g

-- predefined type, no DDL - MDSYS.SDO_GEOMETRY

-- predefined type, no DDL - XMLTYPE

CREATE TABLE dim_dtoc_atv_economica (
    sk_dtoc_atv_economica  NUMBER NOT NULL,
    ds_atv_economica       VARCHAR2(80) NOT NULL,
    ds_setor_economico     VARCHAR2(50) NOT NULL,
    ds_sub_setor_economico VARCHAR2(20) NOT NULL
);

COMMENT ON COLUMN dim_dtoc_atv_economica.sk_dtoc_atv_economica IS
    'Esse atributo irá receber  a surrogate key da atividade economica. O conteúdo desse atributo será preenchido de forma automática pela aplicação.';

COMMENT ON COLUMN dim_dtoc_atv_economica.ds_atv_economica IS
    'Esse atributo irá recebera descrição da atividade economica (hierarquia de sub_sector). O conteúdo desse atributo será preenchido de forma automática pela aplicação.';

COMMENT ON COLUMN dim_dtoc_atv_economica.ds_setor_economico IS
    'Esse atributo irá recebera descrição do setor economico . O conteúdo desse atributo será preenchido de forma automática pela aplicação.';

COMMENT ON COLUMN dim_dtoc_atv_economica.ds_sub_setor_economico IS
    'Esse atributo irá recebera descrição do sub setor economico (hierarquia de setor) . O conteúdo desse atributo será preenchido de forma automática pela aplicação.';

ALTER TABLE dim_dtoc_atv_economica ADD CONSTRAINT dim_dtoc_atv_economica_pk PRIMARY KEY ( sk_dtoc_atv_economica );

CREATE TABLE dim_dtoc_localizacao (
    sk_dtoc_localizacao NUMBER NOT NULL,
    ds_continente       VARCHAR2(30) NOT NULL,
    nm_pais             VARCHAR2(20) NOT NULL,
    nm_capital_pais     VARCHAR2(100) NOT NULL,
    ds_regiao_pais      VARCHAR2(50) NOT NULL
);

COMMENT ON COLUMN dim_dtoc_localizacao.sk_dtoc_localizacao IS
    'Esse atributo irá receber  a surrogate key da localização. O conteúdo desse atributo será preenchido de forma automática pela aplicação.';

COMMENT ON COLUMN dim_dtoc_localizacao.ds_continente IS
    'Esse atributo irá receber  a descrição do continente. O conteúdo desse atributo será preenchido de forma automática pela aplicação.';

COMMENT ON COLUMN dim_dtoc_localizacao.nm_pais IS
    'Esse atributo irá receber o nome do país. O conteúdo desse atributo será preenchido de forma automática pela aplicação.';

COMMENT ON COLUMN dim_dtoc_localizacao.nm_capital_pais IS
    'Esse atributo irá receber o nome da capital do país. O conteúdo desse atributo será preenchido de forma automática pela aplicação.';

COMMENT ON COLUMN dim_dtoc_localizacao.ds_regiao_pais IS
    'Esse atributo irá recebera descrição da região do país. O conteúdo desse atributo será preenchido de forma automática pela aplicação.';

ALTER TABLE dim_dtoc_localizacao ADD CONSTRAINT dim_dtoc_localizacao_pk PRIMARY KEY ( sk_dtoc_localizacao );

CREATE TABLE dim_dtoc_moeda (
    sk_moeda      NUMBER NOT NULL,
    nm_moeda_pais VARCHAR2(30) NOT NULL
);

COMMENT ON COLUMN dim_dtoc_moeda.sk_moeda IS
    'Esse atributo irá receber a surrogate key da moeda. O conteúdo desse atributo será preenchido de forma automática pela aplicação.';

COMMENT ON COLUMN dim_dtoc_moeda.nm_moeda_pais IS
    'Esse atributo irá receber o nome da moeda do país. O conteúdo desse atributo será preenchido de forma automática pela aplicação.';

ALTER TABLE dim_dtoc_moeda ADD CONSTRAINT dim_dtoc_moeda_pk PRIMARY KEY ( sk_moeda );

CREATE TABLE dim_dtoc_tempo (
    sk_dtoc_tempo NUMBER NOT NULL,
    dt_evento     DATE NOT NULL,
    nr_ano        NUMBER(4) NOT NULL,
    nr_mes        NUMBER(2) NOT NULL,
    nr_dia        NUMBER(2) NOT NULL,
    nm_dia_semana VARCHAR2(25) NOT NULL
);

COMMENT ON COLUMN dim_dtoc_tempo.sk_dtoc_tempo IS
    'Esse atributo irá receber a surrogate key do tempo. O conteúdo desse atributo será preenchido de forma automática pela aplicação.';

COMMENT ON COLUMN dim_dtoc_tempo.dt_evento IS
    'Esse atributo irá receber a data em que ocorreu o evento, ou seja, em um determinado, dia, mês e ano. O conteúdo desse atributo será preenchido de forma automática pela aplicação.';

COMMENT ON COLUMN dim_dtoc_tempo.nr_ano IS
    'Esse atributo irá receber o ano em que ocorreu o evento. O conteúdo desse atributo será preenchido de forma automática pela aplicação.';

COMMENT ON COLUMN dim_dtoc_tempo.nr_mes IS
    'Esse atributo irá receber o mês em que ocorreu o evento. O conteúdo desse atributo será preenchido de forma automática pela aplicação';

COMMENT ON COLUMN dim_dtoc_tempo.nr_dia IS
    'Esse atributo irá receber o dia em que ocorreu o evento. O conteúdo desse atributo será preenchido de forma automática pela aplicação';

COMMENT ON COLUMN dim_dtoc_tempo.nm_dia_semana IS
    'Esse atributo irá receber o dia da semana em que ocorreu o evento. O conteúdo desse atributo será preenchido pelo processp de etl.';

ALTER TABLE dim_dtoc_tempo ADD CONSTRAINT dim_dtoc_tempo_pk PRIMARY KEY ( sk_dtoc_tempo );

CREATE TABLE fto_dtoc_indicador (
    sk_moeda              NUMBER NOT NULL,
    sk_dtoc_atv_economica NUMBER NOT NULL,
    sk_dtoc_tempo         NUMBER NOT NULL,
    sk_dtoc_localizacao   NUMBER NOT NULL,
    sk_dtoc_indicador     NUMBER NOT NULL,
    nm_indicador          VARCHAR2(50) NOT NULL
);

COMMENT ON COLUMN fto_dtoc_indicador.sk_dtoc_indicador IS
    'Esse atributo irá receber a surrogate key do indicador. O conteúdo desse atributo será preenchido de forma automática pela aplicação.';

COMMENT ON COLUMN fto_dtoc_indicador.nm_indicador IS
    'Esse atributo irá receber o nome do indicador. O conteúdo desse atributo será preenchido de forma automática pela aplicação.';

ALTER TABLE fto_dtoc_indicador
    ADD CONSTRAINT fto_dtoc_indicador_pk PRIMARY KEY ( sk_dtoc_indicador,
                                                       sk_moeda,
                                                       sk_dtoc_atv_economica,
                                                       sk_dtoc_tempo,
                                                       sk_dtoc_localizacao );

ALTER TABLE fto_dtoc_indicador
    ADD CONSTRAINT fk_dim_dtoc_atv_economica FOREIGN KEY ( sk_dtoc_atv_economica )
        REFERENCES dim_dtoc_atv_economica ( sk_dtoc_atv_economica );

ALTER TABLE fto_dtoc_indicador
    ADD CONSTRAINT fk_dim_dtoc_loc FOREIGN KEY ( sk_dtoc_localizacao )
        REFERENCES dim_dtoc_localizacao ( sk_dtoc_localizacao );

ALTER TABLE fto_dtoc_indicador
    ADD CONSTRAINT fk_dim_dtoc_moeda FOREIGN KEY ( sk_moeda )
        REFERENCES dim_dtoc_moeda ( sk_moeda );

ALTER TABLE fto_dtoc_indicador
    ADD CONSTRAINT fk_dim_dtoc_tempo FOREIGN KEY ( sk_dtoc_tempo )
        REFERENCES dim_dtoc_tempo ( sk_dtoc_tempo );



-- Relatório do Resumo do Oracle SQL Developer Data Modeler: 
-- 
-- CREATE TABLE                             5
-- CREATE INDEX                             0
-- ALTER TABLE                              9
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
