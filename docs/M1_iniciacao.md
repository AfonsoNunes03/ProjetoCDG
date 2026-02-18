
# Milestone 1: Iniciação e Definição do Projeto

## 1. Contexto e Problema de Negócio (Business Understanding)
A crise habitacional em Lisboa afeta tanto jovens como famílias de classe média e baixa, que enfrentam graves dificuldades em encontrar habitação a preços compatíveis com os seus rendimentos.

O Município de Lisboa e o Governo disponibilizam vários programas de apoio (Porta 65, Programa Renda Acessível, Subsídio Municipal ao Arrendamento), mas existe uma lacuna de informação sobre **quem são os candidatos que realmente se qualificam** para estes apoios e **quantas pessoas ficam "de fora"** (sem acesso ao mercado e sem acesso aos apoios).

### Pergunta Central do Projeto:
> **"Dada uma amostra de candidatos residentes (ou aspirantes a residentes) em Lisboa, qual a taxa de cobertura real dos atuais programas de apoio habitacional?"**

## 2. Objetivos SMART
Estes objetivos foram redefinidos para focar na análise de elegibilidade, abandonando a comparação com preços de mercado especulativos.

1.  **Objetivo 1 (Mapeamento de Regras):** Desenvolver um algoritmo capaz de replicar as regras de acesso dos 3 principais programas (Porta 65, PRA, SMAA) com 95% de precisão face à legislação, até à Milestone 3.
2.  **Objetivo 2 (Taxa de Cobertura):** Quantificar, para a amostra fornecida, a percentagem de candidatos elegíveis para pelo menos um apoio habitacional e caracterizar os perfis "excluídos", até ao final do semestre.
3.  **Objetivo 3 (Tipologia Familiar):** Identificar se as tipologias habitacionais disponíveis (T0-T4) são adequadas à dimensão dos agregados familiares candidatos da amostra.

### ✅ Auto-Correção (Checklist SMART)
- [x] **S (Específico):** O que vamos prever/analisar está claro? (Sim: Elegibilidade aos programas baseada em regras oficiais).
- [x] **M (Mensurável):** Definimos uma métrica? (Sim: Taxa de Cobertura e Precisão das regras).
- [x] **A (Atingível):** O nosso dataset permite isto? (Sim: Temos rendimentos, idade e agregado).
- [x] **R (Relevante):** Este objetivo é central para o tema? (Sim: Responde à crise habitacional).
- [x] **T (Temporal):** Está associado a um Milestone/Data? (Sim: Prazos definidos para M3).

## 3. Perguntas de Investigação (Data Science Questions)
Estas são as **3 perguntas** principais que os dados deverão responder ao longo do projeto:

1.  **Qual é a taxa real de cobertura dos programas habitacionais (Porta 65, PRA, SMAA) para esta amostra de candidatos?**
    *   *Variáveis:* Todas as regras de elegibilidade aplicadas à população.
2.  **Quais são os principais fatores socioeconómicos (Rendimento vs. Dimensão do Agregado vs. Idade) que levam à exclusão dos candidatos?**
    *   *Variáveis:* Rendimento Global, Nº Elementos, Idade.
3.  **Existe uma sobreposição significativa entre os públicos-alvo dos diferentes programas, ou eles servem segmentos distintos da população (Jovens vs. Famílias)?**
    *   *Variáveis:* Cruzamento entre os resultados de elegibilidade dos vários programas.



## 4. Metodologia de Gestão
O projeto seguirá o ciclo CRISP-DM, com as decisões documentadas no GitHub.
*   **Controlo de Versões:** Git Flow simplificado (`main` para entregas, `dev` para trabalho).
*   **Documentação:** Pasta `docs/` atualizada a cada Milestone.

## 5. Análise de Viabilidade dos Dados (Data Understanding)
- **Fonte:** Dataset `amostras_desafio.xlsx` (anonimizado, fornecido pela CML).
- **Volume:** ~100 registos iniciais (amostra representativa).
- **Variáveis Chave:**
    - `Rendimento Global`: Crucial para o cálculo da Taxa de Esforço.
    - `Nº Elem. Agregado`: Define a tipologia máxima permitida.
    - `Escalão Etário`: Define a elegibilidade para programas jovens (Porta 65).
    - `Concelho`: Define a elegibilidade geográfica (apenas Lisboa vs. AML).

## 6. Cronograma Estimado
| Fase | Prazo | Entregável |
| :--- | :--- | :--- |
| **M1: Iniciação** | 24 Fev | Definição de Regras e Setup do Repo. |
| **M2: Exploração** | TBD (Março) | Limpeza de Dados e EDA (Notebooks). |
| **M3: Modelação** | TBD (Abril) | Motor de Regras e Classificação de Elegibilidade. |
| **M4: Finalização**| TBD (Maio) | Dashboard e Relatório Final. |

---
*Data de última atualização: 18/02/2026*
