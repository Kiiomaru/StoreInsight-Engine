import pathlib
from dotenv import load_dotenv
import os
from indicators.indicators import Indicadores
from services.email_service import Email
from services.filemanager import FileManager
from services.data_loader import DataLoader
from services.utils import separar_lojas, bateu_meta


def app():
    load_dotenv()
    remetente = os.getenv("EMAIL_REMETENTE")
    senha = os.getenv("SENHA_DE_APP")

    data_loader = DataLoader()
    emails = data_loader.carregar_emails()
    lojas = data_loader.carregar_lojas()
    vendas = data_loader.carregar_vendas()

    vendas = vendas.merge(lojas, on="ID Loja")

    dicionario_lojas = separar_lojas(lojas, vendas)

    dia_indicador = vendas["Data"].max()

    file_manager = FileManager()
    caminho_backup = file_manager.salvar_backups(dicionario_lojas, dia_indicador)  # type: ignore

    # Definição de metas

    meta_faturamento_dia = 1000
    meta_faturamento_ano = 1650000
    meta_qtdeprodutos_dia = 4
    meta_qtdeprodutos_ano = 120
    meta_ticketmedio_dia = 500
    meta_ticketmedio_ano = 500

    indicadores = Indicadores()

    for loja, vendas_loja in dicionario_lojas.items():  # type: ignore
        vendas_loja_dia = indicadores.filtrar_lojas_dia(vendas_loja, dia_indicador)
        faturamento_ano, faturamento_dia = indicadores.calcular_faturamento(
            vendas_loja, vendas_loja_dia
        )
        qtde_produtos_ano, qtde_produtos_dia = indicadores.calcular_qtdeprodutos(
            vendas_loja, vendas_loja_dia
        )
        ticket_medio_ano, ticket_medio_dia = indicadores.calcular_ticket_medio(
            vendas_loja, vendas_loja_dia
        )

        nome_gerente = emails.loc[emails["Loja"] == loja, "Gerente"].values[0]  # type: ignore
        destinatario = emails.loc[emails["Loja"] == loja, "E-mail"].values[0]

        assunto = f"OnePage Dia {dia_indicador.day}/{dia_indicador.month} - Loja {loja}"
        email = Email()
        email.config_email(remetente, destinatario, assunto)

        cor_fat_dia = bateu_meta(faturamento_dia, meta_faturamento_dia)
        cor_fat_ano = bateu_meta(faturamento_ano, meta_faturamento_ano)
        cor_qtde_dia = bateu_meta(qtde_produtos_dia, meta_qtdeprodutos_dia)
        cor_qtde_ano = bateu_meta(qtde_produtos_ano, meta_qtdeprodutos_ano)
        cor_ticket_dia = bateu_meta(ticket_medio_dia, meta_ticketmedio_dia)
        cor_ticket_ano = bateu_meta(ticket_medio_ano, meta_ticketmedio_ano)

        dados = {
            "nome": nome_gerente,
            "dia_indicador_day": dia_indicador.day,
            "dia_indicador_month": dia_indicador.month,
            "loja": loja,
            "faturamento_dia": faturamento_dia,
            "meta_faturamento_dia": meta_faturamento_dia,
            "cor_fat_dia": cor_fat_dia,
            "faturamento_ano": faturamento_ano,
            "meta_faturamento_ano": meta_faturamento_ano,
            "cor_fat_ano": cor_fat_ano,
            "qtde_produtos_dia": qtde_produtos_dia,
            "meta_qtdeprodutos_dia": meta_qtdeprodutos_dia,
            "cor_qtde_dia": cor_qtde_dia,
            "qtde_produtos_ano": qtde_produtos_ano,
            "meta_qtdeprodutos_ano": meta_qtdeprodutos_ano,
            "cor_qtde_ano": cor_qtde_ano,
            "ticket_medio_dia": ticket_medio_dia,
            "meta_ticketmedio_dia": meta_ticketmedio_dia,
            "cor_ticket_dia": cor_ticket_dia,
            "ticket_medio_ano": ticket_medio_ano,
            "meta_ticketmedio_ano": meta_ticketmedio_ano,
            "cor_ticket_ano": cor_ticket_ano,
        }

        corpo = email.montar_corpo(dados)
        email.anexar_corpo(corpo)

        caminho_arquivo = (
            pathlib.Path.cwd()
            / caminho_backup
            / loja
            / f"{dia_indicador.month}_{dia_indicador.day}_{loja}.xlsx"
        )

        email.anexar_arquivo(caminho_arquivo)
        email.enviar_email(remetente, senha)
        print(f"Email da loja {loja} enviado com sucesso!")

    faturamento_lojas_ano = file_manager.backup_ranking_anual(vendas, dia_indicador)  # type: ignore
    faturamento_lojas_dia = file_manager.backup_ranking_diario(vendas, dia_indicador)  # type: ignore

    destinatario = emails.loc[emails["Loja"] == "Diretoria", "E-mail"].values[0]
    assunto = f"Ranking Dia {dia_indicador.day}/{dia_indicador.month}"

    email.config_email(remetente, destinatario, assunto)

    corpo = f"""
    <p>Prezados, bom dia.</p>

    <p><b>Melhor loja do Dia em Faturamento:</b> Loja {faturamento_lojas_dia.index[0]} com Faturamento R${faturamento_lojas_dia.iloc[0, 0]:.2f}</p>

    <p><b>Pior loja do dia em Faturamento:</b> Loja {faturamento_lojas_dia.index[-1]} com Faturamento R${faturamento_lojas_dia.iloc[-1, 0]:.2f}</p>

    <br>

    <p><b>Melhor loja do Ano em Faturamento:</b> Loja {faturamento_lojas_ano.index[0]} com Faturamento R${faturamento_lojas_ano.iloc[0, 0]:.2f}</p>

    <p><b>Pior loja do Ano em Faturamento:</b> Loja {faturamento_lojas_ano.index[-1]} com Faturamento R${faturamento_lojas_ano.iloc[-1, 0]:.2f}</p>

    <br>

    <p>Segue em anexo os rankings do ano e dia de todas as lojas.</p>

    <p>Qualquer dúvida estou à disposição.</p>
    """

    email.anexar_corpo(corpo)

    caminho_arquivo = [
        pathlib.Path.cwd()
        / caminho_backup
        / f"{dia_indicador.month}_{dia_indicador.day}_Ranking_Anual.xlsx",
        pathlib.Path.cwd()
        / caminho_backup
        / f"{dia_indicador.month}_{dia_indicador.day}_Ranking_Dia.xlsx",
    ]

    for arquivo in caminho_arquivo:
        email.anexar_arquivo(arquivo)

    email.enviar_email(remetente, senha)
    print("Email da Diretoria enviado com sucesso!")


if __name__ == "__main__":
    app()
