# Cria tabela
CREATE TABLE `cap05`.`TB_VENDAS` (
  `ano` INT NULL,
  `pais` VARCHAR(45) NULL,
  `produto` VARCHAR(45) NULL,
  `faturamento` INT NULL);


# Insere registros
INSERT INTO `cap05`.`TB_VENDAS` (`ano`, `pais`, `produto`, `faturamento`)
VALUE (2021, 'Brasil', 'Geladeira', 1130);

INSERT INTO `cap05`.`TB_VENDAS` (`ano`, `pais`, `produto`, `faturamento`)
VALUE (2021, 'Brasil', 'TV', 980);

INSERT INTO `cap05`.`TB_VENDAS` (`ano`, `pais`, `produto`, `faturamento`)
VALUE (2021, 'Argentina', 'Geladeira', 2180);

INSERT INTO `cap05`.`TB_VENDAS` (`ano`, `pais`, `produto`, `faturamento`)
VALUE (2021, 'Argentina', 'TV', 2240);

INSERT INTO `cap05`.`TB_VENDAS` (`ano`, `pais`, `produto`, `faturamento`)
VALUE (2021, 'Portugal', 'Smartphone', 2310);

INSERT INTO `cap05`.`TB_VENDAS` (`ano`, `pais`, `produto`, `faturamento`)
VALUE (2021, 'Portugal', 'TV', 1900);

INSERT INTO `cap05`.`TB_VENDAS` (`ano`, `pais`, `produto`, `faturamento`)
VALUE (2021, 'Inglaterra', 'Notebook', 1800);

INSERT INTO `cap05`.`TB_VENDAS` (`ano`, `pais`, `produto`, `faturamento`)
VALUE (2022, 'Brasil', 'Geladeira', 1400);

INSERT INTO `cap05`.`TB_VENDAS` (`ano`, `pais`, `produto`, `faturamento`)
VALUE (2022, 'Brasil', 'TV', 1345);

INSERT INTO `cap05`.`TB_VENDAS` (`ano`, `pais`, `produto`, `faturamento`)
VALUE (2022, 'Argentina', 'Geladeira', 2180);

INSERT INTO `cap05`.`TB_VENDAS` (`ano`, `pais`, `produto`, `faturamento`)
VALUE (2022, 'Argentina', 'TV', 1390);

INSERT INTO `cap05`.`TB_VENDAS` (`ano`, `pais`, `produto`, `faturamento`)
VALUE (2022, 'Portugal', 'Smartphone', 2480);

INSERT INTO `cap05`.`TB_VENDAS` (`ano`, `pais`, `produto`, `faturamento`)
VALUE (2022, 'Portugal', 'TV', 1980);

INSERT INTO `cap05`.`TB_VENDAS` (`ano`, `pais`, `produto`, `faturamento`)
VALUE (2022, 'Inglaterra', 'Notebook', 2300);


# Lista os dados
SELECT * FROM cap05.TB_VENDAS;


# Faturamento total por ano
SELECT ano, SUM(faturamento) AS faturamento
FROM cap05.TB_VENDAS
GROUP BY ano;


# Faturamento total por ano a total geral
SELECT ano, SUM(faturamento) AS faturamento
FROM cap05.TB_VENDAS
GROUP BY ano WITH ROLLUP;


# Faturamento total por ano a total geral filtrando por faturamento
SELECT ano, SUM(faturamento) AS faturamento
FROM cap05.TB_VENDAS
GROUP BY ano WITH ROLLUP
HAVING faturamento > 13000;


# Faturamento total por ano a total geral ordernado por ano
SELECT ano, SUM(faturamento) AS faturamento
FROM cap05.TB_VENDAS
GROUP BY ano WITH ROLLUP
ORDER BY ano;


# Faturamento total por ano e país
SELECT ano, pais, SUM(faturamento) AS faturamento
FROM cap05.TB_VENDAS
GROUP BY ano, pais;


# Faturamento total por ano e país e total geral
SELECT ano, pais, SUM(faturamento) AS faturamento
FROM cap05.TB_VENDAS
GROUP BY ano, pais WITH ROLLUP;


# Faturamento total por ano e produto a total geral
SELECT ano, produto, SUM(faturamento) AS faturamento
FROM cap05.TB_VENDAS
GROUP BY ano, produto WITH ROLLUP


# Faturamento total por ano e produto a total geral, ordenado pelo agrupamento de produto
SELECT ano, produto, SUM(faturamento) AS faturamento
FROM cap05.TB_VENDAS
GROUP BY ano, produto WITH ROLLUP
ORDER BY GROUPING(produto) DESC;


# Por que não podemos usar o CASE na query acima?

# Faturamento total por ano e país e total geral com agrupamento do resultado
SELECT
	IF(GROUPING(ano), 'Total de Todos os Anos', ano) AS ano,
	IF(GROUPING(pais), 'Total de Todos os Países', pais) AS pais,
	IF(GROUPING(produto), 'Total de Todos os Produtos', produto) AS produto,
	SUM(faturamento) faturamento 
FROM cap05.TB_VENDAS
GROUP BY ano, pais, produto WITH ROLLUP;


# ROLLUP e CUBE tem o mesmo propósito, gerar grouping sets (conjuntos de grupos de dados). 

# ROLLUP faz isso através da hierarquia dos dados.
# CUBE gera todas as combinações possíveis.

# CUBE não é suportado no MySQL. Aqui há um bom material de referência:

https://www.sqltutorial.org/sql-cube/












