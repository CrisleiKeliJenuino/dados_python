import pandas as pd  # Biblioteca para analise de dados
import numpy as np   # Biblioteca para trabalhar com valores numericos e NaN

# ==================================================
# 1 - CARREGAMENTO E INSPECAO INICIAL DOS DADOS
# ==================================================

# Le o arquivo CSV com os dados de salarios (fonte: Kaggle)
df = pd.read_csv("D:/GITHUB/dados_python/salaries.csv")

# Visualiza as primeiras linhas do DataFrame
print(df.head())

# Informacoes gerais do DataFrame
df.info()

# Estatisticas descritivas das colunas numericas
print(df.describe())

# Dimensao do DataFrame (linhas, colunas)
print(df.shape)

linhas, colunas = df.shape
print(f"O DataFrame possui {linhas} linhas e {colunas} colunas.")

# Nomes das colunas originais
print(df.columns)

# ==================================================
# 2 - RENOMEACAO DAS COLUNAS
# ==================================================

# Renomeia as colunas para portugues
renomear_colunas = {
    'work_year': 'ano',
    'experience_level': 'senioridade',
    'employment_type': 'contrato',
    'job_title': 'cargo',
    'salary': 'salario',
    'salary_currency': 'moeda',
    'salary_in_usd': 'usd',
    'employee_residence': 'residencia',
    'remote_ratio': 'remoto',
    'company_location': 'empresa',
    'company_size': 'tamanho_empresa'
}

df.rename(columns=renomear_colunas, inplace=True)

# Verifica os novos nomes das colunas
print(df.columns)

# ==================================================
# 3 - TRADUCAO E PADRONIZACAO DE VALORES
# ==================================================

# Traduzao da senioridade
df['senioridade'] = df['senioridade'].replace({
    'SE': 'Senior',
    'MI': 'Pleno',
    'EN': 'Junior',
    'EX': 'Executivo'
})
print(df['senioridade'].value_counts())

# Traduzao do tipo de contrato
df['contrato'] = df['contrato'].replace({
    'FT': 'Tempo Integral',
    'PT': 'Meio Periodo',
    'CT': 'Contrato',
    'FL': 'Freelancer'
})
print(df['contrato'].value_counts())

# Traduzao do tamanho da empresa
df['tamanho_empresa'] = df['tamanho_empresa'].replace({
    'S': 'Pequena',
    'M': 'Media',
    'L': 'Grande'
})
print(df['tamanho_empresa'].value_counts())

# Traduzao do regime de trabalho
df['remoto'] = df['remoto'].replace({
    0: 'Presencial',
    50: 'Hibrido',
    100: 'Remoto'
})
print(df['remoto'].value_counts())

# ==================================================
# 4 - LIMPEZA DA COLUNA ANO
# ==================================================

# Remove linhas com ano nulo
df = df.dropna(subset=['ano'])

# Converte a coluna ano para inteiro
df['ano'] = df['ano'].astype(int)

# ==================================================
# 5 - PADRONIZACAO DOS CARGOS
# ==================================================

# Mantem o cargo original
df['cargo_original'] = df['cargo']

# Funcao para agrupar cargos semelhantes
def padronizar_cargo(cargo):
    cargo = str(cargo).lower()

    if 'data scientist' in cargo:
        return 'Cientista de Dados'
    elif 'data engineer' in cargo:
        return 'Engenheiro de Dados'
    elif 'machine learning' in cargo or 'ml engineer' in cargo:
        return 'Engenheiro de Machine Learning'
    elif 'data analyst' in cargo:
        return 'Analista de Dados'
    elif 'business intelligence' in cargo or 'power bi' in cargo or 'tableau' in cargo:
        return 'Business Intelligence'
    elif 'solutions engineer' in cargo:
        return 'Engenheiro de Solucoes'
    elif 'software' in cargo or 'developer' in cargo:
        return 'Engenharia de Software'
    elif 'manager' in cargo or 'lead' in cargo or 'director' in cargo:
        return 'Gestao / Lideranca'
    elif 'research' in cargo or 'researcher' in cargo:
        return 'Pesquisa / Academico'
    else:
        return 'Outros'

# Aplica a padronizacao
df['cargo_padronizado'] = df['cargo_original'].apply(padronizar_cargo)

# Exemplos de cargos antes e depois
print(df[['cargo_original', 'cargo_padronizado']].sample(10))

# Contagem por cargo padronizado
print(df['cargo_padronizado'].value_counts())

# ==================================================
# 6 - VERIFICACOES FINAIS
# ==================================================

# Estatisticas das colunas categoricas
print(df.describe(include=['object', 'string']))

# Verifica valores nulos
print(df.isnull().sum())

# Anos existentes no dataset
print(df['ano'].unique())

# Linhas que possuem valores nulos
print(df[df.isnull().any(axis=1)])

# ==================================================
# 7 - EXEMPLO DIDATICO DE TRATAMENTO DE VALORES NULOS
# ==================================================

df_salarios = pd.DataFrame({
    'nome': ['Joao', 'Maria', 'Pedro', 'Ana', 'Lucas'],
    'salario': [5000, np.nan, 7000, np.nan, 15000]
})

# Preenche valores nulos com media
df_salarios['salario_media'] = df_salarios['salario'].fillna(
    df_salarios['salario'].mean().round(2)
)

# Preenche valores nulos com mediana
df_salarios['salario_mediana'] = df_salarios['salario'].fillna(
    df_salarios['salario'].median().round(2)
)

print(df_salarios)

# ==================================================
# 8 - EXEMPLO DIDATICO DE TRATAMENTO DE TEMPERATURAS
# ==================================================

df_temperaturas = pd.DataFrame({
    'Dia': ['Segunda', 'Terca', 'Quarta', 'Quinta', 'Sexta', 'Sabado', 'Domingo'],
    'Temperatura': [22.5, 21.0, np.nan, 19.5, np.nan, 20.0, 23.0]
})

# Preenche com valores do dia anterior
df_temperaturas['Prenchido_ffill'] = df_temperaturas['Temperatura'].ffill()
df_temperaturas

# Preenche com valores do dia seguinte
df_temperaturas['Prenchido_bfill'] = df_temperaturas['Temperatura'].bfill()
df_temperaturas

# ==================================================
# 9 - EXEMPLO DIDATICO DE TRATAMENTO DE CIDADES
# ==================================================

df_cidades = pd.DataFrame({
    'nome': ['Joao', 'Maria', 'Pedro', 'Ana', 'Lucas'],
    'cidade': ['Sao Paulo', np.nan, 'Rio de Janeiro', np.nan, 'Belo Horizonte']
})

df_cidades['cidades_preenchidas'] = df_cidades['cidade'].fillna('Não Informado')
df_cidades

df_limpo = df.dropna() # Remove todas as linhas com qualquer valor nulo
df_limpo.isnull().sum() # Verifica valores nulos apos limpeza
df_limpo.head() # Visualiza as primeiras linhas do DataFrame limpo
df_limpo.info() # Informacoes gerais do DataFrame limpo

### exemplo para converter um valor numerico com casas decimais para inteiro, use o comando abaixo:
# df_limpo = df_limpo.assign(ano = df_limpo['ano'].astype(int64))

# ==================================================
# 10 - VISUALIZACAO FINAL
# ==================================================

# Colunas finais
print(df.columns)

# Amostra final do DataFrame
print(df.head())
# Dimensao final do DataFrame