import seaborn as sns
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

pd.set_option('display.max_columns', None)
pd.set_option('display.width', 500)
df = pd.read_excel('miuul_gezinomi.xlsx')
df.head()

df['SaleCityName'].nunique()

df['SaleCityName'].value_counts()

df['ConceptName'].nunique()

df.groupby('ConceptName')['ConceptName'].count()

df[['SaleCityName','Price']].groupby('SaleCityName').sum()

df.groupby('ConceptName')['Price'].sum()
df[['ConceptName','Price']].groupby('ConceptName').sum()

df.groupby('SaleCityName')['Price'].mean()

df.groupby('ConceptName')['Price'].mean()


df.groupby(['SaleCityName','ConceptName'])['Price'].mean()


bins = [-1, 7, 30, 90, df['SaleCheckInDayDiff'].max()]
labels = ['Last Minuters', 'Poetential Planners', 'Planners', 'Early Bookers']


df['EB_Score'] = pd.cut(df['SaleCheckInDayDiff'], bins, labels=labels)
df.to_excel('eb_scorew.xlsx', index = False)


df = pd.read_excel('eb_scorew.xlsx')
df.groupby(['SaleCityName','ConceptName','EB_Score']).agg({'Price':['mean','count']})
df.groupby(['SaleCityName','ConceptName','Seasons']).agg({'Price':['mean','count']})
df.groupby(['SaleCityName','ConceptName','CInDay']).agg({'Price':['mean','count']})


agg_df = df.groupby(['SaleCityName', 'ConceptName', 'Seasons']).agg({'Price':'mean'}).sort_values('Price',ascending = False)



agg_df.reset_index(inplace = True)
agg_df.head()

agg_df['sales_level_based'] = agg_df[['SaleCityName', 'ConceptName', 'Seasons']].agg(lambda x: '_'.join(x).upper(), axis=1)


df['SEGMENT'] = pd.qcut(agg_df['Price'], 4, labels=['D', 'C', 'B', 'A'])
df.to_excel('segmentation.xlsx', index = False)
df.head(50)




[ col[1]['Price'].mean() for col in df[['ConceptName','SaleCityName','Price']].groupby(['ConceptName','SaleCityName']) if col[0][1] == 'Antalya' and col[0][0] == "Herşey Dahil" ]




