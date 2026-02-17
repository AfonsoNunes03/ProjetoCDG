# Milestone 1: Iniciação e Compreensão dos Dados

## 1. Business Understanding (Compreensão do Negócio)

### 1.1. Definição do Problema
O acesso à habitação em Lisboa tornou-se um desafio crítico devido ao aumento dos preços de imobiliário (venda e arrendamento) que não foi acompanhado por um crescimento proporcional dos rendimentos das famílias. Existe uma necessidade premente de identificar o "gap" de acessibilidade e caracterizar os perfis populacionais mais afetados.

### 1.2. Objetivos do Projeto
**Objetivo SMART:**
> Desenvolver, até ao final do semestre, um modelo de análise que cruze dados de rendimento familiar (amostra de adesão) com dados de mercado imobiliário público (INE/Web Scraping), permitindo calcular um "Índice de Acessibilidade" por freguesia e tipologia familiar.

### 1.3. Critérios de Sucesso
- Caracterização completa da amostra de candidatos fornecida.
- Integração bem-sucedida com dados externos (INE).
- Criação de visualizações claras sobre a distribuição de rendimentos vs. custos habitacionais.

---

## 2. Data Understanding (Compreensão dos Dados)

### 2.1. Fontes de Dados Iniciais
- **Amostra Desafio (Interna):** Dados anonimizados de candidatos a programas de habitação, contendo variáveis socioeconómicas, composição do agregado e rendimentos.
- **Dados Externos (INE):** Estatísticas de rendas e preços de venda por m².

### 2.2. Exploração Inicial (Resumo da Amostra)
**Análise Preliminar (Baseada em 100 registos):**
- **Dimensão:** 100 linhas (candidatos) e 8 colunas.
- **Geografia:** A maioria dos candidatos reside no concelho de Lisboa (61%), mas há representação de outros 18 concelhos (ex: Amadora, Sintra, Loures), o que levanta questões sobre a elegibilidade para programas municipais.
- **Perfil Etário:**
    - População Jovem (< 35 anos): 46% (Forte candidato ao Porta 65 Jovem).
    - Adultos (35-65 anos): 47%.
    - Seniores (> 65 anos): 7%.
- **Dimensão do Agregado:**
    - Predominância de agregados singulares (56%) e de 2 pessoas (24%).
- **Rendimentos (Valores Anuais):**
    - **Média:** €14.730,70
    - **Mediana:** €12.778,40
    - Estes valores sugerem que uma grande parte da amostra se enquadra nos limites de rendimento para habitação acessível.
