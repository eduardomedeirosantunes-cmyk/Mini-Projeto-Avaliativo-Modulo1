from pathlib import Path
from funcoes import carregar_dados

# Descobrir onde está o main.py
pasta_projeto = Path(__file__).resolve().parent

# Localizar o CSV dentro da pasta dados
caminho_csv = pasta_projeto / "dados" / "halloween_vendas.csv"

# Chamar a função e enviar o caminho
dados = carregar_dados(caminho_csv)


# Mostrar os nomes das colunas
print("\n=== COLUNAS ===")
print(dados.columns.tolist())

# Mostrar quantidade de linhas e colunas
print("\n=== TAMANHO ===")
print(dados.shape)

# Mostrar os primeiros registros do DataFrame
print("\n=== PRIMEIROS REGISTROS ===")
print(dados.head())