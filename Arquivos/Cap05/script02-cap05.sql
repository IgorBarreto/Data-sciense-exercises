# Lista os pedidos
SELECT * FROM cap05.TB_PEDIDOS;

# Média do valor dos pedidos
SELECT AVG(valor_pedido) AS media
FROM cap05.TB_PEDIDOS;

# Média do valor dos pedidos por cidade
SELECT AVG(valor_pedido) AS media, cidade_cliente
FROM cap05.TB_PEDIDOS P, cap05.TB_CLIENTES C
WHERE P.id_cliente = C.id_cliente
GROUP BY cidade_cliente;

# Média do valor dos pedidos por cidade arredondando a média
SELECT ROUND(AVG(valor_pedido),2) AS media, cidade_cliente
FROM cap05.TB_PEDIDOS P, cap05.TB_CLIENTES C
WHERE P.id_cliente = C.id_cliente
GROUP BY cidade_cliente;

# Média do valor dos pedidos por cidade
SELECT ROUND(AVG(valor_pedido),2) AS media, cidade_cliente
FROM cap05.TB_PEDIDOS P, cap05.TB_CLIENTES C
WHERE P.id_cliente = C.id_cliente
GROUP BY cidade_cliente
ORDER BY media DESC;

# Média do valor dos pedidos por cidade com INNER JOIN
SELECT ROUND(AVG(valor_pedido),2) AS media, cidade_cliente
FROM cap05.TB_PEDIDOS P INNER JOIN cap05.TB_CLIENTES C
ON P.id_cliente = C.id_cliente
GROUP BY cidade_cliente
ORDER BY media DESC;

# Insere um novo registro na tabela de clientes
INSERT INTO `cap05`.`TB_CLIENTES` (`id_cliente`, `nome_cliente`, `endereco_cliente`, `cidade_cliente`, `estado_cliente`)
VALUES (11, "Michael Jordan", "Rua 21", "Palmas", "TO");

# Média do valor dos pedidos por cidade com INNER JOIN
SELECT ROUND(AVG(valor_pedido),2) AS media, cidade_cliente
FROM cap05.TB_PEDIDOS P INNER JOIN cap05.TB_CLIENTES C
ON P.id_cliente = C.id_cliente
GROUP BY cidade_cliente
ORDER BY media DESC;

# Média do valor dos pedidos por cidade com RIGHT JOIN
SELECT ROUND(AVG(valor_pedido),2) AS media, cidade_cliente
FROM cap05.TB_PEDIDOS P RIGHT JOIN cap05.TB_CLIENTES C
ON P.id_cliente = C.id_cliente
GROUP BY cidade_cliente
ORDER BY media DESC;

# Média do valor dos pedidos por cidade com RIGHT JOIN e CASE
SELECT 
	CASE 
		WHEN ROUND(AVG(valor_pedido),2) IS NULL THEN 0
		ELSE ROUND(AVG(valor_pedido),2)
	end AS media, 
	cidade_cliente
FROM cap05.TB_PEDIDOS P RIGHT JOIN cap05.TB_CLIENTES C
ON P.id_cliente = C.id_cliente
GROUP BY cidade_cliente
ORDER BY media DESC;

