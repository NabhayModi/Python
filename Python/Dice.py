import random
import plotly_express as px
import plotly.figure_factory as ff

count=[]

dice_results=[]


for i in range(0,100):
    dice1=random.randint(1,6)
    dice2=random.randint(1,6)
    dice_results.append(dice1+dice2)
    count.append(i)
    
print(dice_results)

fig=ff.create_distplot([dice_results],['Result'])
    
fig.show()