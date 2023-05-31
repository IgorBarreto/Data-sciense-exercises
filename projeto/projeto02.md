## PROJETO 02 - CANCER DE MAMA

### Descrição

[MINHA DESCRIÇÃO]

### Especificações

#### Tabela:

##### public."cp03CancerMama"

|    Coluna    |  Tipo  | Chave_primaria | Chave_estrangeira |
| :-----------: | :-----: | :------------: | ----------------- |
|      id      | bigint |       X       |                   |
|    classe    | varchar |                |                   |
|     idade     | varchar |                |                   |
|   menopausa   | varchar |                |                   |
| tamanho_tumor | varchar |                |                   |
|   inv_nodes   | varchar |                |                   |
|   node_caps   | varchar |                |                   |
|   deg_malig   | integer |                |                   |
|     seio     | varchar |                |                   |
|   quadrante   | varchar |                |                   |
|  irradiando  | varchar |                |                   |

### Questões

#### 1 - Binarizando o campo classe

```sql
SELECT 
	CASE
		WHEN classe ='no-recurrence-events' THEN 0
		WHEN classe ='recurrence-events' THEN 1
	END as classe 
FROM
	public."cp03CancerMama"
```

#### 2 - Binarizando o campo irradiando

```sql
SELECT 
	CASE
		WHEN irradiando ='no' THEN 0
		WHEN irradiando ='yes' THEN 1
	END as irradiando
FROM
	public."cp03CancerMama"
```

#### 3 - Binarizando o campo node_caps

```sql
SELECT 
	CASE
		WHEN node_caps='no' THEN 0
		WHEN node_caps='yes' THEN 1
		WHEN node_caps='?' THEN 2
	END as node_caps
FROM
	public."cp03CancerMama"
```

#### 4 - Binarizando o campo seio

```sql
SELECT 
	CASE
		WHEN seio ='left' THEN 'E'
		WHEN seio ='right' THEN 'D'
	END as seio
FROM
	public."cp03CancerMama"
```

#### 5 - Binarizando o campo tamanho_tumor

```sql
SELECT 
	CASE
	 	WHEN tamanho_tumor = '0-4' or tamanho_tumor = '5-9' THEN 'Muito Pequeno'
          	WHEN tamanho_tumor = '10-14' or tamanho_tumor = '15-19' THEN 'Pequeno'
         	WHEN tamanho_tumor = '20-24' or tamanho_tumor = '25-29' THEN 'Médio'
         	WHEN tamanho_tumor = '30-34' or tamanho_tumor = '35-39' THEN  'Grande'
         	WHEN tamanho_tumor = '40-44' or tamanho_tumor = '45-49' THEN 'Muito Grande'
         	WHEN tamanho_tumor = '50-54' or tamanho_tumor = '55-59' THEN 'Tratamento Urgente'
	END AS tamanho_tumoro
FROM
	public."cp03CancerMama"
```

#### 6 - Binarizando o campo quadrante

```sql
SELECT 
	CASE
		WHEN quadrante = 'left_low' THEN 1
		WHEN quadrante = 'right_up' THEN 2
        	WHEN quadrante = 'left_up' THEN 3
        	WHEN quadrante = 'right_low' THEN 4
        	WHEN quadrante = 'central' THEN 5
        	ELSE 0
	END AS quadrante
FROM
	public."cp03CancerMama"
```

#### 7 - Gerando um novo dataset

```sql
CREATE TABLE IF NOT EXIST  public"cp03CancerMamaNovoDataset" 
AS 
SELECT
	id,
	idade,
	menopausa,
	inv_nodes,
	deg_malig
	CASE
		WHEN quadrante = 'left_low' THEN 1
		WHEN quadrante = 'right_up' THEN 2
        	WHEN quadrante = 'left_up' THEN 3
        	WHEN quadrante = 'right_low' THEN 4
        	WHEN quadrante = 'central' THEN 5
        	ELSE 0
	END AS quadrante,
	CASE
	 	WHEN tamanho_tumor = '0-4' or tamanho_tumor = '5-9' THEN 'Muito Pequeno'
          	WHEN tamanho_tumor = '10-14' or tamanho_tumor = '15-19' THEN 'Pequeno'
         	WHEN tamanho_tumor = '20-24' or tamanho_tumor = '25-29' THEN 'Médio'
         	WHEN tamanho_tumor = '30-34' or tamanho_tumor = '35-39' THEN  'Grande'
         	WHEN tamanho_tumor = '40-44' or tamanho_tumor = '45-49' THEN 'Muito Grande'
         	WHEN tamanho_tumor = '50-54' or tamanho_tumor = '55-59' THEN 'Tratamento Urgente'
	END AS tamanho_tumoro,
	CASE
		WHEN seio ='left' THEN 'E'
		WHEN seio ='right' THEN 'D'
	END as seio,
	CASE
		WHEN node_caps='no' THEN 0
		WHEN node_caps='yes' THEN 1
		WHEN node_caps='?' THEN 2
	END as node_caps,
	CASE
		WHEN irradiando ='no' THEN 0
		WHEN irradiando ='yes' THEN 1
	END as irradiando,
	CASE
		WHEN classe ='no-recurrence-events' THEN 0
		WHEN classe ='recurrence-events' THEN 1
	END as classe 
FROM
	public."cp03CancerMama"


```

#### 8  - Aplique label encoding à variável menopausa.

```sql
SELECT 
	CASE
		WHEN menopausa = 'ge40' THEN 1
		WHEN menopausa = 'premeno' THEN 2
		WHEN menopausa = 'lt40' THEN 3
	END AS menopausa
FROM
	public."cp03CancerMama"
```

#### 9 - [Desafio] Crie uma nova coluna chamada posicao_tumor concatenando as colunas inv_nodes e quadrante

```sql
SELECT 
	concat(inv_nodes,' ',quadrante) as posicao_tumor
FROM
	public."cp03CancerMama"
```

#### 10 - [Desafio] Aplique One Hot Encoding à coluna deg_malig.

```sql
SELECT 
	CASE WHEN deg_malig = 1 THEN 1 ELSE 0 END AS deg_malig1,
	CASE WHEN deg_malig = 2 THEN 1 ELSE 0 END AS deg_malig2,
	CASE WHEN deg_malig = 3 THEN 1 ELSE 0 END AS deg_malig3
FROM
	public."cp03CancerMama"
```

#### 11 -  Crie um novo dataset com todas as variáveis após as transformações anteriores.

```sql
SELECT
	id,
	idade,
	inv_nodes,
	deg_malig,
	concat(inv_nodes,' ',quadrante) as posicao_tumor,
	CASE WHEN deg_malig = 1 THEN 1 ELSE 0 END AS deg_malig1,
	CASE WHEN deg_malig = 2 THEN 1 ELSE 0 END AS deg_malig2,
	CASE WHEN deg_malig = 3 THEN 1 ELSE 0 END AS deg_malig3,
	CASE
		WHEN menopausa = 'ge40' THEN 1
		WHEN menopausa = 'premeno' THEN 2
		WHEN menopausa = 'lt40' THEN 3
	END AS menopausa,
	CASE
		WHEN quadrante = 'left_low' THEN 1
		WHEN quadrante = 'right_up' THEN 2
        	WHEN quadrante = 'left_up' THEN 3
        	WHEN quadrante = 'right_low' THEN 4
        	WHEN quadrante = 'central' THEN 5
        	ELSE 0
	END AS quadrante,
	CASE
	 	WHEN tamanho_tumor = '0-4' or tamanho_tumor = '5-9' THEN 'Muito Pequeno'
          	WHEN tamanho_tumor = '10-14' or tamanho_tumor = '15-19' THEN 'Pequeno'
         	WHEN tamanho_tumor = '20-24' or tamanho_tumor = '25-29' THEN 'Médio'
         	WHEN tamanho_tumor = '30-34' or tamanho_tumor = '35-39' THEN  'Grande'
         	WHEN tamanho_tumor = '40-44' or tamanho_tumor = '45-49' THEN 'Muito Grande'
         	WHEN tamanho_tumor = '50-54' or tamanho_tumor = '55-59' THEN 'Tratamento Urgente'
	END AS tamanho_tumoro,
	CASE
		WHEN seio ='left' THEN 'E'
		WHEN seio ='right' THEN 'D'
	END as seio,
	CASE
		WHEN node_caps='no' THEN 0
		WHEN node_caps='yes' THEN 1
		WHEN node_caps='?' THEN 2
	END as node_caps,
	CASE
		WHEN irradiando ='no' THEN 0
		WHEN irradiando ='yes' THEN 1
	END as irradiando,
	CASE
		WHEN classe ='no-recurrence-events' THEN 0
		WHEN classe ='recurrence-events' THEN 1
	END as classe 
FROM
	public."cp03CancerMama"
```
