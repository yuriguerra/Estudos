# Importa bibliotecas
import pandas as pd
import numpy as np

# Carrega um arquivo csv para a memoria
data = pd.read_csv('datasets/kc_house_data.csv')

# # Exibe as primeiras linhas
# print(data.head())

# # Lista os tipos de dados
# print(data.dtypes)

# =======================================
# Convertendo variáveis
# =======================================
# Por padrão o pandas coloca os campos de data como object (objects são considerados strings)
# Converte object(string) -> date
data['date'] = pd.to_datetime(data['date'])

# Outros tipos de conversões
# Inteiro -> Float
data['bedrooms'] = data['bedrooms'].astype(float)

# Float -> Inteiro
# No caso de conversões em inteiro, o ideal é que todas as variáveis estejam no mesmo tipo, ou int 32 ou int64
data['bedrooms'] = data['bedrooms'].astype(np.int64)

# Inteiro -> String
data['bedrooms'] = data['bedrooms'].astype(str)

# String -> Inteiro
data['bedrooms'] = data['bedrooms'].astype(np.int64)


# =======================================
# Criando novas variáveis
# =======================================
data['meu_nome'] = "Yuri"
data['Idade'] = 29
data['data_aprendizado'] = pd.to_datetime('2021-03-12')

# Exibe as primeiras linhas
# print(data.columns)
# print(data.dtypes)
# print(data[['id','bedrooms', 'meu_nome', 'Idade', 'data_aprendizado']].head(10))

# =======================================
# Deletar variáveis
# =======================================
print(data.columns)
cols = ['meu_nome', 'Idade', 'data_aprendizado']
data = data.drop(cols, axis=1)
print(data.columns)

# =======================================
# Selecionar variáveis (colunas)
# Direto pelos nomes 
# =======================================
print(data[['price', 'id', 'date']])

# =======================================
# Selecionar variáveis (colunas)
# Pelos índices das linhas e colunas
# =======================================
print(data.iloc[0:10, 0:3])

# =======================================
# Selecionar variáveis (colunas)
# Pelos índices das linhas e nome das colunas
# =======================================
print(data.loc[0:10, 'price'])

# =======================================
# Selecionar variáveis (colunas)
# Pelos índices booleanos
# =======================================
cols = [True, False, True, True, False, False,
       False, False, False, False, False, False,
       False, False, False, False, False,
       False, False, False, False]
print(data.loc[0:10, cols])

# iloc = Busca apenas por índices
# loc = Busca por nome, índice ou booleano

# =======================================
# Exercícios
# =======================================
print('1. Qual a data do imóvel mais antigo do portifólio?')
data['date'] = pd.to_datetime(data['date'])
print(data.sort_values('date', ascending = True).head(1))

print('2. Quantos imóveis possuem o número máximo de andares')
print(data['floors'].unique())
print(data[data['floors'] == 3.5].shape)

print('3. Criar uma classificação dos imóveis sendo baixo padrão e alto padrão. Alto padrão > 540k')
data['level'] = 'standard'
data.loc[data['price'] > 540000, 'level'] = 'high_standard'
data.loc[data['price'] < 540000, 'level'] = 'low_standard'
print(data.head())

print('4. Criar um relatório ordenado pelo preço')
cols = ['id', 'date', 'price', 'bedrooms',  'sqft_lot',  'level']
report = data[cols].sort_values('price', ascending = False)
report.to_csv('datasets/report_aula02.csv', index = False)

print('5. Criar um mapa indicando onde as casas estão localizadas')
# Plotly - biblioteca que tem função que desenha mapas
# Scatteer MapBox - Função que desenha mapas
data_map = data[['id', 'lat', 'long', 'price']]
print(data_map)
import plotly.express as px
mapa = px.scatter_mapbox(data_map, lat='lat', lon='long', hover_name='id', hover_data=['price'], color_discrete_sequence=['fuchsia'], zoom=3, height=300 )

mapa.update_layout(mapbox_style='open-street-map')
mapa.update_layout(height=600, margin={'r':0, 't':0, 'l':0, 'b':0})
# mapa.show() # Exibe o mapa no browseer
mapa.write_html('datasets/mapa_house_rocket.html')