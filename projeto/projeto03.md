## PROJETO 03 - ANALIZE DE PEDIDOS

### Especificacçõs

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

|   Coluna   | Tipo | Chave_primaria | Chave_estrangeira |
| :---------: | ---- | :------------: | :---------------: |
|  id_pedido  |      |       X       |                  |
| id_cliente |      |                |         X         |
| id_vendedor |      |                |         X         |
| data_pedido |      |                |                  |
| id_entrega |      |                |                  |

### Questões

#### 1 - Retornar id do pedido e nome do cliente.

```sql
SELECT
	p.id_pedido as id,c.nome_cliente as nome_cliente
FROM
	"cp04Pedidos" as p, "cp04Clientes" as c
WHERE 
	c.id = p.id_cliente_id ORDER BY p.id_pedido
-- OR
SELECT
	p.id_pedido as id_pedido,c.nome_cliente as nome_cliente
FROM
	"cp04Pedidos" as p
INNER JOIN "cp04Clientes" AS C ON c.id_cliente = p.id_cliente_id::integer

```

#### 2 - Retornar id do pedido, nome do cliente e nome do vendedor.

```sql
SELECT
            p.id_pedido as id_pedido,
            c.nome_cliente as nome_cliente,
            v.nome_vendedor as nome_vendedor
        FROM
            "cp04Pedidos" as p
        INNER JOIN
            "cp04Clientes" AS c ON c.id_cliente = p.id_cliente_id::integer
        INNER JOIN
            "cp04Vendedores" AS v ON v.id_vendedor = p.id_cliente_id::integer
```

#### 3 - Retornar todos os clientes, com o	u sem pedido associado (usando Left Join).

```sql
SELECT
	p.id_pedido as id_pedido,
        c.nome_cliente as nome_cliente
FROM
	"cp04Clientes" as c
LEFT JOIN
	"cp04Pedidos" as p
ON
	c.id_cliente = p.id_cliente_id
ORDER BY
	p.id_pedido
```

#### 4 -  Retornar todos os clientes, com ou sem pedido associado (usando Right Join)

```sql
SELECT
	p.id_pedido as id_pedido,
        c.nome_cliente as nome_cliente
FROM
	"cp04Pedidos" as p
RIGHT JOIN
	"cp04Clientes" as c
ON
	c.id_cliente = p.id_cliente_id
ORDER BY
	p.id_pedido
```

#### 5 -  Retornar a data do pedido, o nome do cliente, todos os vendedores, com ou sem pedido associado, e ordenar o resultado pelo nome do cliente.

```sql
SELECT
                p.id_pedido as id_pedido,
                p.data_pedido AS data_pedido,
                c.nome_cliente AS nome_cliente,
                v.nome_vendedor AS nome_vendedor
            FROM
                "cp04Pedidos" as p
            INNER JOIN "cp04Clientes" as c
            ON
                c.id_cliente = p.id_cliente_id
            RIGHT JOIN "cp04Vendedores" as v
            ON
                v.id_vendedor = p.id_vendedor_id
            ORDER BY
                c.nome_cliente
```

#### 6 -	Retornar clientes que sejam da mesma cidade

```sql
SELECT
	C1.id_cliente,
        C1.nome_cliente,
        C1.cidade_cliente
FROM
        "cp04Clientes" as C1,
        "cp04Clientes" as C2
WHERE
        C1.cidade_cliente = C2.cidade_cliente AND
        C1.id_cliente <> C2.id_cliente
```

#### 7 - Retornar todos os dados de todas as tabelas (CROS JOIN)

```sql
SELECT 
	C.nome_cliente, P.id_pedido
FROM 
	"cp04Clientes" AS C
CROSS JOIN 
	"cap04Pedidos" AS P;
-- OR
SELECT 
	C.nome_cliente, P.id_pedido
FROM 
	"cp04Clientes" AS C,
	"cap04Pedidos" AS P;

```
