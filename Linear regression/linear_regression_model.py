import numpy as np
import pandas as pd
import matplotlib
import matplotlib.pyplot as plt
import sklearn


# Read the csv and excel files
better_life_index = pd.read_csv('better_life_index.csv',sep=',')
gdp_per_capita = pd.read_excel('gdp.xls')