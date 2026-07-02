import pathlib
import pandas as pd


class FileManager:
    def salvar_backups(
        self, dicionario_lojas: dict[str, pd.DataFrame], dia_indicador: pd.Timestamp
    ):
        caminho_backup = pathlib.Path(r"Backup Arquivos Lojas")
        caminho_backup.mkdir(parents=True, exist_ok=True)
        arquivos_pasta_backup = caminho_backup.iterdir()
        lista_nomes_backup = [arquivo.name for arquivo in arquivos_pasta_backup]
        for loja in dicionario_lojas:
            if loja not in lista_nomes_backup:
                nova_pasta = caminho_backup / loja
                nova_pasta.mkdir()

            # salvar arquivos de backup na pasta
            nome_arquivo = f"{dia_indicador.month}_{dia_indicador.day}_{loja}.xlsx"
            local_arquivo = caminho_backup / loja / nome_arquivo

            dicionario_lojas[loja].to_excel(local_arquivo)
        return caminho_backup

    def backup_ranking_anual(self, vendas: pd.DataFrame, dia_indicador: pd.Timestamp):
        faturamento_lojas = vendas.groupby("Loja")[["Valor Final"]].sum()
        faturamento_lojas_ano = faturamento_lojas.sort_values(
            by="Valor Final", ascending=False
        )

        nome_arquivo = f"{dia_indicador.month}_{dia_indicador.day}_Ranking_Anual.xlsx"
        faturamento_lojas_ano.to_excel(rf"Backup Arquivos Lojas\{nome_arquivo}")
        return faturamento_lojas_ano

    def backup_ranking_diario(self, vendas: pd.DataFrame, dia_indicador: pd.Timestamp):
        vendas_dia = vendas.loc[vendas["Data"] == dia_indicador, :]
        faturamento_lojas_dia = vendas_dia.groupby("Loja")[["Valor Final"]].sum()
        faturamento_lojas_dia = faturamento_lojas_dia.sort_values(
            by="Valor Final", ascending=False
        )  # type: ignore
        nome_arquivo = f"{dia_indicador.month}_{dia_indicador.day}_Ranking_Dia.xlsx"
        faturamento_lojas_dia.to_excel(rf"Backup Arquivos Lojas\{nome_arquivo}")
        return faturamento_lojas_dia
