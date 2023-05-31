## PROJETO 05 - VENDAS(AGREGAÇÃO)

### Expecificicações

#### Tabelas:

##### Cliente

| Coluna           | Tipo        | Chave_primaria | Chave_estrangeira |
| ---------------- | ----------- | :------------: | ----------------- |
| id_cliente       | integer     |       X       |                   |
| nome_cliente     | varchar(50) |                |                   |
| endereco_cliente | varchar(50) |                |                   |
| cidade_cliente   | varchar(50) |                |                   |
| estado_cliente   | varchar(50) |                |                   |

##### Vendedor

| Coluna        | Tipo        | Chave_primaria | Chave_estrangeira |
| ------------- | ----------- | :------------: | ----------------- |
| id_vendedor   | integer     |       X       |                   |
| nome_vendedor | varchar(50) |                |                   |

##### Pedido

|    Coluna    | Tipo    | Chave_primaria | Chave_estrangeira |
| :----------: | ------- | :------------: | :---------------: |
|  id_pedido  | integer |       X       |                  |
|  id_cliente  | integer |                |         X         |
| id_vendedor | integer |                |         X         |
| data_pedido | integer |                |                  |
|  id_entrega  | integer |                |                  |
| valor_pedido | decimal |                |                  |

##### Vendas

|   coluna   | tipo    |
| :---------: | ------- |
|     ano     | varchar |
|    pais    | varchar |
|   produto   | varchar |
| faturamento | integer |

### Questões

#### 1- Quantidade de clientes por cidade

```sql
SELECT
	count (*) as quantidade,
        cidade_cliente as cidade
FROM "cp05Clientes"
GROUP BY cidade_cliente
```

#### 2- Média do valor dos pedidos

```sql
SELECT
	1 AS id ,AVG(valor_pedido) AS media
FROM "cp05Pedidos" 
```

#### 3- Média do valor dos pedidos por cidade

```sql
 SELECT
	AVG(P.valor_pedido) as media
	,C.cidade_cliente
	FROM "cp05Pedidos" AS P, "cp05Clientes" AS C
WHERE 
	C.id_cliente = P.id_cliente
GROUP BY C.cidade_cliente
```

#### 3- Média do valor dos pedidos por cidade incluindo cidades sem pedidos

```sql
SELECT
	1 AS id,
        CASE
        	WHEN AVG(P.valor_pedido) IS NULL THEN 0
                ELSE AVG(P.valor_pedido)
	END AS media,
        C.cidade_cliente AS cidade
FROM "cp05Pedidos" AS P
RIGHT JOIN "cp05Clientes" AS C ON C.id_cliente = P.id_cliente
GROUP BY cidade_cliente
ORDER BY AVG(P.valor_pedido) DESC
```

#### 4- Soma do valor dos pedidos por cidade

```sql
SELECT
	1 AS id,
        CASE
        	WHEN SUM(P.valor_pedido) IS NULL THEN 0
                ELSE AVG(P.valor_pedido)
	END AS media,
        C.cidade_cliente AS cidade
FROM "cp05Pedidos" AS P
RIGHT JOIN "cp05Clientes" AS C ON C.id_cliente = P.id_cliente
GROUP BY cidade_cliente
ORDER BY AVG(P.valor_pedido) DESC
```

#### 4- Soma do valor dos pedidos por cidade e estado

```sql
SELECT
	1 AS id,
        CASE
        	WHEN SUM(P.valor_pedido) IS NULL THEN 0
                ELSE AVG(P.valor_pedido)
	END AS media,
        C.cidade_cliente AS cidade,
		C.estado_cliente AS estado
FROM "cp05Pedidos" AS P
RIGHT JOIN "cp05Clientes" AS C ON C.id_cliente = P.id_cliente
GROUP BY cidade_cliente,C.estado_cliente
ORDER BY C.estado_cliente DESC
```

#### 4- Supondo que a comissão de cada vendedor seja de 10%, quanto cada vendedor ganhou de comissão nas vendas do estado do Cerá? (Retorne 0 se não houver gasto de comissão)

```sql
SELECT 
	CASE 
		WHEN ROUND(SUM(valor_pedido * 0.10),2) IS NULL THEN 0
		ELSE ROUND(SUM(valor_pedido * 0.10),2)
	end AS comissao, 
    nome_vendedor,
    CASE 
		WHEN estado_cliente IS NULL THEN 'Não Atua no CE'
		ELSE estado_cliente
	end AS estado_cliente
FROM "cp05Pedidos" P INNER JOIN "cp05Clientes" C RIGHT JOIN "cp05Vendedores" V
ON P.id_cliente = C.id_cliente
AND P.id_vendedor = V.id_vendedor
AND estado_cliente = 'CE'
GROUP BY nome_vendedor, estado_cliente
ORDER BY estado_cliente;
```

#### 5- Maior valor

```
SELECT
	MAX(valor_pedido) as maximo
	MIN(valor_pedido) as minimo
 FROM "cp05Pedidos"
```

#### 6- Algum vendedor participou de vendas cujo valor pedido tenha sido superior a 600 no estado de SP

```
SELECT 
    id_pedido,nome_vendedor
FROM "cp05Pedidos" P 
INNER JOIN "cp05Clientes" C
ON c.id_cliente = P.id_cliente
INNER JOIN "cp05Vendedores" V
ON P.id_vendedor = V.id_vendedor
WHERE estado_cliente= 'SP' AND
valor_pedido >600
```

#### 7- Algum vendedor participou de vendas em que a media do valor do pedido por estado do cliente foi superior a 800

```
SELECT
    estado_cliente,
    nome_vendedor,
    ceiling(avg(valor_pedido)) as media
FROM "cp05Pedidos" P
INNER JOIN "cp05Clientes" C ON c.id_cliente = P.id_cliente
INNER JOIN "cp05Vendedores" V ON P.id_vendedor = V.id_vendedor
GROUP BY estado_cliente,nome_vendedor
HAVING avg(valor_pedido) >800
```

#### 8-  Faturamento total por ano

```
SELECT 
    ano, sum(faturamento) faturamento
FROM "cp05Vendas"
GROUP BY ano
```

#### 9- Qual o faturamento total por ano e total?

```sql
SELECT 
    ano, sum(faturamento) faturamento
FROM "cp05Vendas"
GROUP BY ROLLUP(ano)
ORDER BY ano;
```

#### 10- Qual o faturamento total por ano e total maior que 13000?

```sql
SELECT 
    ano, sum(faturamento) faturamento
FROM "cp05Vendas"
GROUP BY ROLLUP(ano)
HAVING sum(faturamento)  >13000
ORDER BY ano;

```

#### 11- Faturamento total por ano e pais e total geral

```sql
SELECT 
    ano,pais, sum(faturamento) faturamento
FROM "cp05Vendas"
GROUP BY ROLLUP(ano,pais)
ORDER BY ano,pais;
```

#### 12- Faturamento total por ano e produto e total geral

```sql
SELECT 
    ano,produto, sum(faturamento) faturamento
FROM "cp05Vendas"
GROUP BY ROLLUP(ano,produto)
ORDER BY ano,produto;
```

#### 13- Faturamento total por ano e produto e total geral, ordenando pelo agrupamento de produto

```sql
SELECT 
    ano,produto,
    SUM(faturamento)
FROM "cp05Vendas"
GROUP BY ROLLUP(ano,produto)
ORDER BY 		(produto) DESC
```

#### 14- Faturamento total por ano e produto e total geral, ordenando pelo agrupamento de produto

```sql
SELECT
	IF(GROUPING(ano),'Total de Todos os Anos') AS ano,
	IF(GROUPING(pais),'Total de Todos os Anos') AS pais,
	IF(GROUPING(produto),'Total de Todos os Anos') AS produto,
	SUM(faturamento) faturamento 
FROM "cp05Vendas"
GROUP BY ROLLUP(ano,pais,produto);
```
