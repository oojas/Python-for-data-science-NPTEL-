# -*- coding: utf-8 -*-
"""
Created on Tue Oct  6 22:42:34 2020

@author: Ojas Gupta

"""

# READING DATA

# importing the libraries and using them to read the csv files.
import os
import pandas as pd
os.chdir("C:/Users/Ojas Gupta/Desktop/Activation Keys") # Reading the csv file from local system 
read=pd.read_csv('Project_Details.csv',index_col=0,na_values=["??"])

print(read)

# demo=pd.read_excel('') Reading the excel sheet usng pandas

rea=pd.read_table('Keys.txt')
print(rea)

# We are having 9 rows and 1 column because the values are separated by very less space
# that's why we use demlimiter/sep but sep is most prefered.
rea1=pd.read_table('Keys.txt',sep='\t')
print(rea1)
# how to copy data

copy=read.copy(deep=False) # Shallow Copy ( Similar to Call by refernce)
copy1=read.copy(deep=True) # Deep Copy ( Similar to Call by Value)
print(read.columns)
  # To get the labels the syntax is dataframe.index(Rows) or dataframe.columns
print(read.index)
print(read.shape) # to get the dimensions of the table.
print(read.memory_usage())
print(read.head(3))
# you can also view more functions that pandas provide using the variable explorer

print(read.at[1,'Ojas Gupta'])
#print(read.loc([:'Ojas Gupta']))

# Pandas Part ||

print(read.dtypes) # function used for checking up the datatypes of the dataframes
# syntax : dataframe.dtypes
print(read.get_types_counts()) # Counts the number of variable with same dtypes
# An object dttpe means that it contains more than one datatype.
num_1 = 546
num_2 = '786'
print (num_1 + num_2)
x=10
def func(num):
    x=5
    for i in num:
        x*=i
    return x
print(func((-2,-1,1,2,3)))    




