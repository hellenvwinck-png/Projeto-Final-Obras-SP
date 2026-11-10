from pathlib import Path
import duckdb
import pandas as pd
def test_quantidade_obras_por_status():
    # Criamos três obras fictícias para testar
    gerais = pd.DataFrame({
        "id_registro": [1, 2, 3],
        "Status": ["CONCLUÍDO", "ANDAMENTO", "CONCLUÍDO"]
    })
    financeiras = pd.DataFrame({
        "id_registro": [1, 2, 3],
        "valor": [100, 200, 300]
    })
    # Criamos um banco temporário, sem alterar o banco real
    conexao = duckdb.connect(":memory:")
    conexao.register("obras_gerais", gerais)
    conexao.register("obras_financeiras", financeiras)
    # Executamos nosso SQL
    consulta = Path("marts/indicador_status.sql").read_text(
        encoding="utf-8"
    )
    resultado = conexao.execute(consulta).df()
    # Verificamos se o resultado está correto
    assert resultado["quantidade_obras"].sum() == 3
    assert resultado.loc[
        resultado["Status"] == "CONCLUÍDO",
        "quantidade_obras"
    ].iloc[0] == 2