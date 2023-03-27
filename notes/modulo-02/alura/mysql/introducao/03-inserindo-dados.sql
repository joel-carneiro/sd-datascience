USE SUCOS;

# INSERINDO DADOS A TABELA DE PRODUTOS
INSERT INTO PRODUTOS (
	PRODUTO,
    NOME,
    EMBALAGEM,
    TAMANHO,
    SABOR,
    PRECO_DE_LISTA
) VALUES (
	'1040107',
    'Light - 350ml - Melância',
    'Lata',
    '350 ml',
    'Melância',
    4.56
);

# SEGUNDO PRODUTO

INSERT INTO PRODUTOS (
	PRODUTO,
    NOME,
    EMBALAGEM,
    TAMANHO,
    SABOR,
    PRECO_DE_LISTA
) VALUES (
	'1330177',
    'Clean - 2 Litros - Laranja',
    'PET',
    '2 Litros',
    'Laranja',
    16.01
);

# TERCEIRO PRODUTO

INSERT INTO PRODUTOS (
	PRODUTO,
    NOME,
    EMBALAGEM,
    TAMANHO,
    SABOR,
    PRECO_DE_LISTA
) VALUES (
	'2345197',
    'Sabor da Montanha - 700 ml - Uva',
    'Garrafa',
    '700ml',
    'Uva',
    6.31
);

# QUARTO PRODUTO

INSERT INTO PRODUTOS (
	PRODUTO,
    NOME,
    EMBALAGEM,
    TAMANHO,
    SABOR,
    PRECO_DE_LISTA
) VALUES (
	'5478542',
    'Videira do Campo - 1,5 Litros - Melância',
    'PET',
    '1,5 Litros',
    'Melância',
    19.51
);

# QUINTO PRODUTO

INSERT INTO PRODUTOS (
	PRODUTO,
    NOME,
    EMBALAGEM,
    TAMANHO,
    SABOR,
    PRECO_DE_LISTA
) VALUES (
	'544931',
    'Frescor do Verão - 350 ml - Limão',
    'PET',
    '350 ml',
    'Limão'
    ,3.20
);

# SEXTO PRODUTO

INSERT INTO PRODUTOS (
	PRODUTO,
    NOME,
    EMBALAGEM,
    TAMANHO,
    SABOR,
    PRECO_DE_LISTA
) VALUES (
	'1078680',
	'Frescor do Verão - 470 ml - Manga',
	'Lata',
	'470 ml',
	'Manga',
	5.18
);

# VISUALIZANDO A TABELA
SELECT * FROM PRODUTOS;
