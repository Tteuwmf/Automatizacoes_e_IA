def demonstrar_estruturas_historico() -> None:
    # Estrutura de lista de dicionários usada para armazenar histórico de conversas em LLMs
    historico_mensagens: list[dict[str, str]] = [
        {"role": "user", "content": "Olá! Como funciona a memória de um chatbot?"},
        {"role": "assistant", "content": "Cada mensagem é salva como um dicionário com 'role' e 'content'."},
    ]

    nova_interacao = {"role": "user", "content": "Perfeito, obrigado pela explicação!"}
    historico_mensagens.append(nova_interacao)

    print("=== Histórico de Mensagens Estruturado ===")
    for item in historico_mensagens:
        autor = "Usuário" if item["role"] == "user" else "IA"
        print(f"[{autor}]: {item['content']}")


if __name__ == "__main__":
    demonstrar_estruturas_historico()
