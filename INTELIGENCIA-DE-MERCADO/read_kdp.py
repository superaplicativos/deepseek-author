import pandas as pd

# Ler arquivo KDP Orders
print("=" * 80)
print("ARQUIVO: KDP_Orders")
print("=" * 80)
xl_file = pd.ExcelFile(r'D:\TRAE-PROJETOS\livro1\BIZANTINO\INTELIGENCIA-DE-MERCADO\KDP_Orders-db6f12e2-0887-4442-a911-009dfe2e395c.xlsx')
print(f'Abas disponíveis: {xl_file.sheet_names}\n')

for sheet in xl_file.sheet_names:
    print(f'\n=== ABA: {sheet} ===')
    df = pd.read_excel(xl_file, sheet_name=sheet)
    print(f'Colunas: {df.columns.tolist()}')
    print(f'\nPrimeiras linhas:')
    print(df.head(20).to_string())
    print(f'\nTotal de linhas: {len(df)}')
    print("\n" + "-" * 80)

# Ler arquivo Royalties Estimator
print("\n\n" + "=" * 80)
print("ARQUIVO: KDP_Royalties_Estimator")
print("=" * 80)
xl_file2 = pd.ExcelFile(r'D:\TRAE-PROJETOS\livro1\BIZANTINO\INTELIGENCIA-DE-MERCADO\KDP_Royalties_Estimator-0c6d1550-2d07-46e7-828c-7fa60c66a2e5.xlsx')
print(f'Abas disponíveis: {xl_file2.sheet_names}\n')

for sheet in xl_file2.sheet_names:
    print(f'\n=== ABA: {sheet} ===')
    df = pd.read_excel(xl_file2, sheet_name=sheet)
    print(f'Colunas: {df.columns.tolist()}')
    print(f'\nPrimeiras linhas:')
    print(df.head(20).to_string())
    print(f'\nTotal de linhas: {len(df)}')
    print("\n" + "-" * 80)
