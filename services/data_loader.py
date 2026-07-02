import pandas as pd


class DataLoader:
    def carregar_emails(self) -> pd.DataFrame:
        emails = pd.read_excel(r"Bases de Dados\Emails.xlsx")
        return emails

    def carregar_lojas(self) -> pd.DataFrame:
        lojas = pd.read_csv(r"Bases de Dados\Lojas.csv", encoding="latin1", sep=";")
        return lojas

    def carregar_vendas(self) -> pd.DataFrame:
        vendas = pd.read_excel(r"Bases de Dados\Vendas.xlsx")
        return vendas
