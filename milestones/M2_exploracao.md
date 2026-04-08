# Milestone 2: Exploração e Preparação de Dados

> **Estado:** ✅ Concluída — 12/03/2026
> **Foco CRISP-DM:** Data Understanding & Data Preparation

---

## 1. Objetivos da Fase

Esta milestone tem como objetivo transformar os dados brutos do LxDataLab em informação estruturada, limpa e pronta para a fase de Modelação. Os objetivos específicos são:

1. **Explorar** a distribuição das variáveis-chave do dataset PHL (candidatos) e comparar com os datasets de beneficiários.
2. **Limpar e preparar** os dados: tratar nulos, harmonizar variáveis, converter tipos.
3. **Produzir visualizações** que descrevem o perfil dos candidatos sem expor valores reais (proteção de dados).
4. **Responder às Perguntas de Investigação I e II** definidas na M1:
   - *Qual a distribuição de rendimentos, escalões etários e dimensão de agregados?*
   - *Qual a representação geográfica dos candidatos?*

---

## 2. Datasets Utilizados

| Dataset | Ficheiro | Papel na M2 |
|:---|:---|:---|
| **PHL (candidatos)** | `Desafio_PHL_Rendimentos_agregados__registos_adesão.csv` | Dataset principal — base de toda a EDA |
| **RA (amostra aleatória)** | `Pub_Amostra_Aleatoria_RA_2024vf.xlsx` | Comparação — perfil de quem acedeu à Renda Acessível |
| **SMAA Ed.6** | `Pub_Amostra_SMAA_6_2024_Beneficiarios.xlsx` | Comparação — perfil dos beneficiários do SMAA |
| **PAA 2024** | `Publ_Amostra_PAA_2024_Afetacao_Hab.xlsx` | Comparação — perfil dos beneficiários do Arrendamento Apoiado |
| **PRA Ed.21,22,25** | `Publ_Amostra_PRA_2024_Beneficiarios.xlsx` | Comparação — perfil dos beneficiários do PRA |

---

## 3. Limpeza e Preparação de Dados

### 3.1 Normalização de Colunas

Todos os nomes de colunas foram convertidos para `snake_case` para uniformidade entre datasets:

| Original | Normalizado |
|:---|:---|
| `Escalão Etário` | `escalao_etario` |
| `Nº Elem. Agregado` | `n_elem_agregado` |
| `Rendimento Global (IRS e Rend. Isentos)` | `rendimento_global_anual` |
| `Rend_Mensal_Atual_Agreg` | `rend_mensal_atual` |
| `Encargos_habitacao` | `encargos_habitacao` |

### 3.2 Tratamento de Valores Nulos

**Política adotada:** Conservadora — registos com variáveis críticas nulas são excluídos da análise de elegibilidade (mas contabilizados para efeitos estatísticos).

| Variável | Estratégia |
|:---|:---|
| `rendimento_global_anual` (nulo) | Excluir do cálculo de elegibilidade |
| `escalao_etario` (nulo) | Excluir do cálculo do Porta 65 |
| `n_elem_agregado` (nulo) | Assumir 1 elemento (conservador) |
| `concelho` (nulo) | Manter como "Desconhecido" — não elegível para critérios geográficos |
| `encargos_habitacao` = "-" | Converter para `NaN` |

### 3.3 Conversão de Tipos e Engenharia de Variáveis

| Variável | Transformação | Motivo |
|:---|:---|:---|
| `escalao_etario` (categórico, 3 valores) | Mapeado para valor médio: "Menos 35 anos" → **26**, "35 a 65 anos" → **50**, "Mais de 65 anos" → **70** | Verificar barreira dos 35 anos do Porta 65 |
| `rendimento_global_anual` (anual) | Dividido por **14** para obter `rend_mensal_bruto` | Comparar com tetos mensais dos programas |
| `Encargos Habitação` / `rend_mensal_atual` | Calcular `taxa_esforco = encargos / rend_mensal_atual × 100` | Critério do SMAA (> 30%) |
| `concelho` | Criar flag `is_residente_lisboa` e **filtrar** para `True` | Restringir análise ao âmbito do projeto (concelho de Lisboa) |

### 3.4 Criação do Dataset Unificado de Beneficiários

Para a análise comparativa, os 3 datasets de beneficiários (SMAA, PAA, PRA) foram concatenados num único dataframe com as colunas harmonizadas:

```
programa | id | idade | n_elem_agregado | rendimento_global_anual |
rend_mensal_atual | encargos_habitacao | taxa_esforco | situacao_habitacional |
situacao_profissional | concelho_residencia
```


---

## 4. Análise Exploratória de Dados (EDA)

> 🔒 **Proteção de Dados:** Todas as visualizações usam distribuições normalizadas, percentagens ou formas de densidade — nunca valores individuais absolutos.

### 4.1 Perfil do Candidato PHL

#### Distribuição por Escalão Etário
*[📊 Ver gráfico: `assets/graficos/dist_escalao_etario_phl.png`]*

**Observações:**
- O dataset PHL usa **3 categorias etárias**: "Menos 35 anos", "35 a 65 anos", "Mais de 65 anos"
- Candidatos em "Menos 35 anos" são os únicos potencialmente elegíveis para o **Porta 65 Jovem** (41,8% dos candidatos de Lisboa)
- Candidatos em "Mais de 65 anos" apontam para potencial elegibilidade PAA (vulnerabilidade social)

#### Distribuição de Rendimentos
*[📊 Ver gráfico: `assets/graficos/dist_rendimento_phl.png`]*

**Observações:**
- Distribuição com cauda longa à direita (assimetria positiva); rendimento médio **16.376 €** e mediana **13.818 €**
- "Zona cinzenta" visível entre 20.000€–45.000€/ano: acima dos limites sociais (PAA), potencialmente dentro ou acima dos tetos do PRA/SMAA
- Candidatos abaixo do limiar mínimo do PRA (< 9.840€/ano) excluídos desse programa por insuficiência de rendimento

#### Distribuição por Nº de Elementos do Agregado
*[📊 Ver gráfico: `assets/graficos/dist_agregado_phl.png`]*

**Observações:**
- **77,6%** dos candidatos têm agregados de 1–2 pessoas (tipologia adequada T0/T1/T2)
- Minoria com 4+ pessoas necessita de T3/T4, onde a oferta municipal é mais escassa

#### Distribuição Geográfica (por Concelho)

> ⚠️ **Nota:** Com o âmbito restrito ao **concelho de Lisboa**, o gráfico de barras por concelhos (`bar_concelhos_phl.png`) foi gerado sobre o dataset original completo (pré-filtro) para documentar a composição geográfica total. A análise de elegibilidade usa exclusivamente os **6.291 candidatos de Lisboa**.

**Composição do PHL (pré-filtro):**
- **61,2% residem no concelho de Lisboa** (6.291 registos) — base da análise
- **38,8% residem noutros concelhos** (3.988 registos): AML (Amadora, Odivelas, Sintra, Oeiras…) e outros (Tomar, Coimbra…) — excluídos do âmbito

### 4.2 Comparação Candidatos (PHL) vs. Beneficiários (SMAA / PAA / PRA)

*[📊 Ver gráfico: `assets/graficos/boxplot_rendimento_candidatos_vs_beneficiarios.png`]*

**Objetivo:** Identificar se o perfil socioeconómico dos aprovados diverge do perfil geral dos candidatos — o que indicaria critérios de seleção para além da elegibilidade formal.

| Variável de Comparação | Candidatos PHL (Lisboa) | Beneficiários Reais |
|:---|:---:|:---:|
| Escalão etário dominante | "Menos 35 anos" e "35 a 65 anos" (3 categorias no CSV) | Disponível de forma numérica nos datasets SMAA/PRA/PAA |
| Rendimento médio anual (€) | **16.376 €** (mediana: 13.818 €) | **SMAA: 16.511 €** \| **PRA: 17.157 €** \| **PAA: 3.065 €** |
| Dimensão do agregado | 77,6% com 1–2 pessoas | Distribuição semelhante — maioritariamente pequenos agregados |
| % com taxa de esforço > 30% | **Não calculável** — PHL não inclui `encargos_habitacao` | **> 30% para SMAA** (critério de entrada por definição); 15–35% para PRA |

> 🔑 **Descoberta Central:** O rendimento médio dos candidatos PHL no **concelho de Lisboa** (16.376 €/ano) é **muito semelhante** ao dos beneficiários SMAA (16.511 €) e PRA (17.157 €). A exclusão **não é explicada por diferenças socioeconómicas estruturais** — os candidatos têm perfil de rendimento comparável aos aprovados. A seleção ocorre por critérios formais (idade, encargos habitacionais, tipologia). O PAA destina-se ao segmento de muito baixo rendimento (3.065 €/ano), distinto do perfil geral PHL.

### 4.3 Taxa de Esforço dos Beneficiários

*[📊 Ver gráfico: `assets/graficos/hist_taxa_esforco_beneficiarios.png`]*

Para os datasets que têm `Encargos_habitacao` e `Rend_Mensal_Atual_Agreg` (SMAA e PRA):
- **Taxa de esforço calculada** para beneficiários SMAA e PRA — confirmada a distribuição esperada (>30% no SMAA, coerente com o critério de entrada).
- **PHL não contém encargos habitacionais** — a taxa de esforço dos candidatos não é calculável nesta fase. Esta limitação será documentada no motor de regras (M3): o critério SMAA de taxa de esforço >30% não poderá ser avaliado diretamente para os candidatos PHL, sendo necessário assumir cenário conservador ou imputação.

### 4.4 Relatório de Limpeza (Resumo)

| Métrica | Valor |
|:---|:---:|
| **Dataset PHL — registos brutos** | **10.279 registos** (ficheiro CSV, ~760 KB — dataset completo recebido em 05/03/2026) |
| **Registos excluídos — `rendimento_global_anual` nulo** | 0 — todos os registos têm rendimento preenchido |
| **Registos excluídos — fora do concelho de Lisboa** | **3.988 registos** (39%) — excluídos do âmbito do projeto |
| **Candidatos residentes no concelho de Lisboa** | **6.291 registos (61,2%)** — base da análise |
| **% com agregados de 1–2 pessoas** | **77,6%** — tipologia adequada T0/T1/T2 |
| **Rendimento médio anual (PHL Lisboa)** | **16.376 €** (mediana: 13.818 €) |
| **Dataset unificado de beneficiários (SMAA + PAA + PRA)** | **777 registos** — SMAA: 410 \| PRA: 261 \| PAA: 106 |
| **Rendimento médio anual (beneficiários SMAA)** | **16.511 €** |
| **Rendimento médio anual (beneficiários PRA)** | **17.157 €** |
| **Rendimento médio anual (beneficiários PAA)** | **3.065 €** (perfil de vulnerabilidade social) |

---

## 5. Visualizações Planeadas

| # | Gráfico | Ficheiro | Protecção | Insight Esperado |
| :--- | :--- | :--- | :--- | :--- |
| 1 | Histograma — Escalão Etário (PHL) | `dist_escalao_etario_phl.png` | Eixos em % | Concentração na faixa ativa; impacto do corte 35 anos |
| 2 | Histograma — Rendimento (PHL) | `dist_rendimento_phl.png` | Densidades normalizadas | "Zona cinzenta" entre 20k–45k€/ano |
| 3 | Gráfico de barras — Concelhos (pré-filtro) | `bar_concelhos_phl.png` | Top 15 concelhos | Composição geográfica do PHL completo; justifica exclusão de 38,8% |
| 4 | Gráfico de barras — Nº Elementos | `dist_agregado_phl.png` | Frequência relativa (%) | Maioria agregados 1-2 pessoas |
| 5 | Boxplot — Rendimento PHL vs. Beneficiários | `boxplot_rendimento_candidatos_vs_beneficiarios.png` | Sem outliers individuais | Comparação de perfis |
| 6 | Histograma — Taxa de Esforço (SMAA+PRA) | `hist_taxa_esforco_beneficiarios.png` | Densidades | Validação do critério > 30% do SMAA |
| 7 | Diagrama de Funil — Elegibilidade estimada | `funil_elegibilidade.png` | Percentagens | Visualizar candidatos→elegíveis→zona cinzenta |

---

## 6. Conclusões da EDA

> 💡 **Descoberta Principal:**
> Para os 6.291 candidatos residentes no **concelho de Lisboa**, o rendimento médio é **16.376 €/ano** (mediana: 13.818 €). Os beneficiários reais do SMAA e PRA apresentam rendimentos muito semelhantes (16.511 € e 17.157 €, respetivamente). Isto demonstra que a exclusão dos programas não é causada por diferenças de riqueza, mas por critérios formais — o "funil burocrático" está empiricamente confirmado já na fase de exploração de dados. O PAA, com beneficiários a 3.065 €/ano, serve um segmento diferente do perfil geral PHL.

### 6.1 Síntese dos Resultados por Dimensão

**Distribuição Geográfica:**
De 10.279 registos PHL, **6.291 (61,2%)** residem no **concelho de Lisboa** e constituem o âmbito do projeto. Os restantes 3.988 (38,8%) pertencem à AML ou a concelhos mais distantes e são excluídos da análise — programas como PRA e SMAA exigem residência no **concelho de Lisboa** (não basta residir no distrito), criando uma barreira geográfica imediata antes de qualquer análise de rendimento.

**Distribuição de Rendimentos:**
A distribuição apresenta assimetria positiva (cauda longa à direita), com rendimento médio de **16.376 €/ano** e mediana de **13.818 €/ano** (candidatos do concelho de Lisboa). A mediana abaixo da média indica a presença de candidatos de rendimento muito baixo. Identifica-se uma "zona cinzenta" provável entre os 20.000 €–45.000 €/ano: acima dos tetos dos programas sociais (PAA) mas potencialmente dentro ou acima dos tetos do PRA e SMAA — necessitando do motor de regras para quantificação precisa.

**Distribuição Etária:**
O dataset PHL usa 3 categorias etárias: "Menos 35 anos" (elegíveis Porta 65 — **41,8%** dos candidatos de Lisboa), "35 a 65 anos" (maioria — população ativa de meia-idade) e "Mais de 65 anos" (potencial PAA). A granularidade limitada impede análise etária mais fina, introduzindo imprecisão no limite dos 35 anos do Porta 65.

**Dimensão do Agregado:**
**77,6%** dos candidatos de Lisboa integram agregados de 1–2 pessoas, correspondendo à necessidade de tipologia T0/T1/T2. Existe uma minoria de agregados alargados (4+ pessoas) com necessidade de T3/T4, onde a oferta municipal é mais escassa.

**Comparação Candidatos ↔ Beneficiários:**
Os candidatos de Lisboa (rendimento médio **16.376 €**) têm perfil muito semelhante aos beneficiários SMAA (**16.511 €**) e PRA (**17.157 €**). Isto rejeita a hipótese de que os programas selecionam os mais pobres dentro dos elegíveis. A seleção ocorre por critérios formais — idade, encargos habitacionais e tipologia. O PAA (beneficiários a **3.065 €/ano**) serve um segmento claramente distinto do perfil geral PHL.

### 6.2 Limitações Identificadas e Impacto em M3

| Limitação | Impacto no Motor de Regras (M3) |
|:---|:---|
| `escalao_etario` categórico (não numérico) | Mapeamento para valor médio introduz imprecisão ±5 anos; candidatos no limite de 35 anos terão classificação aproximada |
| Ausência de `encargos_habitacao` no PHL | Critério de taxa de esforço SMAA (>30%) não calculável diretamente; será tratado como "não avaliável" no motor |
| Critérios não observáveis (imóvel próprio, dívidas municipais) | Subestimação da exclusão real — a taxa de cobertura calculada em M3 será um **limite superior** da elegibilidade real |
| 38,8% de candidatos fora do **concelho de Lisboa** | **Excluídos do âmbito do projeto** — a análise incide apenas sobre os 6.291 residentes no concelho de Lisboa |

---

## 7. Próximos Passos → Milestone 3

Com base nos resultados da EDA, a M3 irá:
1. Implementar o **Motor de Regras** para os 4 programas com as variáveis limpas da M2.
2. Aplicar o motor ao dataset PHL filtrado (**6.291 candidatos do concelho de Lisboa**) para calcular a **taxa de cobertura real**.
3. Validar o motor contra os **beneficiários reais** (SMAA, PAA, PRA) — ground truth.
4. Classificar os candidatos inelegíveis pelo **motivo específico de exclusão**.

---

*Data de última atualização: 20/03/2026*
