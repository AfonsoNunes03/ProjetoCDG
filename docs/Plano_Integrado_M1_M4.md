
# Plano Integrado do Projeto (Milestone 1, 2, 3 e 4)

Este documento detalha o plano de execução para o projeto "Análise de Elegibilidade aos Programas de Apoio Habitacional de Lisboa", alinhado com o guião da disciplina e o feedback da Professora.

---

## 📅 Roadmap Global (Resumo)

| Milestone | Foco Principal | Prazo |
| :--- | :--- | :--- |
| **M1: Iniciação** | Business & Data Understanding (Regras & Dados) | 24/02/2026 |
| **M2: Exploração** | Data Preparation & Análise EDA | TBD (Semana 4-7) |
| **M3: Modelação** | Aplicação das Regras (Motor de Elegibilidade) | TBD (Semana 8-12) |
| **M4: Finalização**| Interpretação, Dashboard e Relatório Final | TBD (Semana 13-15) |

---

## 🚀 Milestone 1: Iniciação (Business & Data Understanding)
**Prazo:** 24/02/2026

### Objetivos Específicos (SMART)
1. **Definir o Problema:** Aferir a elegibilidade dos candidatos da amostra aos programas de habitação municipais/nacionais, sem recorrer a dados de mercado externo.
2. **Setup do Projeto:** Repositório GitHub organizado conforme guião.
3. **Análise Preliminar:** Caracterização estatística básica da amostra (distribuição de rendimentos, idades, localidades).

### Tarefas Detalhadas (Checklist M1)
#### 1. Business Understanding (O que é para fazer?)
- [x] **Ler Feedback da Professora:** Abandonar comparação de preços de mercado. Focar nas Regras Oficiais.
- [x] **Levantamento de Regras:** Criar documento `docs/regras_programas_oficiais.md` com:
    - [x] Regras Porta 65 Jovem (Idade, Rendimentos, Taxa Esforço).
    - [x] Regras Porta 65 + (Idade, Rendimentos).
    - [x] Regras PRA - Programa Renda Acessível (Escalões de rendimento, Tipologias).
    - [x] Regras SMA - Subsídio Municipal ao Arrendamento.
- [x] **Preenchimento do Template:** Completar `docs/M1_iniciacao.md` com a nova visão do projeto.

#### 2. Setup Técnico (Infraestrutura)
- [x] Repositório Criado.
- [x] **Estrutura de Pastas Refinada:**
    - Garantir existência de `data/raw`, `data/processed`, `notebooks`, `src`, `docs`, `reports/figures`.
    - Garantir `.gitignore` correto (ignorar venv, .DS_Store, caches).
- [x] **README.md Final:** Atualizar para refletir o novo objetivo do projeto (foco na elegibilidade).

#### 3. Data Understanding (O que temos?)
- [x] **Notebook de Inspeção (`notebooks/1.0_eda_inicial.ipynb`):**
    - [x] Carregar `amostras_desafio.xlsx`.
    - [x] `df.info()`, `df.describe()`.
    - [x] Verificar nulos e tipos de dados.
    - [x] Analisar distribuição geográfica (Lisboa vs Outros Concelhos).
    - [x] **Output:** Secção "Descrição dos Dados" no `docs/M1_iniciacao.md` e Gráficos em `reports/figures/`.

---

## 🔍 Milestone 2: Exploração (Data Preparation & EDA)
**Foco:** Limpar os dados para que possam ser processados pelas regras.

### Tarefas Principais
1. **Limpeza de Dados (`src/data_cleaning.py`):**
    - Tratar valores nulos (se existirem).
    - Normalizar nomes de Concelhos.
2. **Feature Engineering (Transformação):**
    - Converter `Escalão Etário` (texto) para `Idade Mínima/Máxima` (int).
    - Converter `Rendimento Global` para numérico (float).
    - Derivar `Tipologia Necessária` baseado no `Nº Elem. Agregado` (ex: 1 pessoa -> T0/T1).
3. **Análise Exploratória (EDA):**
    - Gráficos de distribuição de rendimento.
    - Gráficos de composição do agregado familiar.
    - Matriz de correlação (se aplicável).

---

## ⚙️ Milestone 3: Modelação (Implementation of Rules)
**Foco:** O "Modelo" neste projeto é o Motor de Regras (Rule-Based System).

### Tarefas Principais
1. **Desenvolver Motor de Regras (`src/eligibility_engine.py`):**
    - Função `check_porta65(age, income, household_size) -> bool`.
    - Função `check_pra(income, household_size) -> bool`.
    - Função `check_sma(...) -> bool`.
2. **Aplicação ao Dataset:**
    - Correr o motor sobre cada linha do dataset tratado.
    - Criar novas colunas: `Eligivel_Porta65`, `Eligivel_PRA`, `Motivo_Exclusao`.
3. **Validação:**
    - Testar com casos extremos (rendimento 0, rendimento muito alto, idades limite).

---

## 📊 Milestone 4: Finalização (Deployment & Reporting)
**Foco:** Comunicar os resultados.

### Tarefas Principais
1. **Dashboard / Relatório Visual:**
    - Quantos % são elegíveis para cada programa?
    - Quem fica de fora? (Análise dos excluídos).
2. **Relatório Final (`docs/M4_conclusoes.md`):**
    - Resumo dos findings.
    - Recomendações (ex: "O programa X deveria ajustar o limite Y para abranger mais Z% da amostra").
3. **Apresentação Final:** Slides e Pitch.

---

## Ações Concluídas (Milestone 1)
- [x] Criado `docs/regras_programas_oficiais.md` com pesquisa de legislação (Porta 65, PRA, SMAA).
- [x] Atualizado `docs/M1_iniciacao.md` com Objetivos SMART focados na elegibilidade.
- [x] Configurado repositório GitHub com estrutura profissional (`data/`, `notebooks/`, `src/`).
- [x] Criado notebook `1.0_eda_inicial.ipynb` e gerados gráficos de análise preliminar.
- [x] Criado `docs/resumoM1.md` para apoio à apresentação.

## Próximos Passos (Início da Milestone 2)
1.  **Limpeza de Dados:** Criar script para normalizar nomes de concelhos e remover espaços.
2.  **Transformação:** Converter intervalos de idade ("Menos de 35") em números (34).
