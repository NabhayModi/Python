import plotly.express as px
import csv
import numpy as np

def getDataSource(data_path):
    Size_of_TV=[]
    Average_time_spent=[]
    with open(data_path) as csv_file:
        csv_reader = csv.DictReader(csv_file)
        for row in csv_reader:
            Size_of_TV.append(float(row['Size of TV']))
            Average_time_spent.append(float(row['\tAverage time spent watching TV in a week (hours)']))
    return{'x' : Size_of_TV,'y' : Average_time_spent}

def findCorelations(dataSource):
    corelations=np.corrcoef(dataSource['x'],dataSource['y'])
    print('Correlation between Size and watch ---> ',corelations[0][1])

def setup():
    data_path='TV.csv'
    dataSource=getDataSource(data_path)
    findCorelations(dataSource)
setup()