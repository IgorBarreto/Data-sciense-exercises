# Junção de Tabelas


# Vamos inserir um registro na tabela de pedidos que será "órfão" e queremos retornar todos os dados de ambas as tabelas mesmo sem correspondência
INSERT INTO `cap04`.`TB_PEDIDOS` (`id_pedido`, `id_cliente`, `id_vendedor`, `data_pedido`, `id_entrega`)
VALUES (1004, 10, 6, now(), 23);


# Left Join
SELECT C.nome_cliente, P.id_pedido
FROM cap04.TB_CLIENTES as C 
LEFT OUTER JOIN cap04.TB_PEDIDOS AS P 
ON C.id_cliente = P.id_cliente;


# Right Join
SELECT C.nome_cliente, P.id_pedido
FROM cap04.TB_CLIENTES as C 
RIGHT OUTER JOIN cap04.TB_PEDIDOS AS P 
ON C.id_cliente = P.id_cliente;


# Full Outer Join (alguns SGBDs não implementam essa junção)
SELECT C.nome_cliente, P.id_pedido
FROM cap04.TB_CLIENTES as C 
FULL OUTER JOIN cap04.TB_PEDIDOS AS P 
ON C.id_cliente = P.id_cliente;


# Resolvemos o problema com o UNION e UNION ALL

# UNION
SELECT C.nome_cliente, P.id_pedido
FROM cap04.TB_CLIENTES as C 
LEFT OUTER JOIN cap04.TB_PEDIDOS AS P 
ON C.id_cliente = P.id_cliente
UNION
SELECT C.nome_cliente, P.id_pedido
FROM cap04.TB_CLIENTES as C 
RIGHT OUTER JOIN cap04.TB_PEDIDOS AS P 
ON C.id_cliente = P.id_cliente;


# UNION ALL
SELECT C.nome_cliente, P.id_pedido
FROM cap04.TB_CLIENTES as C 
LEFT OUTER JOIN cap04.TB_PEDIDOS AS P 
ON C.id_cliente = P.id_cliente
UNION ALL
SELECT C.nome_cliente, P.id_pedido
FROM cap04.TB_CLIENTES as C 
RIGHT OUTER JOIN cap04.TB_PEDIDOS AS P 
ON C.id_cliente = P.id_cliente;


# Inserir mais um registro na tabela de clientes
INSERT INTO `cap04`.`TB_CLIENTES` (`id_cliente`, `nome_cliente`, `endereco_cliente`, `cidade_cliente`, `estado_cliente`)
VALUES (6, "Madona", "Rua 45", "Campos", "RJ");


# Retornar clientes que sejam da mesma cidade


# Self Join
SELECT A.nome_cliente, A.cidade_cliente
FROM cap04.TB_CLIENTES A, cap04.TB_CLIENTES B
WHERE A.id_cliente <> B.id_cliente
AND A.cidade_cliente = B.cidade_cliente;


# Retornar todos os dados de todas as tabelas


# CROSS JOIN
SELECT C.nome_cliente, P.id_pedido
FROM cap04.TB_CLIENTES AS C
CROSS JOIN cap04.TB_PEDIDOS AS P;


# CROSS JOIN
SELECT P.id_pedido, C.nome_cliente
FROM cap04.TB_PEDIDOS AS P, cap04.TB_CLIENTES AS C;


# CROSS JOIN com WHERE tem o mesmo comportamento do INNER JOIN
SELECT C.nome_cliente, P.id_pedido
FROM cap04.TB_CLIENTES AS C
CROSS JOIN cap04.TB_PEDIDOS AS P
WHERE C.id_cliente = P.id_cliente;




