USE SUCOS;

# ATUALIZANDO UM PRODUTO DA TABELA
UPDATE PRODUTOS SET EMBALAGEM = 'Garrafa' WHERE PRODUTO = '544931';

# DELETANDO UM PRODUTO ESPECÍFICO DA TABELA
DELETE FROM PRODUTOS WHERE PRODUTO = '1078680';

# ADICIONANDO O CAMPO PRODUTO A CHAVE PRIMEIRA
ALTER TABLE PRODUTOS ADD PRIMARY KEY (PRODUTO);

# CRIANDO UM NOVO PRODUTO
INSERT INTO PRODUTOS(
	PRODUTO, NOME, EMBALAGEM, TAMANHO, SABOR, PRECO_DE_LISTA
) VALUES(
	'1078680', 'Videira Da Montanha - 350ml - Uva', 'Garrafa', '350 ml', 'Uva', 3.50
);

SELECT * FROM PRODUTOS;
