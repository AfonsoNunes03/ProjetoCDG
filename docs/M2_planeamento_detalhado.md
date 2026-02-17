
# Planeamento Detalhado do Projeto - Análise de Acesso à Habitação

## 1. Visão Geral e Objetivo
Este documento define o plano de trabalho revisado com base no feedback da coordenação (Professora). O foco principal é a análise de elegibilidade dos candidatos aos diferentes programas de apoio habitacional, utilizando exclusivamente os dados fornecidos (`amostrasdesafio0124`) e as regras oficiais (Legislação e Regulamentos), sem recorrer a comparações com o mercado de arrendamento privado.

O objetivo final é responder à questão: **Quais candidatos são elegíveis para quais programas e qual o tipo de apoio estimado (financeiro ou habitação)?**

## 2. Programas de Apoio Identificados
Com base na ficha de caracterização, os programas principais a analisar são:
- **Porta 65 Jovem**: Apoio financeiro ao arrendamento para jovens.
- **Porta 65+**: Apoio financeiro para idosos ou situações de vulnerabilidade.
- **Programa de Renda Acessível (PRA)**: Disponibilização de habitação a custos controlados.
- **1º Direito**: Apoio a famílias em condições habitacionais indignas (verificar aplicabilidade com os dados disponíveis).
- **Subsídio Municipal ao Arrendamento (SMA)**: Apoio direto ao arrendamento para famílias residentes em Lisboa.

## 3. Fases do Projeto

### Fase 1: Levantamento de Regras e Critérios (Imediato)
**Objetivo**: Transformar a legislação em lógica computacional.
- **Ação**: Pesquisar e documentar as regras específicas de cada programa (Lei/Portaria).
- **Entregável**: Documento `docs/regras_programas_detalhado.md` contendo para cada programa:
    - Limites de Idade.
    - Limites de Rendimento (Anual/Mensal, Bruto/Líquido).
    - Tipologia adequada ao agregado familiar.
    - Taxas de esforço permitidas ou exigidas.
    - Fórmula de cálculo do apoio (se aplicável).

### Fase 2: Mapeamento e Preparação de Dados
**Objetivo**: Preparar o dataset para ser processado pelas regras.
- **Análise das Colunas**:
    - `Escalão Etário`: Converter para intervalos numéricos (ex: "Menos 35 anos" -> `< 35`).
    - `Rendimento Global`: Normalizar valores.
    - `Nº Elem. Agregado` e `Nº Adultos`: Determinar tipologia necessária (T0, T1, etc.).
    - `Concelho`: Filtrar elegibilidade geográfica (Lisboa vs Outros).
- **Tratamento de Dados**: Criar script `prepare_data.py` que gera um DataFrame limpo e pronto para validação.

### Fase 3: Implementação da Lógica de Elegibilidade (Python)
**Objetivo**: Criar um motor de verificação de regras.
- **Estrutura do Código**:
    - Criar módulo `program_rules.py`.
    - Implementar classes para cada programa (ex: `class Porta65Jovem`).
    - Método `check_eligibility(candidato)` que retorna:
        - `is_eligible` (Bool)
        - `reason` (Lista de motivos de exclusão, se houver)
        - `estimated_support` (Valor estimado ou tipo de apoio)

### Fase 4: Análises e Insights
**Objetivo**: Gerar estatísticas baseadas na aplicação das regras aos dados.
- **Questões a responder**:
    1. Quantos candidatos do dataset são elegíveis para o Porta 65 Jovem?
    2. Quantos são elegíveis para o PRA?
    3. Existe sobreposição? (Candidatos elegíveis para ambos).
    4. Qual o percentual de candidatos que não se enquadram em nenhum programa? Porquê (Renda muito alta? Muito baixa? Idade?)?
    5. Distribuição geográfica dos elegíveis.

### Fase 5: Relatório Final
**Objetivo**: Compilar os resultados.
- Apresentar conclusões focadas na eficácia dos programas para a população amostrada.
- Sugestões ou notas sobre as lacunas encontradas (quem fica de fora).

## 4. Próximos Passos (Plano de Ação)
1.  **Ler a legislação** dos links identificados (Porta 65, Habitar Lisboa).
2.  **Criar o documento de regras** (`docs/regras_programas_detalhado.md`).
3.  **Atualizar o código** para importar e processar o dataset com estas novas regras.
