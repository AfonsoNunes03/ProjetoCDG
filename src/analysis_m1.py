
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import os

# 1. Configuração do Ambiente e Dados
data_path = r'../data/raw/amostras_desafio.xlsx'
processed_path = r'../data/processed/'
figures_path = r'../reports/figures/'

# Garantir diretorias
os.makedirs(processed_path, exist_ok=True)
os.makedirs(figures_path, exist_ok=True)

# 2. Carregar os Dados
try:
    df = pd.read_excel(data_path)
    print("Dados carregados com sucesso!")
    print(df.info())
except Exception as e:
    print(f"Erro ao carregar dados: {e}")
    exit()

# 3. Limpeza Inicial (Renomear para facilitar)
df.columns = [col.strip() for col in df.columns]
rename_map = {
    'Contexto': 'contexto',
    'Estado': 'estado',
    'Data Estado': 'data_estado',
    'Escalão Etário': 'escalao_etario',
    'Nº Elem. Agregado': 'n_elem_agregado',
    'Nº Adultos': 'n_adultos',
    'Concelho': 'concelho',
    'Rendimento Global (IRS e Rend. Isentos)': 'rendimento_anual_bruto'
}
df.rename(columns=rename_map, inplace=True)

# 4. Análise Exploratória Básica (M1)

# 4.1 Distribuição Geográfica (Concelho)
plt.figure(figsize=(10, 6))
sns.countplot(y='concelho', data=df, order=df['concelho'].value_counts().index, palette='viridis')
plt.title('Distribuição de Candidatos por Concelho')
plt.xlabel('Número de Candidatos')
plt.ylabel('Concelho')
plt.tight_layout()
plt.savefig(os.path.join(figures_path, 'distribuicao_concelho.png'))
plt.close()

# 4.2 Distribuição Etária (Escalão)
plt.figure(figsize=(8, 5))
sns.countplot(x='escalao_etario', data=df, order=['Menos 35 anos', '35 a 65 anos', 'Mais 65 anos'], palette='pastel')
plt.title('Distribuição de Candidatos por Escalão Etário')
plt.xlabel('Escalão Etário')
plt.ylabel('Contagem')
plt.tight_layout()
plt.savefig(os.path.join(figures_path, 'distribuicao_etaria.png'))
plt.close()

# 4.3 Distribuição de Rendimentos (Histograma)
plt.figure(figsize=(10, 6))
sns.histplot(df['rendimento_anual_bruto'], bins=20, kde=True, color='skyblue')
plt.title('Distribuição do Rendimento Anual Bruto dos Agregados')
plt.xlabel('Rendimento Anual (€)')
plt.ylabel('Frequência')
plt.axvline(df['rendimento_anual_bruto'].mean(), color='red', linestyle='--', label=f'Média: {df["rendimento_anual_bruto"].mean():.2f}€')
plt.legend()
plt.tight_layout()
plt.savefig(os.path.join(figures_path, 'distribuicao_rendimento.png'))
plt.close()

# 5. Guardar Dados Processados (Checkpoint M1)
df.to_csv(os.path.join(processed_path, 'amostra_limpa_M1.csv'), index=False)
print("Análise M1 concluída! Gráficos guardados em 'reports/figures/'.")
