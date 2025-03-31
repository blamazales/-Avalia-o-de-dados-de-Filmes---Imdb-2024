# Avaliação de dados de Filmes - Imdb 2024

📌 Contexto

Este projeto analisa a uma lista de filmes do Imdb sobre o ano de 2024 e suas informações como orçamento, lucro, nota, etc. foram aplicadas técnicas de análise exploratória para entender se existe uma correlação entre as variáveis existentes e entender algum padrão dentre os filmes listados.

📂 Descrição do Dataset

O conjunto de dados contém diversas informações sobre os filmes lançados em 2024. A seguir, uma descrição das colunas:

📝 Variáveis

- Link – URL ou identificador do filme em uma base de dados online.

- Nome do Filme – Título do filme analisado.

- Gêneros – Lista de gêneros aos quais o filme pertence (ex.: Ação, Drama, Comédia).

- Visão Geral – Breve sinopse do filme.

- Elenco – Principais atores que participaram do filme.

- Linguagem Original – Idioma original do filme.

- Resumo – Descrição compacta do filme, possivelmente baseada na visão geral.

- Produtora – Estúdio ou empresa responsável pela produção do filme.

- Data de Lançamento – Data oficial em que o filme foi lançado.

- Tags – Palavras-chave associadas ao filme para facilitar a categorização.

- Média Votação – Nota média atribuída ao filme pelos usuários.

- Qtde Votos – Número total de votos recebidos pelo filme.

- Orçamento $ (em milhões) – Valor investido na produção do filme (em milhões de dólares).

- Lucro $ (em milhões) – Receita total obtida pelo filme (em milhões de dólares).

- Duração (minutos) – Tempo total de exibição do filme em minutos.

- País de Origem – País onde o filme foi produzido.


⚙️ Processamento de Dados

As seguintes etapas foram aplicadas ao conjunto de dados:

1. **Coleta de Dados**: Utilizamos um dataset contendo informações sobre filmes, incluindo duração e média de votação.
2. **Processamento e Limpeza**: Tratamos dados ausentes e removemos valores inconsistentes.
3. **Análise Estatística**: Correlação estre variáveis, média, mediana e outras análises.
4. **Visualização**: Criamos gráficos para representar a relação entre essas variáveis.

📊 Análises e Visualizações

Utilizamos as bibliotecas pandas, numpy, matplotlib e seaborn para explorar o conjunto de dados. Algumas análises incluem:

- Distribuição do tempo de duração do filme

- Gêneros mais frequentes

- Quantidade de filmes lançado ao ano e por mês

- Correlação entre duração do filme e nota de avaliação


### Tecnologias Utilizadas

- Python: Linguagem de programação principal do projeto.

- Pandas: Biblioteca utilizada para manipulação e análise de dados.

- NumPy: Para operações matemáticas e numéricas.

- Seaborn e Matplotlib: Para visualização de dados.

- SciPy: Para análises estatísticas.
