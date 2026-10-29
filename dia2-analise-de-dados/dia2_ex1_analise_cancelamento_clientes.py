from pathlib import Path
import pandas as pd
import plotly.express as px

CAMINHO_DADOS = Path(__file__).parent / "cancelamentos.csv"


def carregar_e_tratar_dados(caminho: Path) -> pd.DataFrame:
    tabela = pd.read_csv(caminho)
    # Remove identificador irrelevante para análise estatística e linhas incompletas
    tabela = tabela.drop(columns=["CustomerID"], errors="ignore")
    return tabela.dropna()


def exibir_taxa_cancelamento(tabela: pd.DataFrame, etapa: str) -> None:
    contagem = tabela["cancelou"].value_counts()
    percentual = tabela["cancelou"].value_counts(normalize=True).map("{:.1%}".format)

    print(f"\n=== {etapa} ===")
    print("Contagem absoluta:")
    print(contagem.to_string())
    print("\nProporção:")
    print(percentual.to_string())


def gerar_histogramas_impacto(tabela: pd.DataFrame) -> None:
    for coluna in tabela.columns:
        grafico = px.histogram(tabela, x=coluna, color="cancelou", title=f"Impacto de {coluna} no Cancelamento")
        grafico.show()


def aplicar_filtros_retencao(tabela: pd.DataFrame) -> pd.DataFrame:
    # Filtra as três principais causas de churn identificadas na análise:
    # 1. Contratos mensais, 2. Mais de 4 ligações ao call center, 3. Mais de 20 dias de atraso
    tabela_filtrada = tabela[tabela["duracao_contrato"] != "Monthly"]
    tabela_filtrada = tabela_filtrada[tabela_filtrada["ligacoes_callcenter"] <= 4]
    tabela_filtrada = tabela_filtrada[tabela_filtrada["dias_atraso"] <= 20]
    return tabela_filtrada


def main(exibir_graficos: bool = False) -> None:
    tabela = carregar_e_tratar_dados(CAMINHO_DADOS)
    exibir_taxa_cancelamento(tabela, "Cenário Inicial (Pós-Limpeza)")

    if exibir_graficos:
        gerar_histogramas_impacto(tabela)

    tabela_otimizada = aplicar_filtros_retencao(tabela)
    exibir_taxa_cancelamento(tabela_otimizada, "Cenário Otimizado (Pós-Ações de Retenção)")


if __name__ == "__main__":
    main(exibir_graficos=False)
