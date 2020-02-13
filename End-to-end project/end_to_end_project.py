import pandas as pd
import os
import matplotlib.pyplot as plt
import functions_support


currentDirectory = os.getcwd()

#Specify the data paths
HOUSING_PATH = os.path.join("datasets", "housing")

def load_housing_data(housing_path=HOUSING_PATH):
    csv_path = os.path.join(housing_path, "housing.csv")
    return pd.read_csv(csv_path)

housing = load_housing_data(HOUSING_PATH)

'''
#Looks at the data Analysis from the csv file using Pandas -not necessary
housing_data.head()
housing_data.describe()
housing_data['ocean_proximity'].value_counts()
housing_data['ocean_proximity'].describe()
'''
### Display the data visually by histogram
'''
housing.hist(bins=50, figsize=(20,15))
functions_support.save_fig("attribute_histogram_plots")
plt.show()
'''
## Get the test data with 20% ratio
train_set, test_set = functions_support.split_train_test(housing, 0.2)