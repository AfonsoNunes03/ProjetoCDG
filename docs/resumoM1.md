
# Resumo Executivo - Milestone 1 (Iniciação)

Este documento resume o estado atual do projeto, a mudança de estratégia e as principais descobertas da análise inicial dos dados. Serve como guião para apresentação ao docente.

---

## 1. A Nova Estratégia (O "Pivot")
**O que mudou:** Inicialmente, a ideia era comparar os rendimentos dos candidatos com os preços do mercado imobiliário (dados do Idealista/Scraping). Essa abordagem foi abandonada por ser especulativa e tecnicamente instável.

**A Nova Lógica:** O projeto transformou-se num **"Auditor de Elegibilidade Habitacional"**.
*   **Foco:** Em vez de olhar para o mercado externo, olhamos para a **Lei**.
*   **Objetivo:** Cruzar cada candidato da amostra com as regras oficiais (Porta 65, PRA(preço por renda acessível), SMAA(Subsídio Municipal ao Arrendamento Acessível)).
*   **A Pergunta Central:** *"Se estas 100 famílias pedissem ajuda hoje, quantas teriam direito? E a que programa?"*

**Vantagem:** O resultado deixa de ser uma estimativa ("talvez consigam arrendar") para ser uma validação binária ("Têm direito / Não têm direito").

---

## 2. O que descobrimos nos Dados (Análise Exploratória M1)
A análise preliminar da amostra de 100 candidatos revelou três padrões críticos:

### A. Geografia (O Fator de Exclusão)
*   **O que vimos:** A maioria dos candidatos reside no concelho de **Lisboa**, mas existe uma parte significativa residente em concelhos limítrofes (Amadora, Odivelas, Sintra).
*   **Impacto no Projeto:** Os programas municipais (Programa Renda Acessível - PRA e Subsídio Municipal - SMAA) são exclusivos para residentes ou trabalhadores em Lisboa.
*   **Conclusão:** O algoritmo terá de excluir imediatamente os não-residentes destes programas específicos.

### B. Idade (O Potencial do Porta 65)
*   **O que vimos:** A amostra divide-se quase 50/50 entre "Jovens (< 35 anos)" e "Adultos (35-65 anos)".
*   **Impacto no Projeto:**
    *   Metade da amostra é candidata natural ao **Porta 65 Jovem**.
    *   A outra metade terá de concorrer ao **Porta 65+** (se existir verba) ou ao **PRA** (Renda Acessível).
    *   Isto valida a necessidade de ter regras separadas para jovens e adultos no nosso motor de decisão.

### C. Rendimentos (A Curva do Dinheiro)
*   **O que vimos:** A maioria dos agregados situa-se na faixa dos **10.000€ a 20.000€ anuais brutos**.
*   **Análise de Elegibilidade:**
    *   **Risco de Exclusão Inferior:** Quem ganha muito pouco (< 10.000€) pode ser excluído do PRA (que exige um mínimo para garantir o pagamento da renda) e empurrado para a Habitação Social (fora do âmbito deste projeto).
    *   **Risco de Exclusão Superior:** Quem ganha acima de 35.000€/45.000€ será excluído por excesso de rendimento.
    *   **Foco:** O projeto vai analisar a eficácia dos apoios para a "classe média-baixa" que está no meio desta distribuição.

---

## 3. Os Documentos Criados (Entregáveis M1)
A entrega da Milestone 1 é composta por:

1.  **`docs/M1_iniciacao.md`:** O Relatório Oficial. Define os Objetivos SMART atualizados (focados na elegibilidade).
2.  **`docs/regras_programas_oficiais.md`:** O Manual Técnico. Contém os valores exatos da lei (teto máximo de 45.000€, idade limite 35 anos) que serão programados.
3.  **`notebooks/1.0_eda_inicial.ipynb`:** O Notebook Jupyter com o código Python que carregou o Excel e gerou os gráficos.
4.  **`reports/figures/`:** A pasta com os gráficos gerados (PNGs) prontos a inserir no relatório final.

---

## 4. Próximos Passos (Para M2 e M3)
O caminho traçado para as próximas semanas:

1.  **Feature Engineering (M2):** Converter colunas de texto (ex: "Menos de 35 anos") em números (ex: `34`) para o computador processar.
2.  **Motor de Regras (M3):** Programar a lógica de decisão:
    *   `IF idade <= 35 AND rendimento < teto_porta65 THEN elegivel_porta65 = True`
    *   `IF concelho == 'Lisboa' AND taxa_esforco > 30% THEN elegivel_smaa = True`

---
*Documento gerado para apoio à apresentação e estudo do aluno.*
