import plotly.express as px
import csv
import numpy as np

def getDataSource(data_path):
    icecream_sales=[]
    colddrink_sales=[]
    with open(data_path) as csv_file:
        csv_reader = csv.DictReader(csv_file)
        for row in csv_reader:
            icecream_sales.append(float(row['Temperature']))
            colddrink_sales.append(float(row['Ice-cream Sales']))
    return{'x' : icecream_sales,'y' : colddrink_sales}

def findCorelations(dataSource):
    corelations=np.corrcoef(dataSource['x'],dataSource['y'])
    print('Correlation between temprature vs icecream sales ---> ',corelations[0][1])

def setup():
    data_path='IceCream.csv'
    dataSource=getDataSource(data_path)
    findCorelations(dataSource)
setup()