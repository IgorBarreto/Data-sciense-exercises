## PROJETO 04 - OLIMPIADAS DE TOKYO 2020 (disputada em 2021)

### Especificações

#### Tabela:

##### Atleta

| Coluna     | Tipo         |
| ---------- | ------------ |
| name       | varchar(255) |
| nOC        | varchar(255) |
| discipline | varchar(255) |

##### Treinador

| Coluna     | Tipo         |
| ---------- | ------------ |
| name       | varchar(255) |
| noc        | varchar(255) |
| discipline | varchar(255) |
| event      | varchar(255) |

##### Registro

| Coluna     | Tipo         |
| ---------- | ------------ |
| discipline | varchar(255) |
| female     | integer      |
| male       | integer      |
| total      | integer      |

##### Medalha

| Coluna        | Tipo         |
| ------------- | ------------ |
| rank          | integer      |
| team_noc      | varchar(255) |
| gold          | integer      |
| silver        | integer      |
| bronze        | integer      |
| total         | integer      |
| rank_by_total | integer      |

##### Time

| Coluna     | Tipo         |
| ---------- | ------------ |
| name       | varchar(255) |
| discipline | varchar(255) |
| noc        | varchar(255) |
| event      | varchar(255) |

### Questões

#### 1 - Quem são os técnicos (coaches) e atletas das equipes de Handball?

```sql
SELECT
	id,name FROM "cp04Treinadores"
WHERE
	discipline = 'Handball'
UNION
SELECT
	id, name FROM "cp04Atletas"
WHERE discipline = 'Handball
```

#### 2 - Quem são os técnicos (coaches) dos atletas da Austrália que receberam medalhas de Ouro?

```sql
NÃO PODE SER RESPONDIDOS COM TODA A INTEGRIDADE DOS DADOS
```

#### 3 - Quais países tiveram mulheres conquistando medalhas de Ouro?

```sql
NÃO PODE SER RESPONDIDOS COM TODA A INTEGRIDADE DOS DADOS
```

#### 4- Quais atletas da Noruega receberam medalhas de Ouro ou Prata?

```sql
NÃO PODE SER RESPONDIDOS COM TODA A INTEGRIDADE DOS DADOS
```

#### 5 - Quais atletas Brasileiros não receberam medalhas?

```sql
NÃO PODE SER RESPONDIDOS COM TODA A INTEGRIDADE DOS DADOS
```
