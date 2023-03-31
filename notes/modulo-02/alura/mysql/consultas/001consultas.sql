-- REVISANDO CONSULTAS

USE sucos_vendas;

SELECT * FROM tabela_de_clientes;

SELECT CPF, NOME, ESTADO FROM tabela_de_clientes;

SELECT CPF AS ID, NOME AS NAME, ESTADO AS UF FROM tabela_de_clientes;

SELECT * FROM tabela_de_produtos WHERE CODIGO_DO_PRODUTO = '1000889';

SELECT * FROM tabela_de_produtos WHERE SABOR = 'Laranja';

SELECT * FROM tabela_de_produtos WHERE EMBALAGEM = 'PeT';

-- CONSULTAS LÓGICAS

SELECT * FROM tabela_de_produtos WHERE SABOR = 'Manga' or SABOR = 'Laranja';

SELECT * FROM tabela_de_produtos WHERE SABOR = 'Manga' and EMBALAGEM = 'PET';

SELECT * FROM tabela_de_produtos WHERE SABOR = 'Manga' and PRECO_DE_LISTA < 10;

SELECT * FROM tabela_de_produtos WHERE NOT (SABOR = 'Manga');

SELECT * FROM tabela_de_produtos WHERE SABOR IN ('Laranja', 'Manga');

SELECT CPF, NOME, IDADE FROM tabela_de_clientes WHERE ESTADO IN ('SP', 'RJ') AND IDADE >= 18;

-- APLICANDO O LIKE

SELECT * FROM tabela_de_produtos WHERE SABOR LIKE '%Maça%';

SELECT CPF, NOME, IDADE FROM tabela_de_clientes WHERE NOME LIKE '%Carvalho%'

