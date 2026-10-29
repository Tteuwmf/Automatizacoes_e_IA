# 🚀 Automatizações e IA — Jornada Python

Este repositório reúne as soluções práticas desenvolvidas ao longo da **Jornada Python** (Hashtag Treinamentos), organizadas para demonstrar aprendizados aplicados em **Automação de Processos (RPA)**, **Análise Exploratória de Dados**, **Machine Learning / Inteligência Artificial** e **Desenvolvimento de Sistemas e Chatbots**.

---

## 📖 Sobre o Minicurso

A **Jornada Python** é uma imersão prática dividida em 4 dias, na qual cada aula aborda um problema real de negócio solucionado com Python e suas principais bibliotecas do mercado:

1. **Dia 1 — Python PowerUp (Automação de Tarefas):** Automação de processos repetitivos (RPA) controlando mouse, teclado e leitura de bases de dados.
2. **Dia 2 — Python Insights (Análise de Dados):** Tratamento de dados, estatística descritiva, visualização gráfica interativa e tomada de decisão orientada a dados (*Data-Driven*).
3. **Dia 3 — Python IA (Inteligência Artificial e Previsões):** Construção, treinamento e avaliação de modelos preditivos de *Machine Learning* para classificação de risco de crédito.
4. **Dia 4 — Python Dev (Criação de Chatbots e Sistemas):** Desenvolvimento de interfaces web interativas, integração com LLMs (OpenAI) e comunicação em tempo real via WebSockets.

---

## 📂 Estrutura do Repositório

O projeto está dividido em subpastas no formato `dia-assunto`, contendo os scripts `.py` nomeados por dia e exercício, além das respectivas bases de dados e templates necessários para execução:

```text
Automatizacoes_e_IA/
├── dia1-automacao-de-tarefas/
│   ├── dia1_ex1_automacao_cadastro_produtos.py
│   ├── dia1_ex2_capturar_posicao_mouse.py
│   └── produtos.csv
├── dia2-analise-de-dados/
│   ├── dia2_ex1_analise_cancelamento_clientes.py
│   └── cancelamentos.csv
├── dia3-inteligencia-artificial-e-previsoes/
│   ├── dia3_ex1_previsao_score_credito.py
│   ├── clientes.csv
│   └── novos_clientes.csv
├── dia4-criacao-de-chatbots-e-sistemas/
│   ├── dia4_ex1_chatbot_ia_streamlit.py
│   ├── dia4_ex2_estruturas_chat_auxiliar.py
│   ├── dia4_ex3_chat_tempo_real_hashzap.py
│   └── templates/
│       ├── homepage.html
│       └── index.html
├── requirements.txt
└── README.md
```

---

## 🧠 O que Cada Exercício Proporciona e Significa

### 🔹 Dia 1: Automação de Tarefas (`dia1-automacao-de-tarefas`)

- **`dia1_ex1_automacao_cadastro_produtos.py`**:
  - **O que faz:** Automatiza a abertura do navegador, o login em um sistema web corporativo, a leitura de uma base de produtos (`produtos.csv`) com `pandas` e o preenchimento contínuo de formulários usando `pyautogui`.
  - **O que proporciona e significa:** Demonstra como substituir tarefas manuais altamente repetitivas e propensas a erro humano por um robô de software (RPA). Na prática corporativa, processos que levariam horas de digitação passam a ser executados de forma autônoma e padronizada.
- **`dia1_ex2_capturar_posicao_mouse.py`**:
  - **O que faz:** Utilitário auxiliar que aguarda o posicionamento do cursor e retorna as coordenadas exatas `(x, y)` da tela.
  - **O que proporciona e significa:** Permite mapear elementos visuais de qualquer interface gráfica (web ou desktop legada) quando não há API disponível para integração direta.

---

### 🔹 Dia 2: Análise de Dados (`dia2-analise-de-dados`)

- **`dia2_ex1_analise_cancelamento_clientes.py`**:
  - **O que faz:** Carrega a base histórica de clientes (`cancelamentos.csv`), realiza limpeza de dados ausentes (`dropna`) e colunas irrelevantes (`CustomerID`), calcula a taxa de cancelamento (*Churn Rate*), gera histogramas interativos com `plotly.express` e simula o impacto de políticas de retenção.
  - **O que proporciona e significa:** Mostra como transformar dados brutos em diagnósticos acionáveis de negócio. A análise revela três causas críticas de cancelamento:
    1. Clientes no contrato mensal (`Monthly`) apresentam praticamente 100% de cancelamento.
    2. Clientes que realizam mais de 4 ligações ao call center cancelam o serviço.
    3. Clientes com mais de 20 dias de atraso financeiro cancelam a assinatura.
  - **Impacto prático:** Ao atuar sobre esses três indicadores, a taxa de cancelamento da empresa cai de **56,8%** para **18,4%**.

---

### 🔹 Dia 3: Inteligência Artificial e Previsões (`dia3-inteligencia-artificial-e-previsoes`)

- **`dia3_ex1_previsao_score_credito.py`**:
  - **O que faz:** Prepara uma base de 100.000 registros financeiros (`clientes.csv`), codifica variáveis categóricas com `LabelEncoder`, divide os dados em treino e teste (`train_test_split`) e treina dois algoritmos supervisionados de classificação (`RandomForestClassifier` e `KNeighborsClassifier`). Em seguida, compara a acurácia, extrai a importância das variáveis e classifica novos clientes (`novos_clientes.csv`) em `Good`, `Standard` ou `Poor`.
  - **O que proporciona e significa:** Representa a transição da análise descritiva ("o que aconteceu?") para a modelagem preditiva ("o que vai acontecer?"). O modelo **Random Forest** atinge **~82,5% de acurácia**, destacando variáveis decisivas como `divida_total`, `mix_credito` e `juros_emprestimo`, permitindo automatizar a concessão de crédito com segurança estatística.

---

### 🔹 Dia 4: Criação de Chatbots e Sistemas (`dia4-criacao-de-chatbots-e-sistemas`)

- **`dia4_ex1_chatbot_ia_streamlit.py`**:
  - **O que faz:** Constrói uma aplicação web completa (frontend e backend em Python) com `streamlit`, mantendo histórico de sessão (`st.session_state`) e integrando-se à API da OpenAI para respostas contextuais em tempo real.
  - **O que proporciona e significa:** Demonstra como criar rapidamente interfaces conversacionais modernas conectadas a Grandes Modelos de Linguagem (LLMs), gerenciando estado de conversa e boas práticas de segurança com variáveis de ambiente (`OPENAI_API_KEY`).
- **`dia4_ex2_estruturas_chat_auxiliar.py`**:
  - **O que faz:** Demonstra a manipulação de listas e dicionários em Python no formato `{"role": ..., "content": ...}`.
  - **O que proporciona e significa:** Explicita a estrutura de dados fundamental utilizada pelas APIs modernas de IA generativa para manter o contexto de múltiplos turnos em uma conversa.
- **`dia4_ex3_chat_tempo_real_hashzap.py`**:
  - **O que faz:** Implementa o servidor web do **Hashzap** utilizando `Flask` e `Flask-SocketIO` para comunicação bidirecional instantânea (*broadcast*) entre múltiplos usuários conectados.
  - **O que proporciona e significa:** Ensina os fundamentos de arquiteturas orientadas a eventos e WebSockets, essenciais para sistemas de mensagens instantâneas, notificações ao vivo e dashboards em tempo real.

---

## ⚙️ Como Executar os Projetos

1. **Clone o repositório e instale as dependências:**
   ```bash
   git clone https://github.com/Tteuwmf/Automatizacoes_e_IA.git
   cd Automatizacoes_e_IA
   pip install -r requirements.txt
   ```

2. **Executar os exercícios de cada dia:**
   - **Dia 1 (Automação):**
     ```bash
     python dia1-automacao-de-tarefas/dia1_ex2_capturar_posicao_mouse.py
     python dia1-automacao-de-tarefas/dia1_ex1_automacao_cadastro_produtos.py
     ```
   - **Dia 2 (Análise de Dados):**
     ```bash
     python dia2-analise-de-dados/dia2_ex1_analise_cancelamento_clientes.py
     ```
   - **Dia 3 (Machine Learning / IA):**
     ```bash
     python dia3-inteligencia-artificial-e-previsoes/dia3_ex1_previsao_score_credito.py
     ```
   - **Dia 4 (Chatbot com IA em Streamlit e Hashzap em Flask):**
     ```bash
     # Para o Chatbot com IA (requer OPENAI_API_KEY configurada no ambiente):
     streamlit run dia4-criacao-de-chatbots-e-sistemas/dia4_ex1_chatbot_ia_streamlit.py

     # Para a demonstração das estruturas de histórico:
     python dia4-criacao-de-chatbots-e-sistemas/dia4_ex2_estruturas_chat_auxiliar.py

     # Para o chat em tempo real Hashzap (acesse http://localhost:5000):
     python dia4-criacao-de-chatbots-e-sistemas/dia4_ex3_chat_tempo_real_hashzap.py
     ```
