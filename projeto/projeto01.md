## PROJETO 01 - INSPAÇÃO DE NAVIOS

### Descrição

[ MINHA DESCRIÇÃO] 

### Especificações

#### Tabela:

##### public."cp02Navios"

|       Coluna       | Tipo         | Chave_primaria | Chave_estrangeira |
| :-----------------: | ------------ | :------------: | ----------------- |
|         id         | bigint       |       X       |                   |
|     nome_navio     | varchar(50)  |                |                   |
|       mes_ano       | varchar(10)  |                |                   |
| classificacao_risco | varchar(15)  |                |                   |
| indice_conformidade | double       |                |                   |
|   pontuacao_risco   | int          |                |                   |
|      temporada      | varchar(200) |                |                   |

### Questões

#### 1 - Quais embarcações possuem pontuação de risco igual a 310?

```sql
SELECT 
	*
FROM 
	public."cp02Navios"
WHERE 
	pontuacao_risco = 310
```

#### 2 - Quais embarcações têm classificação de risco A e índice de conformidade maior ou igual a 95%?

```sql
SELECT 
	* 
FROM 
	public."cp02Navios" 
WHERE 
	classificacao_risco='A' AND
	indice_conformidade >= 95
```

#### 3-Quais embarcações têmclassificação de risco C ou D e índice de conformidade menor ou igual a 95%?

```sql
SELECT 
	* 
FROM 
	public."cp02Navios" 
WHERE 
	classificacao_risco in ('C','D') AND
	indice_conformidade <= 95
```

#### 4 - Quais embarcações têm classificação de risco A ou pontuação de risco igual a 0?

```sql
SELECT 
	* 
FROM 
	public."cp02Navios" 
WHERE 
	classificacao_risco = 'A' OR
	pontuacao_risco = 0
```

#### 5 - [DESAFIO]Quais embarcações foram inspecionadas em Dezembro de 2016?

```sql
SELECT 
	* 
FROM 
	public."cp02Navios" 
WHERE 
	temporada like '%Dezembro 2016'
```
