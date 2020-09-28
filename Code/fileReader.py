#¿Cuáles fueron los 5 países más productores de gases de invernadero en
#2010?
#Los cinco paises mas productores fueron EUA, Rusia, Japon, Alemania, y Canada
#¿Cuáles fueron los 5 países más poblados en 2010?
#Los cinco paises mas poblados en 2010 fueron China, India, EUA, Indonesia y Brazil

import pandas as pd

df1 = pd.read_csv("../TextFiles/populationbycountry19802010millions.csv",sep=',')
df1 = df1[['Country','2010']]
df1['2010']= pd.to_numeric(df1['2010'],errors = 'coerce')
df1 = df1.dropna()
df1 = df1.sort_values('2010', ascending = False)
print(df1.head(20))

print("")

df2 = pd.read_csv("../TextFiles/greenhouse_gas_inventory_data_data.csv",sep=',')
df2 = df2[df2["year"]==2010]
df2 = df2.sort_values("value", ascending = False)

print(df2.head(20))
