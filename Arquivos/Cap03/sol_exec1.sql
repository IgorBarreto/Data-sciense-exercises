# Solução Exercício 1


# Item 1:

SELECT * 
FROM cap02.TB_NAVIOS 
WHERE pontuacao_risco = 310;


# Item 2

SELECT * 
FROM cap02.TB_NAVIOS 
WHERE classificacao_risco = 'A'
  AND indice_conformidade >= 95;


# Item 3

SELECT * 
FROM cap02.TB_NAVIOS 
WHERE classificacao_risco = 'C' OR classificacao_risco = 'D'
  AND indice_conformidade <= 95;

SELECT * 
FROM cap02.TB_NAVIOS 
WHERE classificacao_risco IN ('C','D')
  AND indice_conformidade <= 95;


# Item 4

SELECT * 
FROM cap02.TB_NAVIOS 
WHERE classificacao_risco = 'A' 
   OR pontuacao_risco = 0;


# Item 5

SELECT * 
FROM cap02.TB_NAVIOS 
WHERE temporada LIKE '%Dezembro 2016';


