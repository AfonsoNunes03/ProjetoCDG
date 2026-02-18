# Projeto Desafio Habitação: Análise de Elegibilidade e Acesso

## Identificação da Equipa 
* **Grupo nº:** 2 
* **Membros:** 
  * Afonso Nunes - 2023141213 
  * [Nome do Aluno 2] - [Nº de Estudante] 
  * [Nome do Aluno 3] - [Nº de Estudante] 
 
## Organização do Repositório 
 
A estrutura deste projeto segue as boas práticas de Ciência de Dados e Engenharia de Software: 
 
* **`data/`**: Armazenamento de dados (dados brutos em `raw/` e processados em `processed/`). 
* **`docs/`**: Documentação técnica detalhada dividida por Milestones (M1, M2 e M3). 
* **`notebooks/`**: Jupyter Notebooks para experimentação, limpeza e modelação. 
* **`src/`**: Código-fonte modular (scripts `.py`) para funções reutilizáveis. 
* **`reports/`**: Relatórios finais, apresentações e exportação de figuras (`figures/`). 
* **`requirements.txt`**: Ficheiro de configuração com as bibliotecas necessárias. 
 
 
## 1. Iniciação (Milestone 1) 
### Contexto e Problema de Negócio 
A crise habitacional em Lisboa dificulta o acesso à habitação para jovens e famílias. O Município disponibiliza programas de apoio (Porta 65, Renda Acessível), mas existe uma lacuna de informação sobre a real elegibilidade dos candidatos. O desafio é identificar "quem tem direito a quê" com base numa amostra de candidatos.

### Objetivos do Projeto 
* **Objetivo 1:** Mapear e Codificar as Regras Oficiais dos Programas de Apoio (Porta 65 Jovem/Mais, PRA, SMAA).
* **Objetivo 2:** Desenvolver um algoritmo de Classificação de Elegibilidade para cruzar candidatos com programas.
* **Objetivo 3:** Quantificar a taxa de cobertura real dos apoios na amostra fornecida.

### Fonte de Dados 
* **Dataset:** `amostras_desafio.xlsx` (Dados anonimizados de candidatos a habitação em Lisboa).
* **Dimensão:** ~100 registos com variáveis demográficas e económicas.


## 2. Exploração (Milestone 2) 
### Limpeza e Preparação 
* [Planeado: Normalização de concelhos, tratamento de nulos e conversão de escalões etários/rendimento para valores numéricos explícitos.]
 
### Principais Conclusões (EDA) 
> *Ver gráficos detalhados em `reports/figures/`*
* **Geografia:** A maioria dos candidatos reside em Lisboa, mas há exclusão imediata de não-residentes para programas municipais.
* **Idade:** Divisão 50/50 entre público-alvo Jovem (<35) e Adulto, exigindo diferenciação de programas (Porta 65 Jovem vs Porta 65+).
* **Rendimentos:** A curva de rendimentos sugere que a "classe média-baixa" é o grupo crítico para análise de elegibilidade.


## 3. Modelação (Milestone 3) 
### Abordagem Técnica 
* **Modelos:** Sistema Baseado em Regras (Rule-Based Expert System) que implementa a legislação em Python.
* **Métrica Principal:** Precisão da Elegibilidade (vs Regras Oficiais) e Taxa de Cobertura (%).


## 4. Finalização (Milestone 4) 
### Resposta ao Problema 
[A preencher na conclusão do projeto]
 
### Recomendações de Inovação 
1. [A preencher na conclusão do projeto]
 
 
## Como Reproduzir este Projeto 
1. Clone o repositório: `git clone https://github.com/AfonsoNunes03/ProjetoCDG.git` 
2. Instale as dependências: `pip install -r requirements.txt` 
3. Execute os notebooks na pasta `notebooks/` seguindo a ordem numérica. 
 
 
**Instituição:** Coimbra Business School | ISCAC   
**Curso:** Licenciatura em Ciência de Dados para a Gestão   
**Unidade Curricular:** Projeto em Ciência de Dados   
**Professor Responsável:** Dora Melo (dmelo@iscac.pt)
