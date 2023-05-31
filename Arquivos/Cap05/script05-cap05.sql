# Algum vendedor participou de vendas cujo valor pedido tenha sido superior a 600 no estado de SP?

SELECT nome_cliente, cidade_cliente, valor_pedido, nome_vendedor
FROM cap05.TB_PEDIDOS P INNER JOIN cap05.TB_CLIENTES C INNER JOIN cap05.TB_VENDEDOR V
ON P.id_cliente = C.id_cliente
AND P.id_vendedor = V.id_vendedor
AND estado_cliente = 'SP'
AND valor_pedido > 600;


# Algum vendedor participou de vendas em que a média do valor_pedido por estado do cliente foi superior a 800?

SELECT estado_cliente, CEILING(AVG(valor_pedido)) AS media
FROM cap05.TB_PEDIDOS P INNER JOIN cap05.TB_CLIENTES C 
ON P.id_cliente = C.id_cliente
GROUP BY estado_cliente;

SELECT estado_cliente, nome_vendedor, CEILING(AVG(valor_pedido)) AS media
FROM cap05.TB_PEDIDOS P INNER JOIN cap05.TB_CLIENTES C INNER JOIN cap05.TB_VENDEDOR V
ON P.id_cliente = C.id_cliente
AND P.id_vendedor = V.id_vendedor
GROUP BY estado_cliente, nome_vendedor
ORDER BY nome_vendedor;

SELECT estado_cliente, nome_vendedor, CEILING(AVG(valor_pedido)) AS media
FROM cap05.TB_PEDIDOS P INNER JOIN cap05.TB_CLIENTES C INNER JOIN cap05.TB_VENDEDOR V
ON P.id_cliente = C.id_cliente
AND P.id_vendedor = V.id_vendedor
AND media > 800
GROUP BY estado_cliente, nome_vendedor
ORDER BY nome_vendedor;

SELECT estado_cliente, nome_vendedor, CEILING(AVG(valor_pedido)) AS media
FROM cap05.TB_PEDIDOS P INNER JOIN cap05.TB_CLIENTES C INNER JOIN cap05.TB_VENDEDOR V
ON P.id_cliente = C.id_cliente
AND P.id_vendedor = V.id_vendedor
GROUP BY estado_cliente, nome_vendedor
HAVING media > 800
ORDER BY nome_vendedor;


# Qual estado teve mais de 5 pedidos?

SELECT estado_cliente, (COUNT(id_pedido)) AS contagem
FROM cap05.TB_PEDIDOS P INNER JOIN cap05.TB_CLIENTES C 
ON P.id_cliente = C.id_cliente
GROUP BY estado_cliente
ORDER BY contagem DESC;

SELECT estado_cliente, (COUNT(id_pedido)) AS contagem
FROM cap05.TB_PEDIDOS P INNER JOIN cap05.TB_CLIENTES C 
ON P.id_cliente = C.id_cliente
AND contagem > 5
GROUP BY estado_cliente
ORDER BY contagem DESC;

SELECT estado_cliente, (COUNT(id_pedido)) AS contagem
FROM cap05.TB_PEDIDOS P INNER JOIN cap05.TB_CLIENTES C 
ON P.id_cliente = C.id_cliente
GROUP BY estado_cliente
HAVING contagem > 5
ORDER BY contagem DESC;
