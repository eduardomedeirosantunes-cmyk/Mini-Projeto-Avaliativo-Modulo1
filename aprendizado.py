from pathlib import Path

# Importar a biblioteca Pandas
import pandas as pd

# 1. Descobrir onde este programa está salvo
pasta_projeto = Path(__file__).resolve().parent

# 2. Montar o caminho completo do CSV
caminho = pasta_projeto / "dados" / "halloween_vendas.csv"

# 3. Mostrar o caminho encontrado
print("Caminho do CSV:")
print(caminho)

# 4. Ler o CSV e guardar os dados em uma variável
dados = pd.read_csv(caminho, encoding="utf-8-sig", sep=",")


# 5. Mostrar os primeiros registros
print("\nPrimeiros cinco registros:")
print(dados.head())

# 6. Mostrar quantidade de linhas
print("\nQuantidade de registros:")
print(len(dados))








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






categoria = " FANTASIA!!! "

print(categoria)
print(categoria.strip())


categoria = " FANTASIA!!! "

categoria_limpa = categoria.strip().lower()

print(categoria_limpa)


import re

categoria = " FANTASIA!!! "

categoria_limpa = categoria.strip().lower()

categoria_limpa = re.sub(r"[^a-z ]", "", categoria_limpa)

print(categoria_limpa)


preco = "132.5"

numero = float(preco)

print(numero)
print(type(numero))



from datetime import datetime

texto = "2025-10-12 14:35:00"

data = datetime.strptime(texto, "%Y-%m-%d %H:%M:%S")

print(data)
print(type(data))

print("Ano:", data.year)
print("Mês:", data.month)
print("Dia:", data.day)
print("Hora:", data.hour)