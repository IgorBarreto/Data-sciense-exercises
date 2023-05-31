# Lista os clientes
SELECT * FROM cap05.TB_CLIENTES;

# Contagem de clientes por cidade (query incorreta)
SELECT COUNT(id_cliente), cidade_cliente
FROM cap05.TB_CLIENTES;

# Contagem de clientes por cidade (query correta)
SELECT COUNT(id_cliente), cidade_cliente
FROM cap05.TB_CLIENTES
GROUP BY cidade_cliente;

# Contagem de clientes por cidade ordenado pela contagem
SELECT COUNT(id_cliente), cidade_cliente
FROM cap05.TB_CLIENTES
GROUP BY cidade_cliente
ORDER BY COUNT(id_cliente) DESC;

# Contagem de clientes por cidade ordenado pela contagem
SELECT COUNT(id_cliente) AS contagem, cidade_cliente
FROM cap05.TB_CLIENTES
GROUP BY cidade_cliente
ORDER BY contagem DESC;