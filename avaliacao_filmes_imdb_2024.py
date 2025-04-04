# -*- coding: utf-8 -*-
"""Untitled2.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1dyk4P9kbYo3jEnHwT7_FCv8gWwmkeNGc

# Avaliação de dados de Filmes - Imdb 2024
"""

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

df = pd.read_csv('/content/cleaned_imdb_2024.csv')

df.head()

df.dtypes

# Renomeando colunas
df = df.rename(columns={
    'Home_Page': 'Link',
    'Movie_Name': 'Nome do Filme',
    'Genres': 'Gêneros',
    'Overview': 'Visão Geral',
    'Cast': 'Elenco',
    'Original_Language': 'Linguagem Original',
    'Storyline': 'Resumo',
    'Production_Company': 'Produtora',
    'Release_Date': 'Data de Lançamento',
    'Tagline': 'Tags',
    'Vote_Average': 'Média Votação',
    'Vote_Count': 'Qtde Votos',
    'Budget_USD': 'Orçamento $ (em milhões)',
    'Revenue_$': 'Lucro $ (em milhões)',
    'Run_Time_Minutes': 'Duração (minutos)',
    'Release_Country': 'País de Origem'
})

# Função para converter valores de orçamento
def convert_budget(budget):
    if isinstance(budget, str):
        budget = budget.replace('$', '').replace('M', '')
        try:
            return float(budget)
        except ValueError:
            return np.nan  # Trata casos de conversão inválida
    elif pd.isna(budget):
        return np.nan
    else:
        return float(budget)

# Aplicando a função à coluna 'Budget_USD'
df['Orçamento $ (em milhões)'] = df['Orçamento $ (em milhões)'].apply(convert_budget)

# Função para converter valores de lucro
def convert_profit(profit):
    if isinstance(profit, str):
        profit = profit.replace('$', '').replace('M', '')
        try:
            return float(profit)
        except ValueError:
            return np.nan
    elif pd.isna(profit):
        return np.nan
    else:
        return float(profit)

# Aplicando a função à coluna 'Lucro $ (em milhões)'
df['Lucro $ (em milhões)'] = df['Lucro $ (em milhões)'].apply(convert_profit)

# Convertendo campo 'Release_Date' para data
df['Data de Lançamento'] = pd.to_datetime(df['Data de Lançamento'], errors='coerce')

# Função para converter campo Vote_Count removendo o K
def convert_vote_count(vote_count):
    if isinstance(vote_count, str) and 'K' in vote_count:
        try:
            return int(float(vote_count.replace('K', '')) * 1000)
        except ValueError:
            return np.nan  # lidando com casos onde a conversão falhar
    elif pd.isna(vote_count):
        return np.nan #lidando com nulos
    else:
      try:
        return int(vote_count)
      except ValueError:
        return np.nan

# Aplicando função à coluna
df['Qtde Votos'] = df['Qtde Votos'].apply(convert_vote_count)

# Converter coluna 'Run_Time_Minutes' para inteiro, tratando erros
df['Duração (minutos)'] = pd.to_numeric(df['Duração (minutos)'], errors='coerce').astype('Int64')

df.columns

"""# Analise Descritiva - Exploração e resumo dos Dados

### Qual a média, mediana e dispersão da nota dos filmes (Vote_Average)?
"""

media_notas = df['Média Votação'].mean()
mediana_notas = df['Média Votação'].median()
desvio_padrao_notas = df['Média Votação'].std()
print(f"Média das notas: {media_notas:.2f}")
print(f"Mediana das notas: {mediana_notas:.2f}")
print(f"Desvio Padrão das notas: {desvio_padrao_notas:.2f}")

"""### Há filmes com avaliações extremas (muito altas ou muito baixas)?


"""

# Analisando filmes com avaliações extremas
avaliacoes_extremas = df[(df['Média Votação'] >= 9.5) | (df['Média Votação'] <= 2.0)]
print(f"Número de filmes com avaliações extremas: {len(avaliacoes_extremas)}")

# Exibindo alguns exemplos de filmes com avaliações extremas
print("\nExemplos de filmes com avaliações extremas:")
print(avaliacoes_extremas[['Nome do Filme', 'Média Votação']].head(10)) # Exibindo os 10 primeiros

# Plotando um histograma das avaliações para visualizar a distribuição
plt.figure(figsize=(10, 6))
sns.histplot(df['Média Votação'], kde=True)
plt.title('Distribuição das Avaliações dos Filmes')
plt.xlabel('Média de Votação')
plt.ylabel('Frequência')
plt.show()

"""### Qual a distribuição do número de votos (Vote_Count)?


"""

# Analisando estatísticas descritivas da quantidade de votos
print(df['Qtde Votos'].describe())

# Distribuição de Qtde Votos por País de Origem
plt.figure(figsize=(12, 6))
df.groupby('País de Origem')['Qtde Votos'].sum().plot(kind='bar')
plt.xticks(rotation=90)
plt.title('Distribuição da Quantidade de Votos por País de Origem')
plt.xlabel('País de Origem')
plt.ylabel('Quantidade de Votos')
plt.show()

"""### Qual o orçamento médio (Budget_USD) dos filmes?


"""

orcamento_medio = df['Orçamento $ (em milhões)'].mean()
print(f"Orçamento médio dos filmes: US$ {orcamento_medio:.2f} milhões")

"""### Qual a receita média (Revenue_$) dos filmes?

"""

lucro_medio = df['Lucro $ (em milhões)'].mean()
print(f"Lucro médio dos filmes: US$ {lucro_medio:.2f} milhões")

"""### Qual a rentabilidade média (Receita - Orçamento)?

"""

rentabilidade_media = df['Lucro $ (em milhões)'].mean() - df['Orçamento $ (em milhões)'].mean()
print(f"Rentabilidade média dos filmes: US$ {rentabilidade_media:.2f} milhões")

"""### Qual a distribuição do tempo de duração (Duração - minutos)?


"""

# Analisando estatísticas descritivas da duração dos filmes
print(df['Duração (minutos)'].describe())

# Plotando um histograma da duração dos filmes
plt.figure(figsize=(10, 6))
sns.histplot(df['Duração (minutos)'], kde=True)
plt.title('Distribuição da Duração dos Filmes')
plt.xlabel('Duração (minutos)')
plt.ylabel('Frequência')
plt.show()

"""### Existem padrões por gênero?

"""

import ast
# Convertendo as strings para listas reais
df["Gêneros"] = df["Gêneros"].apply(ast.literal_eval)

# Explodindo os gêneros
df_exploded = df.explode("Gêneros")

# Contando a frequência dos gêneros
frequencia_generos = df_exploded["Gêneros"].value_counts()

print(frequencia_generos)

# Analisando a relação entre gênero e outras variáveis
# Agrupar por gênero e calcular a média da avaliação
genero_avaliacao = df_exploded.groupby("Gêneros")["Média Votação"].mean().sort_values(ascending=False)

df_exploded.columns

# Plotando gráfico de barras
plt.figure(figsize=(12, 6))
genero_avaliacao.plot(kind='bar', color='skyblue', edgecolor='black')
plt.title('Média da Avaliação por Gênero')
plt.xlabel('Gênero')
plt.ylabel('Média da Avaliação')
plt.xticks(rotation=45, ha='right')  # Rotaciona os rótulos do eixo x
plt.grid(axis='y', linestyle='--', alpha=0.7)
plt.tight_layout()
plt.show()

# Analisando a relação entre gênero e orçamento
genero_orcamento = df_exploded.groupby("Gêneros")['Orçamento $ (em milhões)'].mean().sort_values(ascending=False)

# Plotando gráfico de barras para visualizar
plt.figure(figsize=(12, 6))
genero_orcamento.plot(kind='bar')
plt.title('Orçamento Médio por Gênero')
plt.xlabel('Gênero')
plt.ylabel('Orçamento Médio (em milhões)')
plt.xticks(rotation=45, ha='right') # rotaciona os rótulos do eixo x
plt.tight_layout()
plt.show()

# Analisando a relação entre gênero e lucro
genero_lucro = df_exploded.groupby("Gêneros")['Lucro $ (em milhões)'].mean().sort_values(ascending=False)

# Plotando gráfico de barras para visualizar
plt.figure(figsize=(12, 6))
genero_lucro.plot(kind='bar')
plt.title('Lucro Médio por Gênero')
plt.xlabel('Gênero')
plt.ylabel('Lucro Médio (em milhões)')
plt.xticks(rotation=45, ha='right') # rotaciona os rótulos do eixo x
plt.tight_layout()
plt.show()

"""### Quais são os gêneros mais frequentes nos filmes?

"""

# Calculando a frequência dos gêneros
genero_frequencia = df_exploded['Gêneros'].value_counts()

# Exibindo os gêneros mais frequentes
print(genero_frequencia)

# Plotando um gráfico de barras para visualizar a frequência dos gêneros
plt.figure(figsize=(12, 6))
genero_frequencia.plot(kind='bar')
plt.title('Frequência dos Gêneros')
plt.xlabel('Gênero')
plt.ylabel('Frequência')
plt.xticks(rotation=45, ha='right')
plt.tight_layout()
plt.show()

"""### Filmes de múltiplos gêneros são comuns?

"""

# Contar o número de gêneros por filme (lidando com valores NaN)
multiple_genres = df["Gêneros"].dropna().apply(len)

# Contar a frequência normalizada (%) de filmes por número de gêneros
multiple_genres_counts = multiple_genres.value_counts(normalize=True) * 100

print(multiple_genres_counts)

# Plotar um gráfico de barras para visualizar a distribuição
plt.figure(figsize=(10, 6))
multiple_genres_counts.sort_index().plot(kind='bar', color='skyblue', edgecolor='black')
plt.title('Frequência de Filmes por Número de Gêneros')
plt.xlabel('Número de Gêneros')
plt.ylabel('Frequência (%)')
plt.xticks(rotation=0)
plt.grid(axis='y', linestyle='--', alpha=0.7)
plt.show()

"""### Quais são os idiomas originais mais frequentes?

"""

import ast
# Convertendo as strings para listas reais
df["Linguagem Original"] = df["Linguagem Original"].apply(ast.literal_eval)

# Explodindo os gêneros
df_exploded = df.explode("Linguagem Original")

# Contando a frequência dos gêneros
frequencia_linguagem = df_exploded["Linguagem Original"].value_counts()

print(frequencia_linguagem)

# Plotando um gráfico de barras para visualizar a frequência dos gêneros
plt.figure(figsize=(12, 6))
frequencia_linguagem.plot(kind='bar')
plt.title('Frequência da Linguagem')
plt.xlabel('Linguagem')
plt.ylabel('Frequência')
plt.xticks(rotation=45, ha='right')
plt.tight_layout()
plt.show()

"""### Quantos filmes foram lançados por ano/mês?


"""

# Criando colunas de ano e mês a partir da coluna 'Data de Lançamento'
df['Ano de Lançamento'] = df['Data de Lançamento'].dt.year
df['Mês de Lançamento'] = df['Data de Lançamento'].dt.month

# Agrupando por ano e contando a quantidade de filmes lançados
filmes_por_ano = df.groupby('Ano de Lançamento')['Nome do Filme'].count()

# Plotando o gráfico de filmes lançados por ano
plt.figure(figsize=(12, 6))
filmes_por_ano.plot(kind='bar')
plt.title('Quantidade de Filmes Lançados por Ano')
plt.xlabel('Ano')
plt.ylabel('Quantidade de Filmes')
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()

# Agrupando por mês e contando a quantidade de filmes lançados
filmes_por_mes = df.groupby('Mês de Lançamento')['Nome do Filme'].count()

# Plotando o gráfico de filmes lançados por mês
plt.figure(figsize=(12, 6))
filmes_por_mes.plot(kind='bar')
plt.title('Quantidade de Filmes Lançados por Mês')
plt.xlabel('Mês')
plt.ylabel('Quantidade de Filmes')
plt.xticks(rotation=0)
plt.tight_layout()
plt.show()

"""### Existe um período do ano com mais lançamentos?"""

# Agrupando por mês e contando a quantidade de filmes lançados
filmes_por_mes = df.groupby('Mês de Lançamento')['Nome do Filme'].count()

# Encontrando o mês com mais lançamentos
mes_mais_lancamentos = filmes_por_mes.idxmax()
qtde_lancamentos_mes = filmes_por_mes.max()

print(f"O mês com mais lançamentos é o mês {mes_mais_lancamentos} com {qtde_lancamentos_mes} lançamentos.")

"""### Quais são as produtoras que mais aparecem na base?"""

# Convertendo as strings para listas reais
df["Produtora"] = df["Produtora"].apply(ast.literal_eval)

# Explodindo as produtoras
df_exploded = df.explode("Produtora")

# Contando a frequência das produtoras
frequencia_produtoras = df_exploded["Produtora"].value_counts()
print(frequencia_produtoras)

plt.figure(figsize=(12, 6))

# Exibir apenas as 20 produtoras mais frequentes
frequencia_produtoras.head(20).plot(kind='bar', color='skyblue', edgecolor='black')

plt.title('Top 20 Produtoras Mais Frequentes')
plt.xlabel('Produtora')
plt.ylabel('Frequência')
plt.xticks(rotation=90, ha='right')  # Rotaciona os rótulos para melhor leitura
plt.grid(axis='y', linestyle='--', alpha=0.7)  # Adiciona linhas guias no eixo Y
plt.tight_layout()

plt.show()

"""### Quais filmes tiveram maior e menor retorno financeiro?"""

# Encontrando o filme com maior retorno financeiro
maior_retorno = df['Lucro $ (em milhões)'].max()
filme_maior_retorno = df.loc[df['Lucro $ (em milhões)'] == maior_retorno, 'Nome do Filme'].iloc[0]

print(f"Maior retorno financeiro: {filme_maior_retorno} (US$ {maior_retorno:.2f} milhões)")

# Encontrando o filme com menor retorno financeiro (considerando apenas valores positivos)
menor_retorno_positivo = df[df['Lucro $ (em milhões)'] > 0]['Lucro $ (em milhões)'].min()
filme_menor_retorno_positivo = df.loc[df['Lucro $ (em milhões)'] == menor_retorno_positivo, 'Nome do Filme'].iloc[0]

print(f"Menor retorno financeiro (positivo): {filme_menor_retorno_positivo} (US$ {menor_retorno_positivo:.2f} milhões)")

"""# Exploração Inferencial

### O orçamento impacta a receita?

Existe relação entre Budget_USD e Revenue_$?
"""

# Cálculo da correlação entre orçamento e receita
correlation = df['Orçamento $ (em milhões)'].corr(df['Lucro $ (em milhões)'])
print(f"Correlação entre Orçamento e Receita: {correlation:.2f}")

# Criando um scatter plot para visualizar a relação
plt.figure(figsize=(10, 6))
sns.scatterplot(x='Orçamento $ (em milhões)', y='Lucro $ (em milhões)', data=df)
plt.title('Relação entre Orçamento e Receita')
plt.xlabel('Orçamento (em milhões)')
plt.ylabel('Receita (em milhões)')
plt.show()

"""Qual o retorno médio sobre investimento por gênero?"""

# Garantir que os gêneros estejam como listas (caso estejam como strings)
import ast
#df["Gêneros"] = df["Gêneros"].apply(ast.literal_eval)  # Converte string para lista (se necessário)

# Calcular o ROI antes de explodir os gêneros
df["ROI"] = df["Lucro $ (em milhões)"] - df["Orçamento $ (em milhões)"]

# Explodir os gêneros para cada filme
df_exploded = df.explode("Gêneros")

# Agrupar por gênero e calcular o ROI médio
roi_por_genero = df_exploded.groupby("Gêneros")["ROI"].mean().sort_values(ascending=False)

# Exibir o ROI médio por gênero
print(roi_por_genero)

# Plotando um gráfico de barras para visualizar o ROI médio por gênero
plt.figure(figsize=(12, 6))
roi_por_genero.plot(kind='bar')
plt.title('Retorno Médio sobre Investimento por Gênero')
plt.xlabel('Gênero')
plt.ylabel('ROI Médio (em milhões)')
plt.xticks(rotation=45, ha='right')
plt.tight_layout()
plt.show()

"""### A duração do filme afeta a nota?


"""

# Cálculo da correlação entre duração e média de votação
correlation_duration_rating = df['Duração (minutos)'].corr(df['Média Votação'])
print(f"Correlação entre Duração e Média de Votação: {correlation_duration_rating:.2f}")

# Criando um scatter plot para visualizar a relação
plt.figure(figsize=(10, 6))
sns.scatterplot(x='Duração (minutos)', y='Média Votação', data=df)
plt.title('Relação entre Duração e Média de Votação')
plt.xlabel('Duração (minutos)')
plt.ylabel('Média de Votação')
plt.show()

"""### Há padrões sazonais nos lançamentos?"""

# Agrupando por mês e contando a quantidade de filmes lançados
filmes_por_mes = df.groupby('Mês de Lançamento')['Nome do Filme'].count()

# Plotando o gráfico de filmes lançados por mês
plt.figure(figsize=(12, 6))
filmes_por_mes.plot(kind='bar')
plt.title('Quantidade de Filmes Lançados por Mês')
plt.xlabel('Mês')
plt.ylabel('Quantidade de Filmes')
plt.xticks(rotation=0)
plt.tight_layout()
plt.show()

# Analisando a tendência de lançamentos ao longo dos meses
filmes_por_mes

"""### Filmes com maior orçamento tendem a ser mais bem avaliados?"""

# Cálculo da correlação entre orçamento e média de votação
correlation_budget_rating = df['Orçamento $ (em milhões)'].corr(df['Média Votação'])
print(f"Correlação entre Orçamento e Média de Votação: {correlation_budget_rating:.2f}")

# Criando um scatter plot para visualizar a relação
plt.figure(figsize=(10, 6))
sns.scatterplot(x='Orçamento $ (em milhões)', y='Média Votação', data=df)
plt.title('Relação entre Orçamento e Média de Votação')
plt.xlabel('Orçamento (em milhões)')
plt.ylabel('Média de Votação')
plt.show()