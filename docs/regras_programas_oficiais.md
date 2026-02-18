
# Regras Oficiais dos Programas de Apoio à Habitação (Lisboa)

Este documento compila as regras técnicas de elegibilidade para os programas de habitação considerados no projeto, servindo de base para a implementação do motor de regras.

## 1. Porta 65 Jovem (Apoio Financeiro ao Arrendamento)
**Fonte:** Portaria n.º 277-A/2010 e Decreto-Lei n.º 42/2024.
**Objetivo:** Apoiar jovens no pagamento da renda de casa.

### 📝 Critérios de Elegibilidade
- **Idade:**
  - Jovens isolados: **18 a 35 anos** (inclusive).
  - Casais: Um dos elementos pode ter até **36 anos**, desde que o outro tenha até 35.
- **Residência:** Titular de contrato de arrendamento para residência permanente (morada fiscal coincidente).
- **Rendimento (Teto Máximo Mensal):**
  - O rendimento mensal corrigido do agregado não pode exceder **4x** a Retribuição Mínima Mensal Garantida (RMMG).
  - RMMG 2024 (aprox): 820€.
  - Teto Máximo: **3.280€/mês** (brutos).
- **Taxa de Esforço:**
  - A soma dos rendimentos brutos deve ser compatível com uma taxa de esforço máxima de **60%** (Renda / Rendimento Bruto <= 0.6).
- **Tipologia Adequada (Máxima):**
  - 1 a 2 pessoas: Até **T2**.
  - 3 pessoas: Até **T3**.
  - 4 a 5 pessoas: Até **T4**.

### ⚠️ Motivos de Exclusão Comuns
- Ser proprietário de outro imóvel.
- Ter dívidas a programas anteriores.
- Renda superior à **Renda Máxima de Referência** (RMR) definida por concelho.

## 2. Porta 65 + (Apoio a Quebra de Rendimentos)
**Fonte:** Linha 36 da Ficha de Caracterização / Portal da Habitação.
**Objetivo:** Apoiar famílias com quebra de rendimentos (>20%) ou monoparentais.

### 📝 Critérios de Elegibilidade
- **Público Alvo:**
  - Pessoas com quebra de rendimentos superior a 20% face aos 3 meses anteriores ou ano homólogo.
  - Famílias Monoparentais.
- **Rendimento:**
  - Rendimento mensal corrigido não pode exceder **4x** o Salário Mínimo (~3.280€/mês).
- **Taxa de Esforço:**
  - Máxima de **60%**.
- **Limites de Renda:**
  - Aplicam-se os mesmos tetos máximos de renda (RMR) do Porta 65 Jovem.

## 3. Programa Renda Acessível - PRA (Câmara Municipal de Lisboa)
**Fonte:** Regulamento do Programa Renda Acessível (CML).
**Objetivo:** Disponibilizar casas com rendas inferiores ao mercado para a classe média.

### 📝 Critérios de Elegibilidade
- **Rendimento Mínimo:**
  - O agregado deve ter capacidade financeira para pagar a renda.
  - Mínimo anual: **9.840€** (1 pessoa) ou aferido pela taxa de esforço mínima.
- **Rendimento Máximo (Anual Bruto):**
  - **1 pessoa:** Até **35.000€** (~2.500€/mês x 14).
  - **2 pessoas:** Até **45.000€** (~3.214€/mês x 14).
  - **+2 pessoas:** 45.000€ + **5.000€** por cada dependente adicional.
- **Taxa de Esforço Exigida:**
  - O valor da renda acessível deve representar entre **15% e 35%** do Rendimento Mensal Líquido (RML) do agregado.

### ⚠️ Motivos de Exclusão Comuns
- Ser proprietário de imóvel na Área Metropolitana de Lisboa.
- Ter dívidas ao município ou finanças.


## 4. Subsídio Municipal ao Arrendamento Acessível (SMAA)
**Fonte:** Regulamento Municipal do Direito à Habitação (CML).
**Objetivo:** Apoio financeiro a famílias com carência económica e rendas elevadas.

### 📝 Critérios de Elegibilidade
- **Residência:** Contrato de arrendamento em Lisboa.
- **Rendimento Global:**
  - Máximo de **35.000€/ano** (1 pessoa) ou **45.000€/ano** (2 pessoas).
- **Taxa de Esforço Atual:**
  - O agregado deve estar a gastar **mais de 30%** do seu rendimento líquido na renda atual.
- **Limites de Renda Aceites (Teto Máximo da Renda Atual):**
  - A renda que a família paga atualmente não pode ultrapassar:
    - **T0:** 600€
    - **T1:** 900€
    - **T2:** 1.150€
    - **T3:** 1.375€
    - **T4:** 1.550€

## 5. Nota sobre o Programa 1º Direito (Linha 37)
Embora listado na Ficha de Caracterização, o programa **1º Direito** destina-se a famílias que vivem em condições habitacionais indignas (precariedade, insalubridade, insegurança, sobrelotação).
Como o dataset fornecido (`amostras_desafio.xlsx`) **não contém informação sobre as condições físicas da habitação atual** dos candidatos, não é tecnicamente possível calcular a elegibilidade para este programa com rigor. Será excluído do algoritmo principal, focando-se a análise nos critérios financeiros e demográficos.

## Resumo Comparativo para o Algoritmo

| Critério | Porta 65 Jovem | Porta 65 + | Renda Acessível (PRA) | SMAA (Subsídio) |
| :--- | :--- | :--- | :--- | :--- |
| **Idade** | 18-35 anos | Qualquer (foco quebra/monoparental) | > 18 anos | > 18 anos |
| **Rendimento Max** | ~3.280€/mês (Bruto) | ~3.280€/mês (Bruto) | 35k-45k/ano (Bruto) | 35k-45k/ano (Bruto) |
| **Fator Chave** | Jovens | Quebra Rendimento | Classe Média | Taxa de Esforço Elevada (>30%) |
| **Tipo de Apoio** | Financeiro | Financeiro | Casa com Renda Reduzida | Financeiro (Diferencial) |
