import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

pd.set_option('display.max_columns', None)
pd.set_option('display.width', None)


df = pd.read_csv('ecommerce_estatistica.csv')

# Análise inicial
print("Quantidade de linhas e colunas:")
print(df.shape)

print("\nColunas disponíveis:")
print(df.columns.tolist())

print("\nPrimeiras linhas:")
print(df.head().to_string())

print("\nTipos dos dados:")
print(df.dtypes)

# Gráfico Histograma de preços
plt.figure(figsize=(10,6))
plt.hist(df['Preço'].dropna(), bins=20, edgecolor='black')
plt.title('Distribuição dos Preços dos Produtos')
plt.xlabel('Preço do Produto (R$)')
plt.ylabel('Quantidade de Produtos')
plt.tight_layout()
plt.show()

# Gráfico de Dispersão entre preços e avaliações
plt.figure(figsize=(10,6))
plt.scatter(df['Preço'], df['N_Avaliações'], alpha=0.6)
plt.title('Relação entre Preço e Número de Avaliações')
plt.xlabel('Preço (R$)')
plt.ylabel('Número de Avaliações')
plt.tight_layout()
plt.show()

# Gráfico Mapa de calor das correlações
colunas = ['Preço','Nota','N_Avaliações','Desconto','Qtd_Vendidos_Cod']
correlacao = df[colunas].corr()
plt.figure(figsize=(10,7))
sns.heatmap(
    correlacao,
    annot=True,
    cmap='coolwarm',
    fmt='.2f',
    vmin=-1,
    vmax=1,
    center=0
)
plt.title('Correlação entre Indicadores dos Produtos')
plt.tight_layout()
plt.show()

# Gráfico de Barras das marcas mais frequentes
top_marcas = df['Marca'].value_counts().head(10)
plt.figure(figsize=(11,6))
plt.barh(top_marcas.index, top_marcas.values)
plt.title('Top 10 Marcas com Mais Produtos Cadastrados')
plt.xlabel('Quantidade de Produtos')
plt.ylabel('Marca')
plt.gca().invert_yaxis()
plt.tight_layout()
plt.show()

# Gráfico de Pizza das temporadas
temporadas = df['Temporada'].value_counts()
principais = temporadas.head(3).copy()
principais['Outras'] = temporadas.iloc[3:].sum()
plt.figure(figsize=(9, 7))
plt.pie(principais,labels=principais.index,autopct='%1.1f%%',startangle=90)
plt.title('Distribuição dos Produtos por Temporada')
plt.tight_layout()
plt.show()

# Gráfico de Densidade dos preços
plt.figure(figsize=(10,6))
sns.kdeplot(x='Preço', data=df, fill=True)
plt.title('Densidade dos Preços dos Produtos')
plt.xlabel('Preço (R$)')
plt.ylabel('Densidade')
plt.tight_layout()
plt.show()

# Gráfico de Regressão entre Avaliações e Quantidade Vendida
plt.figure(figsize=(10, 6))

sns.regplot( data=df,
    x='N_Avaliações',
    y='Qtd_Vendidos_Cod',
    ci=None,
    scatter_kws={'alpha': 0.5, 's': 25},
    line_kws={'color': 'red'}
)
plt.title('Relação entre Avaliações e Quantidade Vendida')
plt.xlabel('Número de Avaliações')
plt.ylabel('Quantidade Vendida (Codificada)')
plt.tight_layout()
plt.show()
