import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

train_data = pd.read_csv(\
    "C:/Users/Administrator/Desktop/Joints-Data-Elims-master/datasets/train.csv", 
    low_memory=False)

# remove the space in column names
train_data.columns = train_data.columns.str.replace(' ', '')
string_columns = ['floors_before_eq(total)','land_surface_condition','type_of_foundation','type_of_roof','type_of_ground_floor',
                  'type_of_other_floor','position','building_plan_configuration' ,'technical_solution_proposed',
                  'legal_ownership_status','residential_type','public_place_type','industrial_use_type',
                  'govermental_use_type','flexible_superstructure']

# Make every values in every column to lowercase
def make_lower_case(column):
    column = str(column)
    return column.lower()

for col in string_columns:
    train_data[col] = train_data[col].apply(make_lower_case)


def make_eda_using_correlation_within_damagegrade(df, cols):
    correlate = pd.DataFrame(
    index=['1', '2','3','4','5'], 
    columns=df[cols].unique())

    for j  in df[cols].unique():
        try : 
            
            correlate.loc[correlate.index == '1', j]= \
                np.round(sum((df[cols]==j)&\
                            (df['damage_grade']==1))/sum(df[cols]==j) * 100, 3)
            
            correlate.loc[correlate.index == '2', j]= \
                np.round(sum((df[cols]==j)&\
                            (df['damage_grade']==2))/sum(df[cols]==j) * 100, 3)
            
            correlate.loc[correlate.index == '3', j]= \
                np.round(sum((df[cols]==j)&\
                            (df['damage_grade']==3))/sum(df[cols]==j) * 100, 3)
            
            correlate.loc[correlate.index == '4', j]= \
                np.round(sum((df[cols]==j)&\
                            (df['damage_grade']==4))/sum(df[cols]==j) * 100, 3)
            
            correlate.loc[correlate.index == '5', j]= \
                np.round(sum((df[cols]==j)&\
                            (df['damage_grade']==5))/sum(df[cols]==j) * 100, 3)
            
        except :
            pass
    return correlate

percentage = make_eda_using_correlation_within_damagegrade(train_data, 'type_of_foundation')

def my_autopct(pct):
    return ('%.2f' % pct) if pct > 20 else ''

percentage.drop(['nan'], axis=1, inplace=True)

fig, ax = plt.subplots(3, 4, figsize=(20, 14))
for i in range(3):
    for j in range(4):
        if i == 2 and j == 3:
            break
        ax[i, j].pie(\
            percentage[percentage.columns[i*4+j]], 
            labels=percentage.index, autopct=my_autopct,
            startangle=90, shadow=True, explode=(0.1, 0, 0, 0, 0),
            colors=['#0d0887', '#3e09ff', '#8c0fa2', '#d35170', '#f0f921'],
            # change color of the text autopct
            textprops={'color': 'white', 'fontsize': 8, 'fontweight': 'bold'})
        ax[i, j].set_title(percentage.columns[i*4+j])
ax[2, 3].axis('off')
fig.suptitle(\
    '', 
    fontsize=25, fontweight='bold', fontfamily='serif')
fig.legend(\
    labels=['1', '2', '3', '4', '5'],
    loc='lower center', ncol=5,
    fontsize=20, frameon=False,
    bbox_to_anchor=(0.5, 0.01))
plt.show()