import pandas as pd # importa a biblioteca pandas

df = pd.read_csv("https://raw.githubusercontent.com/guilhermeonrails/data-jobs/refs/heads/main/salaries.csv")  # importa o conjunto de dados de salários

df.head() # exibe as primeiras linhas do DataFrame

df.info() # exibe informações sobre o DataFrame, como número de entradas, colunas e tipos de dados

df.describe() # exibe estatísticas descritivas das colunas numéricas do DataFrame

df.shape # exibe a forma do DataFrame (número de linhas e colunas)

linhas, colunas = df.shape[0], df.shape[1]  # atribui o número de linhas e colunas a variáveis separadas
print(f"O DataFrame possui {linhas} linhas e {colunas} colunas.")  # imprime o número de linhas e colunas

df.columns  # exibe os nomes das colunas do DataFrame

renomear_colunas = {'work_year': 'ano', 'experience_level': 'nivel_experiencia', 'employment_type': 'tipo_emprego', 
'job_title': 'cargo', 'salary': 'salario', 'salary_currency': 'moeda_salario', 'salary_in_usd': 'salario_usd', 
'employee_residence': 'residencia_empregado', 'remote_ratio': 'taxa_remoto', 'company_location': 'localizacao_empresa', 
'company_size': 'tamanho_empresa'} # define um conjunto com os nomes das colunas do DataFrame
df.rename(columns=renomear_colunas, inplace=True)  # renomeia as colunas do DataFrame
df.columns  # exibe os novos nomes das colunas do DataFrame

df['nivel_experiencia'].value_counts()  # exibe a contagem de valores únicos na coluna 'nivel_experiencia' do DataFrame

df['tipo_emprego'].value_counts()  # exibe a contagem de valores únicos na coluna 'tipo_emprego' do DataFrame

df['taxa_remoto'].value_counts()  # exibe a contagem de valores únicos na coluna 'taxa_remoto' do DataFrame

renomear_colunas = {'ano': 'ano', 'nivel_experiencia': 'senioridade', 'tipo_emprego': 'contrato', 'cargo': 'cargo', 
'salario': 'salario', 'moeda_salario': 'moeda', 'salario_usd': 'usd', 'residencia_empregado': 'residencia', 
'taxa_remoto': 'remoto', 'localizacao_empresa': 'empresa', 'tamanho_empresa': 'tamanho_empresa'} # define um novo conjunto com os nomes das colunas do DataFrame
df.rename(columns=renomear_colunas, inplace=True)  # renomeia as colunas do DataFrame
df.columns  # exibe os novos nomes das colunas do DataFrame

df['senioridade'].value_counts() # exibe a contagem de valores únicos na coluna 'senioridade' do DataFrame

df['contrato'].value_counts() # exibe a contagem de valores únicos na coluna 'contrato' do DataFrame

df['remoto'].value_counts() # exibe a contagem de valores únicos na coluna 'remoto' do DataFrame

df['tamanho_empresa'].value_counts() # exibe a contagem de valores únicos na coluna 'tamanho_empresa' do DataFrame

senioridade = {'SE': 'Senior', 'MI': 'Pleno', 'EN': 'Junior', 'EX': 'Executivo'} # define um dicionário para substituir os códigos de senioridade por descrições completas
df['senioridade'] = df['senioridade'].replace(Senioridade)  # substitui os códigos de senioridade na coluna 'senioridade' do DataFrame
df['senioridade'].value_counts()  # exibe a contagem de valores únicos na coluna 'senioridade' do DataFrame após a substituição

contrato = {'FT': 'Tempo Integral', 'PT': 'Meio Período', 'CT': 'Contrato', 'FL': 'Freelancer'} # define um dicionário para substituir os códigos de contrato por descrições completas
df['contrato'] = df['contrato'].replace(contrato)  # substitui os códigos de contrato na coluna 'contrato' do DataFrame
df['contrato'].value_counts()  # exibe a contagem de valores únicos na coluna 'contrato' do DataFrame após a substituição

tamanho_empresa = {'S': 'Pequena', 'M': 'Média', 'L': 'Grande'} # define um dicionário para substituir os códigos de tamanho de empresa por descrições completas
df['tamanho_empresa'] = df['tamanho_empresa'].replace(tamanho_empresa)  # substitui os códigos de tamanho de empresa na coluna 'tamanho_empresa' do DataFrame
df['tamanho_empresa'].value_counts()  # exibe a contagem de valores únicos na coluna 'tamanho_empresa' do DataFrame após a substituição

remoto = {0: 'Presencial', 50: 'Híbrido', 100: 'Remoto'} # define um dicionário para substituir os códigos de remoto por descrições completas
df['remoto'] = df['remoto'].replace(remoto)  # substitui os códigos de remoto na coluna 'remoto' do DataFrame
df['remoto'].value_counts()  # exibe a contagem de valores únicos na coluna 'remoto' do DataFrame após a substituição
      
df.head()  # exibe as primeiras linhas do DataFrame atualizado

df.describe(include='object')  # exibe estatísticas descritivas das colunas categóricas do DataFrame atualizado

df.describe()  # exibe estatísticas descritivas das colunas numéricas do DataFrame atualizado
