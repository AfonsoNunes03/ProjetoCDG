
import pandas as pd

file_path = r'../data/raw/ficha_caracterizacao.xlsx'

try:
    xls = pd.ExcelFile(file_path)
    print(f"Abas disponíveis: {xls.sheet_names}")
    
    # Tentar ler a aba 'Informações' ou similar se existir, senão ler todas as primeiras linhas
    for sheet in xls.sheet_names:
        print(f"\n--- Conteúdo inicial da aba '{sheet}' ---")
        df = pd.read_excel(xls, sheet_name=sheet, nrows=20)
        # Mostrar apenas colunas com texto relevante para não poluir
        print(df.to_string())
        
except Exception as e:
    print(f"Erro ao ler Excel: {e}")
