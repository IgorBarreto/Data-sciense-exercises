## PROJETO 06 - IFOOD

### Explicações

#### Tabelas:

##### Channels

| Coluna       | Tipo    | Chave_primaria | Chave_estrangeira |
| ------------ | ------- | :------------: | ----------------- |
| channel_id   | integer |       XC       |                   |
| channel_name | varchar |                |                   |
| channel_type | varchar |                |                   |

##### Deliveries

| Coluna                   | Tipo    | Chave_primaria | Chave_estrangeira |
| ------------------------ | ------- | :------------: | :---------------: |
| delivery_id              | integer |       X       |                  |
| delivery_order_id        | integer |                |         X         |
| driver_id                | integer |                |         X         |
| delivery_distance_meters | integer |                |                  |
| delivery_status          | varchar |                |                  |

##### Drivers

| Coluna       | Tipo    | Chave_primaria | Chave_estrangeira |
| ------------ | ------- | :------------: | ----------------- |
| driver_id    | integer |       X       |                   |
| driver_modal | varchar |                |                   |
| driver_type  | varchar |                |                   |

##### Hubs

| Coluna        | Tipo    | Chave_primaria | Chave_estrangeira |
| ------------- | ------- | :------------: | ----------------- |
| hub_id        | integer |       X       |                   |
| hub_name      | varchar |                |                   |
| hub_city      | varchar |                |                   |
| hub_state     | varchar |                |                   |
| hub_latitude  | decimal |                |                   |
| hub_longitude | decimal |                |                   |

##### Orders

| Coluna                            |   Tipo   | Chave_primaria | Chave_estrangeira |
| :-------------------------------- | :------: | :------------: | :---------------: |
| order_id                          | integer |       X       |                  |
| store_id                          | integer |                |         X         |
| channel_id                        | integer |                |         X         |
| payment_order_id                  | integer |                |         X         |
| delivery_order_id                 | integer |                |         X         |
| order_status                      | varchar |                |                  |
| order_amount                      | decimal |                |                  |
| order_delivery_fee                | decimal |                |                  |
| order_delivery_cost               | decimal |                |                  |
| order_created_hour                | integer |                |                  |
| order_created_minute              | integer |                |                  |
| order_created_day                 | integer |                |                  |
| order_created_month               | integer |                |                  |
| order_created_year                | integer |                |                  |
| order_moment_created              | datetime |                |                  |
| order_moment_accepted             | datetime |                |                  |
| order_moment_ready                | datetime |                |                  |
| order_moment_collected            | datetime |                |                  |
| order_moment_in_expedition        | datetime |                |                  |
| order_moment_delivered            | datetime |                |                  |
| order_moment_finished             | datetime |                |                  |
| order_metric_collected_time       | datetime |                |                  |
| order_metric_paused_time          | decimal |                |                  |
| order_metric_production_time      | decimal |                |                  |
| order_metric_walking_time         | decimal |                |                  |
| order_metric_expediton_speed_time | decimal |                |                  |
| order_metric_transit_time         | decimal |                |                  |
| order_metric_cycle_time           | decimal |                |                  |

##### Payment

| Coluna           | Tipo    | Chave_primaria | Chave_estrangeira |
| ---------------- | ------- | :------------: | :---------------: |
| payment_id       | integer |       X       |                  |
| payment_order_id | integer |                |         X         |
| payment_amount   | decimal |                |                  |
| payment_fee      | decimal |                |                  |
| payment_method   | varchar |                |                  |
| payment_status   | varchar |                |                  |

##### Store

| Coluna           | Tipo    | Chave_primaria | Chave_estrangeira |
| ---------------- | ------- | :------------: | :---------------: |
| store_id         | integer |       X       |                  |
| hub_id           | integer |                |         X         |
| store_name       | varchar |                |                  |
| store_segment    | varchar |                |                  |
| store_plan_price | decimal |                |                  |
| store_latitude   | integer |                |                  |
| store_longitude  | integer |                |                  |

### Questões

#### 1- Qual o número de hubs por cidade?

```sql
SELECT
	1 as hub_id,
	COUNT(*) AS total,
	hub_city AS cidade
FROM public."p06Hubs"
GROUP BY hub_city
ORDER BY total DESC
```

#### 2- Qual o número de pedidos (orders) por status?

```sql
SELECT
	1 AS order_id,
	count(*) AS total,
	order_status AS status
FROM public."p06Orders"
GROUP BY order_status
```

#### 3-  Qual o número de lojas (stores) por cidade dos hubs?

```sql
SELECT
	1 AS store_id
	count(store.store_id) AS total,
	hubs.hub_city AS cidade
FROM public."p06Stores" AS store
INNER JOIN public."p06Hubs" AS hubs 
on hubs.hub_id = store.hub_id
GROUP BY hubs.hub_city
ORDER BY total DESC
```

#### 4- Qual o menor e o maior valor de pagamento(payment_amount) registrado?

```sql
SELECT 
	1 AS payment_id,
	max(payment_amount) AS maior,
	min(payment_amount) AS menor
FROM public."p06Payments"
```

#### 5- Qual tipo de driver (driver_type) fez o maior número de entregas?

```sql
SELECT
	1 as driver_id,
	count(driver.driver_id) as total,
	driver.driver_type as driver_type
FROM public."p06Drivers" AS driver
INNER JOIN public."p06Deliveries" AS delivery
ON delivery.driver_id = driver.driver_id
GROUP BY driver.driver_type 
```

#### 6- Qual a distância média das entregas por tipo de driver (driver_modal)?

```sql
SELECT 
	1 AS driver_id,
	dr.driver_modal AS modal,
	avg(de.delivery_distance_meters) as media
FROM public."p06Drivers" AS dr
INNER JOIN public."p06Deliveries" AS de
ON dr.driver_id = de.driver_id
GROUP BY dr.driver_modal 
```

#### 7- Qual a média de valor de pedido (order_amount) por loja, em ordem decrescente?

```sql
SELECT
	1 AS store_id,
	store.store_name AS name,
	AVG(o.order_amount) as media
FROM public."p06Orders" AS o
INNER JOIN public."p06Stores" AS store
ON store.store_id = o.store_id 
GROUP BY store.store_name 
ORDER BY media desc
```

#### 8- Existem pe	didos que não estão associados a lojas? Se caso positivo, quantos?

```sql
SELECT
	1 AS order_id,
	count(o.order_id) AS total,
	COALESCE(s.store_name,'Sem Loja') AS name
FROM public."p06Orders" AS o
LEFT JOIN public."p06Stores" AS s 
ON s.store_id = o.store_id
GROUP BY s.store_name
having  COUNT(o.order_id) =0
ORDER BY total DESC
```

#### 9- Qual o valor total de pedido (order_amount) no channel 'FOOD PLACE'?

```sql
SELECT
	1 as order_id,
	sum(order_amount) soma
FROM public."p06Orders" AS o
INNER JOIN public."p06Channels" c
ON c. channel_id = o.channel_id
WHERE c.channel_name = 'FOOD PLACE'
```

#### 10- Quantos pagamentos foram cancelados (chargeback)?

```sql
SELECT
	1 as payment_id,
	COUNT(payment_id) quantidade,
	payment_status AS status
FROM public."p06Payments"
WHERE payment_status = 'CHARGEBACK'
GROUP BY payment_status
```

#### 11- Qual foi o valor médio dos pagamentos cancelados (chargeback)?

```sql
SELECT
	1 as payment_id,
	AVG(payment_amount) quantidade,
	payment_status AS status
FROM public."p06Payments"
WHERE payment_status = 'CHARGEBACK'
GROUP BY payment_status
```

#### 12- Qual a média do valor de pagamento por método de pagamento (payment_method) em ordem decrescente?

```sql
SELECT
	1 AS payment_id,
	AVG(payment_amount) AS cashback_average,
	payment_method
FROM public."p06Payments"
GROUP BY payment_method
ORDER BY AVG(payment_amount) DESC
```

#### 13- Quais métodos de pagamento tiveram valor médio superior a 100?

```sql
SELECT
	1 AS payment_id,
	AVG(payment_amount) AS cashback_average,
	payment_method
FROM public."p06Payments"
GROUP BY payment_method
HAVING AVG(payment_amount) > 100
ORDER BY AVG(payment_amount) DESC
```

#### 14- Qual a média de valor de pedido (order_amount) por estado do hub (hub_state), segmento da loja (store_segment) e tipo de canal (channel_type)?

```sql
SELECT 
	1 AS order_id,
	AVG(o.order_amount) AS amount_average,
	h.hub_state AS state,
	s.store_segment AS segment,
	c.channel_type AS channel
FROM public."p06Orders" AS o 
INNER JOIN public."p06Stores" AS s ON s.store_id =o.store_id
INNER JOIN public."p06Hubs" AS h ON h.hub_id = s.hub_id
INNER JOIN public."p06Channels" AS c ON c.channel_id = o.channel_id
GROUP BY h.hub_state, s.store_segment, c.channel_type
ORDER BY state
```

#### 15- Qual estado do hub (hub_state), segmento da loja (store_segment) e tipo de canal(channel_type) teve média de valor de pedido (order_amount) maior que 450?

```sql
SELECT 
	1 AS order_id,
	AVG(o.order_amount) AS amount_average,
	h.hub_state AS state,
	s.store_segment AS segment,
	c.channel_type AS channel
FROM public."p06Orders" AS o 
INNER JOIN public."p06Stores" AS s ON s.store_id =o.store_id
INNER JOIN public."p06Hubs" AS h ON h.hub_id = s.hub_id
INNER JOIN public."p06Channels" AS c ON c.channel_id = o.channel_id
GROUP BY h.hub_state, s.store_segment, c.channel_type
HAVING AVG(o.order_amount) >450
ORDER BY state
```

#### 16- Qual o valor total de pedido (order_amount) por estado do hub (hub_state),segmento da loja (store_segment) e tipo de  canal (channel_type)? Demonstre os totais intermediários e formate o resultado.

```sql
SELECT 
	1 AS order_id,
	COALESCE(h.hub_state,'Total hub state') AS state,
	COALESCE(s.store_segment,'Total Segmento') AS segment,
	COALESCE(c.channel_type,'Total Tipo de Canais') AS channel,
	SUM(o.order_amount) AS amount_average
FROM public."p06Orders" AS o 
INNER JOIN public."p06Stores" AS s ON s.store_id =o.store_id
INNER JOIN public."p06Hubs" AS h ON h.hub_id = s.hub_id
INNER JOIN public."p06Channels" AS c ON c.channel_id = o.channel_id
GROUP BY ROLLUP (h.hub_state, s.store_segment, c.channel_type)
ORDER BY AVG(order_amount)

```

#### 17- Quando  o  pedido  era  do  Hub  do  Rio  de  Janeiro  (hub_state),  segmento  de  loja 'FOOD',  tipo  de  canal  Marketplace  e  foi  cancelado,  qual  foi  a  média  de  valor  do  pedido (order_amount)?

```sql
SELECT 
	1 AS order_id,
	AVG(order_amount) AS amount_average,
	h.hub_state AS state,
	s.store_segment AS segment,
	c.channel_type AS channel
FROM public."p06Orders" AS o
INNER JOIN public."p06Stores" AS s
ON s.store_id =o.store_id
INNER JOIN public."p06Hubs" AS h
ON h.hub_id = s.hub_id
INNER JOIN public."p06Channels" AS c
ON c.channel_id = o.channel_id
GROUP BY ROLLUP
	(h.hub_state,
	s.store_segment,
	c.channel_type)
```

#### 18- Quando o pedido era do segmento de loja 'GOOD', tipo de canal Marketplace e foi cancelado, algum hub_state teve total de valor do pedido superior a 100.000?

```sql
SELECT 
	h.hub_state AS state
FROM public."p06Orders" AS o
INNER JOIN public."p06Stores" AS s
ON s.store_id =o.store_id
INNER JOIN public."p06Hubs" AS h
ON h.hub_id = s.hub_id
INNER JOIN public."p06Channels" AS c
ON c.channel_id = o.channel_id
WHERE s.store_segment = 'GOOD'
AND c.channel_type ='MARKETPLACE'
GROUP BY h.hub_state
HAVING AVG(o.order_amount) >100000
```

#### 19- Em que data houve a maior média de valor do pedido (order_amount)?  Dica: Pesquise e use a função SUBSTRING().

```sql

```

#### 20- Em quais datas o valor do pedido foi igual a zero (ou seja, não houve venda)? Dica: Use a função SUBSTRING().

```sql

```
