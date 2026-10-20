import csv
import pandas as pd

def carregar_dados(caminho_arquivo):
    dados = pd.read_csv(caminho_arquivo, sep=";", encoding="cp1252", dtype=str, keep_default_na=False) 

    return dados #retornar os dados carregados