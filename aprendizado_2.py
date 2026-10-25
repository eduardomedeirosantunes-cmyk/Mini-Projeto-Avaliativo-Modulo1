from pathlib import Path
import pandas as pd

# Localizar a pasta e o CSV
pasta_projeto = Path(__file__).resolve().parent
caminho = pasta_projeto / "dados" / "halloween_vendas.csv"


# Criar nossa primeira função
def carregar_dados(caminho_arquivo):

    tabela = pd.read_csv( caminho_arquivo, encoding="utf-8-sig", sep=",")

    return tabela


# Utilizar a função
dados = carregar_dados(caminho)

# Mostrar o resultado
print(dados.head())

print("\nQuantidade de registros:")
print(len(dados))