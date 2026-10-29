import os
import streamlit as st
from openai import OpenAI

MODELO_PADRAO = "gpt-4o-mini"


def inicializar_cliente_openai() -> OpenAI:
    # A chave deve ser definida na variável de ambiente OPENAI_API_KEY
    chave_api = os.getenv("OPENAI_API_KEY")
    if not chave_api:
        st.warning("Defina a variável de ambiente OPENAI_API_KEY para utilizar o chatbot.")
        st.stop()
    return OpenAI(api_key=chave_api)


def inicializar_historico() -> None:
    if "lista_mensagens" not in st.session_state:
        st.session_state["lista_mensagens"] = []


def renderizar_historico() -> None:
    for mensagem in st.session_state["lista_mensagens"]:
        st.chat_message(mensagem["role"]).write(mensagem["content"])


def processar_nova_mensagem(cliente: OpenAI, texto_usuario: str) -> None:
    st.chat_message("user").write(texto_usuario)
    st.session_state["lista_mensagens"].append({"role": "user", "content": texto_usuario})

    resposta_modelo = cliente.chat.completions.create(
        messages=st.session_state["lista_mensagens"],
        model=MODELO_PADRAO,
    )
    resposta_ia = resposta_modelo.choices[0].message.content

    st.chat_message("assistant").write(resposta_ia)
    st.session_state["lista_mensagens"].append({"role": "assistant", "content": resposta_ia})


def main() -> None:
    st.set_page_config(page_title="ChatBot com IA", page_icon="🤖")
    st.title("ChatBot com IA")

    inicializar_historico()
    renderizar_historico()

    cliente = inicializar_cliente_openai()
    mensagem_usuario = st.chat_input("Escreva sua mensagem aqui...")

    if mensagem_usuario:
        processar_nova_mensagem(cliente, mensagem_usuario)


if __name__ == "__main__":
    main()
