import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import sklearn.linear_model as linear_model
import sklearn.neighbors as neighbors


# Read the csv and excel files
better_life_index = pd.read_csv('better_life_index.csv',sep=',')
gdp_per_capita = pd.read_excel('gdp.xlsx',thousands=',')

#Prepare a function for return a country stats
def country_stats(gdp,bli):
    #Take only where life satisfaction is given
    df_bli = bli.loc[np.logical_and(bli.Indicator == 'Life satisfaction', bli.Inequality == 'Total')]
    df_bli = df_bli[['Country','Value']]

    #Take the gdp value from gdp frame
    df_gdp = gdp[['Country','gdp']]

    #Merge two dataframes on column 'country'
    df = pd.merge(df_bli,df_gdp,on='Country')

    return df


#x - as GDP per capita
country_data = country_stats(gdp_per_capita,better_life_index)

#Prepare the data
x = np.c_[country_data['gdp']]
y = np.c_[country_data['Value']]

#visualize the original data
#country_data.plot(kind='scatter',x='gdp',y='Value')

#select a linear model
model = linear_model.LinearRegression()

### Seect K-nearest neighbour method
#model = neighbors.KNeighborsRegressor(n_neighbors=3)



######Train the model
model.fit(x,y)

# Make an numpy array of data to predict the model
data_x = list(np.linspace(min(x),max(x),40))
data_y = []
data_original = []

#Make Predictions in loop
for i in range(len(data_x)):
    y = (model.predict([data_x[i]]))
    data_y.append(y[0][0])
    y_original = (model.predict([x[i]]))
    data_original.append(y[0][0])

#Append the predicted values and plot for comparasion purposes
country_data['Value_1'] = data_y
country_data['Value_orig'] = data_original
country_data.plot(x='gdp', y=['Value','Value_orig', 'Value_1'], figsize=(10,5), grid=True,kind='line')
plt.show()