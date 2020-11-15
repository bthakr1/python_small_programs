# Importing the required libraries

import pandas as pd 
import numpy as np
import ssl
import os
ssl._create_default_https_context = ssl._create_unverified_context

# Check the directory

os.chdir("/Users/bt/Documents/GITHUB/python_small")

# Importing the data frame we will
# be using in this exercise.

reviews = pd.read_csv("winemag-data_first150k.csv", index_col=False)

# Dropping the unneccessary column 
# from the dataframe

reviews.drop(columns={'Unnamed: 0'},inplace=True)

# First we will learn more about "loc" and "iLoc"
# These are used to filter the data. Both are row first and column second.

# iloc
# To get the first row

print(reviews.iloc[0,])
print("\n\n")

# To get the second row 

print(reviews.iloc[1,])
print("\n\n")

# To get the 50th row 

print(reviews.iloc[51,])

# Now lets check the column only
# This means we will use ":" (everything) as first option and after comma we will mention the column 
# we would like to select

print(reviews.iloc[:,0])
print("\n\n")
# Now let's select the second column

print(reviews.iloc[:,1])
print("\n\n")
# Enough playing with rows and columns. Let's bring both of them together
# This we can achieve by using Row and Column something different than "everything" (":") operator.

# First Row and Second Column
# Remember iLoc is Row First and Column Second

print(reviews.iloc[0,1])
print("\n\n")

# Let's select a range of rows and columns

# First we will select 1st and 2nd Row and 3rd Column

print(reviews.iloc[0:1,2])