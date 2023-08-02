import numpy as np
import pandas as pd
import plotly.express as px
# plot distribution of damage_grade by value_counts using plotly
df = pd.read_csv(\
    "C:/Users/Administrator/Desktop/Joints-Data-Elims-master/datasets/train.csv", 
    low_memory=False)
def plot_damage_grade(df):
    fig = px.bar(df['damage_grade'].value_counts().reset_index(), 
                 x='index', 
                 y='damage_grade', 
                 color='damage_grade', 
                 # turn off the legend
                 template='plotly_white',
                 labels={'index':'Damage Grade', 'damage_grade':'Count'})
    fig.show()
    return

plot_damage_grade(df)

