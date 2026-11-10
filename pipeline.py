import pandas as pd

arquivo = "raw/Obras.xlsx"
excel = pd.ExcelFile(arquivo)

print(excel.sheet_names) 
dados = pd.read_excel(arquivo, sheet_name="Estradas Municipais")
print(dados.head())
print(dados.columns.tolist())
print("Quantidade de linhas:", dados.shape[0])
print("Quantidade de colunas:", dados.shape[1])
print("\nValores ausentes por coluna:")
print(dados.isnull().sum().to_string())
print("\nQuantidade de linhas duplicadas:")
print(dados.duplicated().sum())
print("\nColunas relacionadas à identificação:")
print([col for col in dados.columns if "contrato" in col.lower() or "obra" in col.lower()])
print("\nContratos diferentes:", dados["Contrato"].nunique())
print("Contratos vazios:", dados["Contrato"].isnull().sum())
print("Contratos repetidos:", dados["Contrato"].duplicated().sum())
sem_contrato = dados[dados["Contrato"].isnull()]
print("\nExemplos de registros sem contrato:")
print(sem_contrato.head(5).to_string())
dados["id_registro"] = range(1, len(dados) + 1)
print("\nIdentificadores criados:")
print(dados[["id_registro", "Contrato"]].head())
from pathlib import Path
Path("refined").mkdir(exist_ok=True)
dados.to_csv("refined/obras.csv", index=False, encoding="utf-8-sig")
print("\nTabela refined/obras.csv criada com sucesso!")
colunas_gerais = [
    "id_registro",
    "Contrato",
    "Status",
    "Prazo Inicial",
    "Prazo Vigente",
]
colunas_financeiras = [
    "id_registro",
    "Valor Contrato Inicial (R$)",
    "Valor Contrato Vigente (R$)",
    "% Execução Financeira",
]
obras_gerais = dados[colunas_gerais].copy()
obras_financeiras = dados[colunas_financeiras].copy()
obras_gerais.to_csv("refined/obras_gerais.csv", index=False)
obras_financeiras.to_csv("refined/obras_financeiras.csv", index=False)
print("\nTabelas gerais e financeiras criadas!")
import duckdb
conexao = duckdb.connect("obras.duckdb")
conexao.execute("""
    CREATE OR REPLACE TABLE obras_gerais AS
    SELECT * FROM read_csv_auto('refined/obras_gerais.csv')
""")
conexao.execute("""
    CREATE OR REPLACE TABLE obras_financeiras AS
    SELECT * FROM read_csv_auto('refined/obras_financeiras.csv')
""")
print("Tabelas carregadas no DuckDB com sucesso!")
from pathlib import Path
consulta = Path("marts/indicador_status.sql").read_text(encoding="utf-8")
resultado = conexao.execute(consulta).df()
print("\nQuantidade de obras por status:")
print(resultado)
resultado.to_csv(
    "marts/indicador_status.csv",
    index=False,
    encoding="utf-8-sig"
)
print("Indicador salvo com sucesso!")