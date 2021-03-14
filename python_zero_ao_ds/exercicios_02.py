# Importa bibliotecas
import pandas as pd
import numpy as np

# Carrega o arquivo csv para a memoria
data = pd.read_csv('datasets/kc_house_data.csv')


# =======================================
# Novas perguntas do CEO
# =======================================
print('1. Criar nova coluna chamada house_age')
# Se date > 2014-01-01 = 'new_house', se date < 2014-01-01 = 'old_house'
data['date'] = pd.to_datetime(data['date'])
data['house_age'] = 'not_defined'
data.loc[data['date'] >= '2014-01-01', 'house_age'] = 'new_house'
data.loc[data['date'] < '2014-01-01', 'house_age'] = 'old_house'


print('2. Criar nova coluna chamada dormitory_type')
# Se bedrooms== 1 = 'studio', se bedrooms== 2 = 'apartment', se bedrooms>2 = 'house'
data['dormitory_type'] = 'not_defined'
data.loc[data['bedrooms'] == 1, 'dormitory_type'] = 'studio'
data.loc[data['bedrooms'] == 2, 'dormitory_type'] = 'apartment'
data.loc[data['bedrooms'] > 2, 'dormitory_type'] = 'house'

print('3. Criar nova coluna chamada condition_type')
# Se condition<= 2 = 'bad', se condition==3 ou condition==4 = 'regular', se condition=5 = 'good'
data['condition_type'] = 'not_defined'
data.loc[data['condition'] <= 2, 'condition_type'] = 'bad'
data.loc[data['condition'].between(3, 4), 'condition_type'] = 'regular'
data.loc[data['condition'] == 5, 'condition_type'] = 'good'

print('4. Modifique o tipo da coluna condition para string')
# print(data.dtypes)
data['condition'] = data['condition'].astype(str)
# print(data.dtypes)

print('5. Delete as colunas sqft_living15 e sqft_lot15')
# print(data.columns)
cols = ['sqft_living15', 'sqft_lot15']
data = data.drop(cols, axis=1)
# print(data.columns)

print('6. Modifique o tipo da coluna yr_built para date')
# print(data['yr_built'])
data['yr_built'] = pd.to_datetime(data['yr_built'])
# print(data['yr_built'])

print('7. Modifique o tipo da coluna yr_renovated para date')
# print(data['yr_renovated'])
data['yr_renovated'] = pd.to_datetime(data['yr_renovated'])
# print(data['yr_renovated'])

print('8. Qual a data mais antiga de contrução de um imóvel?')
print(data[['id', 'yr_built']].head(1).sort_values('yr_built', ascending=True))

print('9. Qual a data mais antiga de renovação de um imóvel?')
print(data[['id', 'yr_renovated']].head(1).sort_values('yr_renovated', ascending=True))

print('10. Quantos imóveis tem 2 andares?')
print(data[data['floors'] == 2].shape)

print('11. Quantos imóveis tem uma condição regular?')
print(data[data['condition_type'] == 'regular'].shape)

print('12. Quantos imóveis estão com a condição bad e possueem vista para água?')
print(data[(data['waterfront'] == 1) & (data['condition_type'] == 'bad')])

print('13. Quantos imóveis estão com a condição good e são new_house?')
print(data[(data['condition_type'] == 'good') & (data['house_age'] == 'new_house')].shape)

print('14. Qual o valor do imóvel mais caro do tipo studio?')
print(data[data['dormitory_type'] == 'studio'].head(1).sort_values('price', ascending=False))

print('15. Quantos imóveis do tipo apartment foram reformados em 2015?')
print(data[(data['dormitory_type']=='apartment') & (data['yr_renovated'] >= '2015-01-01') & (data['yr_renovated'] <= '2015-12-31')])

print('16. Qual o maior número de quartos que um imóvel do tipo house possui?')
print(data[data['dormitory_type']=='house'].head(1).sort_values('bedrooms', ascending=False))

print('17. Quantos imóveis new_house forma reformados no ano de 2014?')
data['yr_renovated'] = data['yr_renovated'].astype(np.int64)
print(data[(data['house_age']=='new_house') & (data['yr_renovated']==2014) ])

print('18. Selecione as colunas id, date, price, floors, zipcode pelos métodos')
# #Direto pelo nome das colunas
cols = ['id', 'date', 'price', 'floors', 'zipcode']
print(data[cols])
# #Por índices
indx = [0,1,2,7,16]
print(data.iloc[:,indx])
# #Pelos índices das linhas e nome das colunas
print(data.loc[:,cols])

# #Índices boobleanos
bols = [True, True, True, False, False, False,
       False, True, False, False, False, False,
       False, False, False, False, True,
       False, False, False, False, False]
print(data.loc[:,bols])

# print('19. Salvar o resultado do relatório em csv')
data.to_csv('datasets/exercicio_aula02.csv', index = False)

# print('20. Printar o mapa com os pontos em cor verde escuro')
data_map = data[['id', 'lat', 'long', 'price']]
print(data_map)
import plotly.express as px
mapa = px.scatter_mapbox(data_map, lat='lat', lon='long', hover_name='id', hover_data=['price'], color_discrete_sequence=['darkgreen'], zoom=3, height=300 )

mapa.update_layout(mapbox_style='open-street-map')
mapa.update_layout(height=600, margin={'r':0, 't':0, 'l':0, 'b':0})
# mapa.show() # Exibe o mapa no browseer
mapa.write_html('datasets/exercicio_02_mapa_house_rocket.html')