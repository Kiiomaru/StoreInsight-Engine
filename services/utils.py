import pandas as pd


def separar_lojas(lojas: pd.DataFrame, vendas: pd.DataFrame) -> dict[str, pd.DataFrame]:
    dicionario_lojas = {}
    for loja in lojas["Loja"]:
        dicionario_lojas[loja] = vendas.loc[vendas["Loja"] == loja, :]
    return dicionario_lojas


def bateu_meta(valor, meta):
    return "green" if valor >= meta else "red"
