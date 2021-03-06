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


# Let's check the last row of the dataframe

print("\n\n")
print(reviews.iloc[-5:,])

# It seems that we have done a lot of exercise on iloc. 
# Let's now practice loc

# The differnce between iloc and loc is in iloc we can provide numbers to select the columns
# This may not be the case in loc , where we can suggest the name of feature or column

print("\n")
# The below command will give us first 5 values for column "country"
print(reviews.loc[0:5,"country"])

# Let's check other columns as well

print("\n\n")
print(reviews.loc[20:25,'winery'])

# We can also select multiple columns from the data frame
# In the following loc command we have selected the column "price" and "winery"

print(reviews.loc[2:12,['price','winery']])

# loc is label based : It means we can provide the "names" of columns

# Here we have refined the data framed based on "winery" and "points"
print("\n\n")
print(reviews.loc[(reviews['winery'] == 'Ponzi') & (reviews['points']> 94)])

# from row 3 to 7, without any filter
print("\n\n")
print(reviews.loc[3:7])

# iloc in comparison is different since it is based on index. 

# suppose we want to select random rows of data from the dataframe

list_needed = [12,34,56,78,5,11]

print("\n\n")
print(reviews.loc[list_needed])

# lets say we want only 2,3, and 5 columns

columns_needed = [2,3,5]

print("\n\n")
print(reviews.iloc[list_needed,columns_needed])

# Thats all for iloc and loc