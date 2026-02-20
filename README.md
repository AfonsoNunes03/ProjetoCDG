# Projeto Desafio Habitação: Análise de Elegibilidade e Acesso

## Identificação da Equipa
* **Grupo nº:** 2
* **Membros:**
  * Afonso Nunes - 2023141213
  * Guilherme Ventura - 2023132296
  * Duarte Ribeiro - 2023142440

## 📂 Organização do Portfólio de Resultados 

Este repositório funciona como uma **Wiki de Projeto**, documentando as decisões e resultados
sem exposição de dados sensíveis ou código proprietário:
* **`milestones/`**: Documentação técnica detalhada de cada etapa do projeto.
* **`assets/`**: Repositório de evidências visuais, dividido em `graficos/`, `diagramas/` e
`tabelas/`.
* **`.gitignore`**: Filtro de segurança que impede a submissão acidental de dados brutos ou
scripts.
---

## 1. Iniciação (Milestone 1)
### Contexto e Problema de Negócio
O projeto analisa o "Acesso Económico à Habitação no Concelho de Lisboa" através da exploração de dados reais da plataforma municipal "Habitar Lisboa". O objetivo central é traçar o perfil socioeconómico das famílias que procuram apoio (analisando variáveis como o rendimento global, a idade e a dimensão do agregado) e cruzar essa caracterização com os critérios de elegibilidade do Regulamento Municipal do Direito à Habitação.

A relevância deste estudo é simultaneamente social e estratégica. A nível social, permite identificar e quantificar a real vulnerabilidade de grupos demográficos específicos, como jovens e famílias numerosas, perante a atual crise habitacional. A nível estratégico, o projeto fornece à Câmara Municipal de Lisboa indicadores essenciais para apoiar uma gestão baseada em evidências (data-driven). Ao compreender o perfil exato de quem efetivamente procura apoio e ao verificar se as regras municipais atuais se adequam à realidade destes requerentes, o trabalho contribui diretamente para a otimização dos programas de habitação e para um planeamento urbano mais inclusivo.

### Objetivos do Projeto
* **Objetivo 1:** Caracterizar o Perfil da Procura: Analisar os dados da plataforma "Habitar Lisboa" para identificar exatamente quem procura apoio habitacional.
* **Objetivo 2:** Validar a Elegibilidade: Cruzar o rendimento dos candidatos com os limites legais do Regulamento Municipal.
👉 **[Consulta a Documentação Completa do Milestone 1](milestones/M1_iniciacao.md)**
---
## 2. Exploração (Milestone 2)
### Principais Conclusões (EDA)
> *Dica: Insere aqui o gráfico mais importante do projeto que resume a tua descoberta principal.*
> ![Gráfico de Destaque](assets/graficos/insight_principal.png)
* **Conclusão Chave:** [Ex: Verificámos que 80% das falhas ocorrem em equipamentos com mais de
5 anos de operação, sem manutenção preventiva.]
👉 **[Consulta a Documentação Completa do Milestone 2](milestones/M2_exploracao.md)**
---
## 3. Modelação (Milestone 3)
### Desempenho do Modelo
| Modelo | Métrica (F1-Score) | Tempo de Treino |
| :--- | :--- | :--- |
| Baseline (LogReg) | 0.72 | 1.2s |
| **XGBoost (Final)** | **0.89** | **5.4s** |
* **Nota:** O modelo final foi selecionado pelo equilíbrio entre precisão e capacidade de
generalização.
👉 **[Consulta a Documentação Completa do Milestone 3](milestones/M3_modelacao.md)**
---
## 4. Finalização (Milestone 4)
### Resposta ao Problema
[Explica como os resultados obtidos respondem à pergunta inicial do Milestone 1. Qual o impacto
prático desta solução?]
### Recomendações e Inovação
1. [Sugestão de melhoria ou automação baseada nos dados analisados.]
👉 **[Consulta a Documentação Completa do Milestone 4](milestones/M4_finalizacao.md)**
---
**Instituição:** Coimbra Business School | ISCAC
**Curso:** Licenciatura em Ciência de Dados para a Gestão
**Unidade Curricular:** Projeto em Ciência de Dados
**Professor Responsável:** Dora Melo (dmelo@iscac.pt) 

## ⚠ Nota de Confidencialidade
Este repositório foi construído exclusivamente para fins de **portfólio e documentação de
resultados**. Por questões de proteção de dados e propriedade intelectual, este repositório **não
contém**:
1. Dados brutos (datasets originais).
2. Código-fonte proprietário da implementação.
3. Informação sensível de clientes ou parceiros.
