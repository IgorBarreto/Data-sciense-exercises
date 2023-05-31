# Lista os pedidos
SELECT * FROM cap05.TB_PEDIDOS;

# Soma (total) do valor dos pedidos
SELECT SUM(valor_pedido) AS total
FROM cap05.TB_PEDIDOS;

# Soma (total) do valor dos pedidos por cidade
SELECT SUM(valor_pedido) AS total, cidade_cliente
FROM cap05.TB_PEDIDOS P, cap05.TB_CLIENTES C
WHERE P.id_cliente = C.id_cliente
GROUP BY cidade_cliente;

# Insere mais 2 clientes
INSERT INTO `cap05`.`TB_CLIENTES` (`id_cliente`, `nome_cliente`, `endereco_cliente`, `cidade_cliente`, `estado_cliente`)
VALUES (12, "Bill Gates", "Rua 14", "Santos", "SP");

INSERT INTO `cap05`.`TB_CLIENTES` (`id_cliente`, `nome_cliente`, `endereco_cliente`, `cidade_cliente`, `estado_cliente`)
VALUES (13, "Jeff Bezos", "Rua 29", "Osasco", "SP");

# Insere mais 3 pedidos
INSERT INTO `cap05`.`TB_PEDIDOS` (`id_pedido`, `id_cliente`, `id_vendedor`, `data_pedido`, `id_entrega`, `valor_pedido`)
VALUES (1016, 11, 5, now(), 27, 234.09);

INSERT INTO `cap05`.`TB_PEDIDOS` (`id_pedido`, `id_cliente`, `id_vendedor`, `data_pedido`, `id_entrega`, `valor_pedido`)
VALUES (1017, 12, 4, now(), 22, 678.30);

INSERT INTO `cap05`.`TB_PEDIDOS` (`id_pedido`, `id_cliente`, `id_vendedor`, `data_pedido`, `id_entrega`, `valor_pedido`)
VALUES (1018, 13, 4, now(), 22, 978.30);

# Soma (total) do valor dos pedidos por cidade
SELECT SUM(valor_pedido) AS total, cidade_cliente
FROM cap05.TB_PEDIDOS P, cap05.TB_CLIENTES C
WHERE P.id_cliente = C.id_cliente
GROUP BY cidade_cliente;

# Soma (total) do valor dos pedidos por estado
SELECT SUM(valor_pedido) AS total, estado_cliente
FROM cap05.TB_PEDIDOS P, cap05.TB_CLIENTES C
WHERE P.id_cliente = C.id_cliente
GROUP BY estado_cliente;

# Soma (total) do valor dos pedidos por cidade e estado (query incorreta)
SELECT SUM(valor_pedido) AS total, cidade_cliente, estado_cliente
FROM cap05.TB_PEDIDOS P, cap05.TB_CLIENTES C
WHERE P.id_cliente = C.id_cliente
GROUP BY estado_cliente;

# Soma (total) do valor dos pedidos por cidade e estado (query correta)
SELECT SUM(valor_pedido) AS total, cidade_cliente, estado_cliente
FROM cap05.TB_PEDIDOS P, cap05.TB_CLIENTES C
WHERE P.id_cliente = C.id_cliente
GROUP BY cidade_cliente, estado_cliente
ORDER BY estado_cliente;

# Insere mais 2 clientes
INSERT INTO `cap05`.`TB_CLIENTES` (`id_cliente`, `nome_cliente`, `endereco_cliente`, `cidade_cliente`, `estado_cliente`)
VALUES (14, "Melinda Gates", "Rua 14", "Barueri", "SP");

INSERT INTO `cap05`.`TB_CLIENTES` (`id_cliente`, `nome_cliente`, `endereco_cliente`, `cidade_cliente`, `estado_cliente`)
VALUES (15, "Barack Obama", "Rua 29", "Barueri", "SP");

# Soma(total) do valor dos pedidos por cidade e estado com RIGHT JOIN e CASE
SELECT 
	CASE 
		WHEN FLOOR(SUM(valor_pedido)) IS NULL THEN 0
		ELSE FLOOR(SUM(valor_pedido))
	end AS total, 
	cidade_cliente, 
	estado_cliente
FROM cap05.TB_PEDIDOS P RIGHT JOIN cap05.TB_CLIENTES C
ON P.id_cliente = C.id_cliente
GROUP BY cidade_cliente, estado_cliente
ORDER BY total DESC;

# Supondo que a comissão de cada vendedor seja de 10%, quanto cada vendedor ganhou de comissão nas vendas no estado do Ceará?
# Retorne 0 se não houve ganho de comissão

# Soma (total) do valor dos pedidos por cidade e estado (query correta)
SELECT SUM(valor_pedido * 0.10) AS comissao, nome_vendedor, estado_cliente
FROM cap05.TB_PEDIDOS P, cap05.TB_CLIENTES C, cap05.TB_VENDEDOR V
WHERE P.id_cliente = C.id_cliente
AND P.id_vendedor = V.id_vendedor
AND estado_cliente = 'CE'
GROUP BY nome_vendedor, estado_cliente
ORDER BY estado_cliente;

SELECT SUM(valor_pedido * 0.10) AS comissao, nome_vendedor, estado_cliente
FROM cap05.TB_PEDIDOS P INNER JOIN cap05.TB_CLIENTES C RIGHT JOIN cap05.TB_VENDEDOR V
ON P.id_cliente = C.id_cliente
AND P.id_vendedor = V.id_vendedor
AND estado_cliente = 'CE'
GROUP BY nome_vendedor, estado_cliente
ORDER BY estado_cliente;

# Soma (total) do valor dos pedidos por cidade e estado (query correta)
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
FROM cap05.TB_PEDIDOS P INNER JOIN cap05.TB_CLIENTES C RIGHT JOIN cap05.TB_VENDEDOR V
ON P.id_cliente = C.id_cliente
AND P.id_vendedor = V.id_vendedor
AND estado_cliente = 'CE'
GROUP BY nome_vendedor, estado_cliente
ORDER BY estado_cliente;





