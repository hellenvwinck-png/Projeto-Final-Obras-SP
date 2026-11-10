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