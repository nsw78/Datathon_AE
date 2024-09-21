import pandas as pd

# Carregar os dados dos arquivos CSV
dados_alunos = pd.read_csv('Dados Alunos.csv')
dados_historicos = pd.read_csv('Dados Historicos.csv', delimiter=';')

# Verificar as colunas disponíveis em 'Dados Históricos'
print(dados_historicos.columns)

# Agrupar e sumarizar (ajuste a coluna conforme seus dados)
principais_receitas = dados_historicos.groupby('INSTITUICAO_ENSINO_ALUNO_2020')['IAA_2020'].sum().reset_index()

# Mostrar as principais linhas de receita
print("\nPrincipais Linhas de Receita:")
print(principais_receitas)

# Salvar o resultado em um novo arquivo CSV
principais_receitas.to_csv('principais_linhas_de_receita.csv', index=False)
