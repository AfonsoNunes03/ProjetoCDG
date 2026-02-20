# Projeto Desafio Habitação: Análise de Elegibilidade e Acesso

## Identificação da Equipa
* **Grupo nº:** 2
* **Membros:**
  * Afonso Nunes - 2023141213
  * Guilherme Ventura - 2023132296
  * Duarte Ribeiro - 2023142440

## Organização do Repositório

A estrutura deste projeto segue as boas práticas de Ciência de Dados:

* **`milestones/`**: Documentação detalhada de cada fase do projeto (M1 a M4).
* **`assets/graficos/`**: Gráficos e visualizações exportadas (PNGs/SVGs).
* **`assets/diagramas/`**: Fluxogramas e diagramas de arquitetura.
* **`assets/demos/`**: GIFs ou prints da solução final.
* **`notebooks/`**: Jupyter Notebooks para experimentação e análise.
* **`data/`**: Dados brutos (`raw/`) e processados (`processed/`) — protegidos pelo `.gitignore`.
* **`src/`**: Código-fonte modular (scripts `.py`) para funções reutilizáveis.
* **`requirements.txt`**: Bibliotecas Python necessárias.

## 1. Iniciação (Milestone 1)
### Contexto e Problema de Negócio
A crise habitacional em Lisboa dificulta o acesso à habitação para jovens e famílias. O Município disponibiliza programas de apoio (Porta 65, Renda Acessível, SMAA), mas existe uma lacuna de informação sobre a real elegibilidade dos candidatos.

O desafio central é: **os programas de apoio existem, mas as suas regras de elegibilidade criam um funil burocrático que exclui uma parte significativa de quem precisa de apoio.**

> *Ver detalhes completos em [`milestones/M1_iniciacao.md`](milestones/M1_iniciacao.md)*

### Fonte de Dados
* **Dataset:** `amostras_desafio.xlsx` (Dados anonimizados de candidatos a habitação em Lisboa — LxDataLab).
* **Dimensão:** ~100 registos com variáveis demográficas e económicas.

## 2. Exploração (Milestone 2)
> *Ver [`milestones/M2_exploracao.md`](milestones/M2_exploracao.md)*

## 3. Modelação (Milestone 3)
> *Ver [`milestones/M3_modelacao.md`](milestones/M3_modelacao.md)*

## 4. Finalização (Milestone 4)
> *Ver [`milestones/M4_finalizacao.md`](milestones/M4_finalizacao.md)*

## Como Reproduzir este Projeto
1. Clone o repositório: `git clone https://github.com/AfonsoNunes03/ProjetoCDG.git`
2. Instale as dependências: `pip install -r requirements.txt`
3. Adicione o dataset em `data/raw/` (não incluído no repositório por proteção de dados).
4. Execute os notebooks na pasta `notebooks/` seguindo a ordem numérica.

---

**Instituição:** Coimbra Business School | ISCAC
**Curso:** Licenciatura em Ciência de Dados para a Gestão
**Unidade Curricular:** Projeto em Ciência de Dados
**Professor Responsável:** Dora Melo (dmelo@iscac.pt)
