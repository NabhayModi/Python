import csv
import pandas as pd
import plotly.express as px

df =      pd.read_csv('something.csv')

fig = px.scatter(df,x='level',y='attempt')


fig.show()
