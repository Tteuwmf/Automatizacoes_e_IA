from pathlib import Path
import time
import pandas as pd
import pyautogui

URL_SISTEMA = "https://dlp.hashtagtreinamentos.com/python/intensivao/login"
CAMINHO_DADOS = Path(__file__).parent / "produtos.csv"


def configurar_pyautogui() -> None:
    pyautogui.PAUSE = 0.5
    pyautogui.FAILSAFE = True


def abrir_navegador(navegador: str = "chrome") -> None:
    pyautogui.press("win")
    pyautogui.write(navegador)
    pyautogui.press("enter")
    time.sleep(2)


def realizar_login(email: str, senha: str) -> None:
    pyautogui.write(URL_SISTEMA)
    pyautogui.press("enter")
    time.sleep(3)

    # Clica no campo de e-mail e preenche as credenciais
    pyautogui.click(x=685, y=451)
    pyautogui.write(email)
    pyautogui.press("tab")
    pyautogui.write(senha)
    pyautogui.press("tab")
    pyautogui.press("enter")
    time.sleep(3)


def cadastrar_produtos(tabela: pd.DataFrame) -> None:
    campos = ["codigo", "marca", "tipo", "categoria", "preco_unitario", "custo"]

    for linha in tabela.index:
        # Clica no primeiro campo do formulário
        pyautogui.click(x=653, y=294)

        for campo in campos:
            pyautogui.write(str(tabela.loc[linha, campo]))
            pyautogui.press("tab")

        obs = tabela.loc[linha, "obs"]
        if not pd.isna(obs):
            pyautogui.write(str(obs))

        pyautogui.press("tab")
        pyautogui.press("enter")
        pyautogui.scroll(5000)


def main() -> None:
    configurar_pyautogui()
    tabela_produtos = pd.read_csv(CAMINHO_DADOS)

    abrir_navegador()
    realizar_login(email="pythonimpressionador@gmail.com", senha="sua_senha_aqui")
    cadastrar_produtos(tabela_produtos)


if __name__ == "__main__":
    main()
