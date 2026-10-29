from __future__ import annotations
from pathlib import Path
import pandas as pd
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score
from sklearn.model_selection import train_test_split
from sklearn.neighbors import KNeighborsClassifier
from sklearn.preprocessing import LabelEncoder

DIRETORIO_BASE = Path(__file__).parent
CAMINHO_CLIENTES = DIRETORIO_BASE / "clientes.csv"
CAMINHO_NOVOS_CLIENTES = DIRETORIO_BASE / "novos_clientes.csv"
COLUNAS_CATEGORICAS = ["profissao", "mix_credito", "comportamento_pagamento"]


def codificar_colunas_categoricas(
    tabela: pd.DataFrame, codificadores: dict[str, LabelEncoder] | None = None
) -> tuple[pd.DataFrame, dict[str, LabelEncoder]]:
    tabela = tabela.copy()

    if codificadores is None:
        codificadores = {}
        for coluna in COLUNAS_CATEGORICAS:
            le = LabelEncoder()
            tabela[coluna] = le.fit_transform(tabela[coluna])
            codificadores[coluna] = le
    else:
        for coluna, le in codificadores.items():
            tabela[coluna] = le.transform(tabela[coluna])

    return tabela, codificadores


def treinar_e_avaliar_modelos(x: pd.DataFrame, y: pd.Series) -> RandomForestClassifier:
    x_treino, x_teste, y_treino, y_teste = train_test_split(
        x, y, test_size=0.3, random_state=42
    )

    modelo_arvore = RandomForestClassifier(random_state=42, n_jobs=-1)
    modelo_knn = KNeighborsClassifier(n_jobs=-1)

    modelo_arvore.fit(x_treino, y_treino)
    modelo_knn.fit(x_treino, y_treino)

    acuracia_arvore = accuracy_score(y_teste, modelo_arvore.predict(x_teste))
    acuracia_knn = accuracy_score(y_teste, modelo_knn.predict(x_teste))

    print("=== Avaliação dos Modelos ===")
    print(f"Acurácia Random Forest: {acuracia_arvore:.2%}")
    print(f"Acurácia KNN:           {acuracia_knn:.2%}")

    # Exibe as 5 variáveis mais relevantes para definição do score
    importancias = pd.Series(modelo_arvore.feature_importances_, index=x.columns)
    print("\n=== Top 5 Características Mais Importantes ===")
    print((importancias.sort_values(ascending=False).head(5) * 100).round(2).to_string())

    return modelo_arvore


def prever_novos_clientes(
    modelo: RandomForestClassifier, codificadores: dict[str, LabelEncoder]
) -> None:
    novos_clientes = pd.read_csv(CAMINHO_NOVOS_CLIENTES)
    novos_codificados, _ = codificar_colunas_categoricas(novos_clientes, codificadores)

    previsoes = modelo.predict(novos_codificados)
    resultado = novos_clientes[["profissao", "salario_anual", "mix_credito", "divida_total"]].copy()
    resultado["score_previsto"] = previsoes

    print("\n=== Previsão para Novos Clientes ===")
    print(resultado.to_string(index=False))


def main() -> None:
    tabela = pd.read_csv(CAMINHO_CLIENTES)
    tabela_codificada, codificadores = codificar_colunas_categoricas(tabela)

    y = tabela_codificada["score_credito"]
    x = tabela_codificada.drop(columns=["score_credito", "id_cliente"])

    melhor_modelo = treinar_e_avaliar_modelos(x, y)
    prever_novos_clientes(melhor_modelo, codificadores)


if __name__ == "__main__":
    main()
