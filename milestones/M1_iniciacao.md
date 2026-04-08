# Milestone 1: Iniciação — Versão Final (Foco em IA)
> Revisão estratégica baseada no feedback da Professora Dora Melo (Abril 2026)

---

## 1. Título do Projeto

**Predição de Elegibilidade Habitacional em Lisboa: Um Modelo de Classificação Supervisionado para Identificação de Perfis de Candidatos**

---

## 2. Questão SMART (Objetivo Principal)

> "Desenvolver um **modelo de classificação supervisionado** que, utilizando os dados socioeconómicos da Plataforma Habitar Lisboa, seja capaz de prever a elegibilidade dos candidatos aos programas municipais com um **F1-Score (taxa de sucesso) superior a 80%**, identificando simultaneamente a importância das variáveis (rendimento, idade, agregado) na exclusão dos candidatos, a concluir até maio de 2026."

| Critério SMART | Descrição e Cumprimento |
|:---|:---|
| **S — Específico** | Criar um classificador supervisionado para prever elegibilidade (Elegível/Inelegível) sem que o modelo conheça as regras a priori. |
| **M — Mensurável** | Atingir uma performance mínima de **80% de F1-Score/Recall** no conjunto de teste. |
| **A — Atingível** | Utilização de variáveis críticas (Rendimento, Idade, Agregado) e Ground Truth gerado pelo Motor de Regras (Oracle). |
| **R — Relevante** | Automatização da triagem municipal e identificação das variáveis que mais pesam no "funil burocrático". |
| **T — Temporal** | Cronograma de entrega final para a Milestone 4 em maio de 2026. |

---

## 3. Perguntas de Investigação

1. **Classificação:** É possível treinar um modelo supervisionado que aprenda as fronteiras de elegibilidade legislativa com um erro inferior a 20%?
2. **Importância das Variáveis:** Quais as características (características do agregado) que apresentam maior peso estatístico na decisão de elegibilidade?
3. **Métricas:** Qual o desempenho do modelo em termos de F1-Score e Recall para garantir que o sistema identifica o maior número de elegíveis possível?
4. **Generalização:** O modelo consegue classificar corretamente um "novo candidato" (automação) mantendo a estabilidade via Cross-Validation?

---

## 4. Metodologia: O Ciclo de Modelação (A Pedido da Professora)

Para cumprir o objetivo, o projeto segue este plano técnico:

1. **O Motor de Regras (Ground Truth):** Criar uma função em Python que aplica as regras de decisão legais (Porta 65, PRA, SMAA, PAA) de forma 100% rigorosa. Esta função cria a variável de resposta (Elegível/Inelegível) para cada caso.
2. **Aprendizagem Supervisionada:** Pegar nos dados rotulados pelo motor, dividir em conjuntos de **Treino e Teste**, e aplicar algoritmos (Decision Tree / Random Forest) que tentam "adivinhar" o resultado sem ver o código das regras.
3. **Avaliação Crítica:** Usar medidas de desempenho (Accuracy > 80%, F1, Recall) e validação cruzada (**Cross-Validation**) para garantir a robustez.
4. **Interpretabilidade:** Extrair a importância das variáveis para ordenar os fatores que mais influenciam a elegibilidade.

---

## 5. Dicionário de Dados

### Dataset Principal — Plataforma Habitar Lisboa (PHL)

| Variável | Descrição | Papel no Modelo |
|:---|:---|:---|
| `Rendimento_Anual` | Rendimento anual bruto (€) | Feature de maior peso (contínua) |
| `Idade_Media` | Valor numérico derivado do escalão etário | Feature crítica para programas jovens |
| `N_Elem_Agregado` | Número de elementos no agregado familiar | Feature que define os tetos de rendimento |
| `Target_Elegivel` | Classe (Elegível=1 / Inelegível=0) | **Variável Alvo** (Gerada pelo Motor de Regras) |

---

## 6. Cronograma de Execução

| Fase | Entrega | Estado |
|:---|:---|:---|
| **M1: Iniciação** | Abr 2026 | ✅ Finalizado |
| **M2: Exploração** | Abr 2026 | ✅ Finalizado |
| **M3: Modelação (IA)** | Abr/Mai 2026 | 🔄 Em curso (Sucesso atual: 99.2%) |
| **M4: Finalização** | Mai 2026 | 🔒 Pendente |

---
*Versão Final — Alinhada com os requisitos de IA Supervisionada*
