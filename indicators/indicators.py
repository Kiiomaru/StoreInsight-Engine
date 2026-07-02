class Indicadores:
    def filtrar_lojas_dia(self, vendas_loja, dia_indicador):
        vendas_loja_dia = vendas_loja.loc[vendas_loja["Data"] == dia_indicador, :]
        return vendas_loja_dia

    def calcular_faturamento(self, vendas_loja, vendas_loja_dia):
        faturamento_ano = vendas_loja["Valor Final"].sum()
        faturamento_dia = vendas_loja_dia["Valor Final"].sum()
        return faturamento_ano, faturamento_dia

    def calcular_qtdeprodutos(self, vendas_loja, vendas_loja_dia):
        qtde_produtos_ano = vendas_loja["Produto"].nunique()
        qtde_produtos_dia = vendas_loja_dia["Produto"].nunique()
        return qtde_produtos_ano, qtde_produtos_dia

    def calcular_ticket_medio(self, vendas_loja, vendas_loja_dia):
        valor_venda = vendas_loja.groupby("Código Venda").agg(
            {"Quantidade": "sum", "Valor Unitário": "sum", "Valor Final": "sum"}
        )
        ticket_medio_ano = valor_venda["Valor Final"].mean()

        valor_venda_dia = vendas_loja_dia.groupby("Código Venda").agg(
            {"Quantidade": "sum", "Valor Unitário": "sum", "Valor Final": "sum"}
        )
        ticket_medio_dia = valor_venda_dia["Valor Final"].mean()
        return ticket_medio_ano, ticket_medio_dia
