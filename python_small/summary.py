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

# boxplot_price = reviews.boxplot(column='price')
# boxplot_price.plot()
# plt.show()

# info() command will provide the info such as number of non null rows for each 
# column and data types for each column

print(reviews.info())

# Now we will use the describe with a categorical column
# Let's see what happens

print(reviews['country'].describe())

# now we will try to use describe for more than one column

print(reviews[['price','points']].describe())

# You can also transpose it for better viewing
# by using "transpose"

print(reviews[['price','points']].describe().transpose())

# In both methods we were using names of columns
# now we will try to see the describe with numeric column first

print(reviews.dtypes)

list_of_numeric_datatypes = ['int64','float']

print(reviews.describe(include=list_of_numeric_datatypes).transpose())

# How about objects in the dataframe

print(reviews.describe(include='object').transpose())

# The top winery is Williams Selyem and Top country is US
# There are 48 unique countries and 632 unique varities of wines

# How about we identify the unqiue countries included in the dataset
# The "nunique" command gives the Number of unqiue countries in the data set

print(reviews['country'].nunique())

# unique will give us the names of those countries

print(reviews.country.unique())

# we can also see the number of times these countries appeared
# it can be done by using value_counts
print(reviews.country.value_counts())

# So we can say the following 
# nunique() --> Gives the number of unqiue values
# unique() --> Gives the names of those unique values
# value_counts() --> Provides the names with number of occurences

# Now how about finding mean and median for price and points.

print(reviews[['price','points']].mean().transpose())

print(reviews[['price','points']].median().transpose())

# We can also use the "agg" operator for max, min, skew, and median

print(reviews.agg({'price':['max','min','skew','median'],
                    'points':['max','min','skew','median']}))

