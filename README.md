# Análise de Obras Rodoviárias — Departamento de Estradas de Rodagem (DER/SP)

## 1. Sobre o projeto
Projeto desenvolvido para o desafio final da Trilha Engenheiro de Dados Júnior da Aceleração EmpregaDados.

O objetivo é organizar e analisar dados de obras rodoviárias do Estado de São Paulo, utilizando Python, Pandas, DuckDB e SQL.

## 2. Fonte dos dados
- **Órgão:** Departamento de Estradas de Rodagem (DER/SP).
- **Base:** Obras.
- **Arquivo:** `Obras.xlsx`.
- **Aba utilizada:** Estradas Municipais.
- **Fonte:** https://dadosabertos.sp.gov.br/
- **Licença indicada no catálogo:** CC BY 4.0.

## 3. Organização do projeto
Os dados foram organizados em três camadas:
**Raw:** contém a planilha original, sem alterações.
**Refined:** contém os dados preparados em três arquivos:
- `obras.csv`: registros da planilha original.
- `obras_gerais.csv`: informações gerais das obras.
- `obras_financeiras.csv`: informações financeiras.
**Marts:** contém a consulta SQL e o indicador de quantidade de registros por status.
Foi criado o campo `id_registro` para relacionar as tabelas, pois a coluna `Contrato` possui valores ausentes.
A consulta SQL utiliza um JOIN entre as tabelas gerais e financeiras.

## 4. Resultado da análise
Foram analisados 685 registros da aba Estradas Municipais.
| Status | Quantidade |
|---|---:|
| Concluído | 540 |
| Andamento | 57 |
| Licitação | 46 |
| A licitar | 29 |
| Suspenso | 7 |
| Aguardando 1ª N.S. | 5 |
| Não informado | 1 |
| **Total** | **685** |
Os registros não representam necessariamente obras ou contratos únicos.

## 5. Ferramentas utilizadas
Python, Pandas, DuckDB, SQL, Poetry, Pytest, Git, GitHub e VS Code.

## 6. Como executar
Com Python e Poetry instalados, execute na pasta do projeto:
```bash
poetry install
poetry run python pipeline.py
````


O programa lê a planilha, prepara os dados e gera o indicador em `marts/indicador_status.csv`.

Para executar o teste:

```bash
poetry run pytest -v
```

## 7. Testes

Foi criado um teste automatizado com três registros fictícios para verificar se o SQL contabiliza corretamente os registros por status.

O teste utiliza um banco temporário e não altera os dados originais.

## 8. Uso de inteligência artificial

Utilizei inteligência artificial como apoio para desenvolver o projeto, entender os comandos e corrigir dúvidas durante a execução.

Durante a análise, identificamos que 76 registros não possuíam contrato informado. Por isso, não utilizamos a coluna `Contrato` como identificador único e criamos o campo `id_registro`.

Também conferimos o resultado do SQL, verificando que a soma dos registros por status corresponde aos 685 registros da planilha.

## 9. Limitações

A análise considera apenas a aba Estradas Municipais. Existem informações ausentes na base e os registros não representam necessariamente obras únicas.

O projeto apresenta um indicador de situação das obras, sem avaliar seu desempenho técnico ou financeiro.