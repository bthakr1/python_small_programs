# Importing the required libraries

import pandas as pd 
import numpy as np
import ssl
import os
import seaborn as sns
import matplotlib.pyplot as plt
ssl._create_default_https_context = ssl._create_unverified_context

# Check the directory

os.chdir("/Users/bt/Documents/GITHUB/python_small")

# Importing the data frame we will
# be using in this exercise.

reviews = pd.read_csv("winemag-data_first150k.csv", index_col=False)


# Dropping the unneccessary column 
# from the dataframe

reviews.drop(columns={'Unnamed: 0'},inplace=True)

# Let's see the distribution of "price" in the dataset

print(reviews['price'].describe())

# We can also draw the boxplot for "price" to see the distribution

reviews = pd.DataFrame(reviews)

boxplot_price = reviews.boxplot(column='price')
boxplot_price.plot()
plt.show()

