
# Análise Exploratória de Dados de E-commerce

Projeto desenvolvido em Python para analisar informações de produtos de um e-commerce, utilizando dados disponibilizados durante o curso de Análise de Dados da EBAC.

## Objetivo

Explorar os dados de produtos e identificar padrões relacionados a preços, avaliações, marcas, temporadas e quantidade vendida.

## Tecnologias utilizadas

- Python
- Pandas
- Matplotlib
- Seaborn
- Jupyter Notebook

## Base de dados

A base analisada possui 295 registros e 24 colunas, incluindo informações de preço, nota, avaliações, desconto, marca, material, temporada e quantidade vendida codificada.

## Visualizações desenvolvidas

1. Histograma da distribuição dos preços.
2. Gráfico de dispersão entre preço e avaliações.
3. Mapa de calor das correlações.
4. Gráfico de barras das marcas mais frequentes.
5. Gráfico de pizza das temporadas.
6. Gráfico de densidade dos preços.
7. Gráfico de regressão entre avaliações e quantidade vendida.

## Principais resultados

- A maior parte dos produtos apresenta preços entre 40 e 200 reais.
- A marca Lupo possui a maior quantidade de produtos na base analisada.
- Aproximadamente 45,1% dos produtos pertencem à categoria primavera/verão.
- Cerca de 21% dos produtos não possuem temporada definida.
- O número de avaliações apresentou forte correlação positiva com a quantidade vendida codificada, aproximadamente 0,91.

## Limitações

A quantidade vendida foi obtida de faixas como +1000 e +10mil, convertidas em valores numéricos. Portanto, não representa necessariamente o número exato de vendas.

As correlações encontradas não comprovam relações de causa e efeito.

## Arquivos do projeto

- `analise_ecommerce.ipynb`: notebook principal com gráficos e interpretações.
- `analise_ecommerce.py`: script Python da análise.
- `ecommerce_estatistica.csv`: base de dados utilizada.
- `requirements.txt`: bibliotecas necessárias.

## Conclusão

O projeto permitiu praticar análise exploratória, estatística descritiva e visualização de dados, identificando padrões comerciais e oportunidades de melhoria na qualidade dos dados.
