import pandas as pd

df = pd.read_excel(r'D:\TRAE-PROJETOS\livro1\BIZANTINO\INTELIGENCIA-DE-MERCADO\KDP_Orders-db6f12e2-0887-4442-a911-009dfe2e395c.xlsx',
                   sheet_name='Vendas combinadas')

print('=' * 80)
print('TÍTULOS ÚNICOS DA TURMA DA AVENTURA')
print('=' * 80)

titulos_unicos = df['Título'].unique()
for i, titulo in enumerate(titulos_unicos, 1):
    print(f'{i}. {titulo}')

print(f'\n>>> Total de títulos únicos: {len(titulos_unicos)}')

print('\n' + '=' * 80)
print('MERCADOS/LOJAS ONDE OS LIVROS ESTÃO VENDENDO')
print('=' * 80)

lojas = df['Loja'].unique()
for loja in lojas:
    vendas_loja = df[df['Loja'] == loja]['Número líquido de unidades vendidas'].sum()
    print(f'- {loja}: {int(vendas_loja)} unidades vendidas')

print(f'\n>>> Total de mercados: {len(lojas)}')

# Análise por título
print('\n' + '=' * 80)
print('VENDAS POR TÍTULO (Top 10)')
print('=' * 80)

vendas_por_titulo = df.groupby('Título')['Número líquido de unidades vendidas'].sum().sort_values(ascending=False)
for titulo, vendas in vendas_por_titulo.head(10).items():
    print(f'{int(vendas)} unidades - {titulo[:80]}...' if len(titulo) > 80 else f'{int(vendas)} unidades - {titulo}')

# Análise temporal
print('\n' + '=' * 80)
print('VENDAS POR MÊS (2025-2026)')
print('=' * 80)

vendas_por_mes = df.groupby('Data dos royalties')['Número líquido de unidades vendidas'].sum().sort_values(ascending=False)
for mes, vendas in vendas_por_mes.head(15).items():
    print(f'{mes}: {int(vendas)} unidades')
