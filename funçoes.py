import pandas as pd

def carregar_dados(caminho): #receber a localização do arquivo
    dados = pd.read_csv(caminho, dtype=str, keep_default_na=False) 

    return dados #retornar os dados carregados