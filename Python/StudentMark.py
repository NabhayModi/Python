import plotly.express as px
import csv
import numpy as np

def getDataSource(data_path):
    Marks_In_Percentage=[]
    Days_Present=[]
    with open(data_path) as csv_file:
        csv_reader = csv.DictReader(csv_file)
        for row in csv_reader:
            Marks_In_Percentage.append(float(row['Marks In Percentage']))
            Days_Present.append(float(row['Days Present']))
    return{'x' : Marks_In_Percentage,'y' : Days_Present}

def findCorelations(dataSource):
    corelations=np.corrcoef(dataSource['x'],dataSource['y'])
    print('Correlation between Size and watch ---> ',corelations[0][1])

def setup():
    data_path='Marks.csv'
    dataSource=getDataSource(data_path)
    findCorelations(dataSource)
setup()