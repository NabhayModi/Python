import csv
import pandas as pd
import plotly.express as px

df =      pd.read_csv('HeightWeight.csv')

fig = px.scatter(df,x='Height',y='Weight')


fig.show()
