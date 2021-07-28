import pandas as pd
import statistics
import csv

df=pd.read_csv('HeightWeight.csv')
height_list=df['Height'].to_list()
weight_list=df['Weight'].to_list()
height_mean=statistics.mean(height_list)
weight_mean=statistics.mean(weight_list)
height_median=statistics.median(height_list)
weight_median=statistics.median(weight_list)


print('mean of the data is {}'.format(height_mean) )
print('mean of the data is {}'.format(weight_mean) )

print('median of the data is {}'.format(height_median) )
print('median of the data is {}'.format(weight_median) )

