import pandas as pd

def carregar_dados(caminho_arquivo): #receber a localização do arquivo
    dados = pd.read_csv(camino_arquivo, dtype=str, keep_default_na=False) 

    return dados #retornar os dados carregados