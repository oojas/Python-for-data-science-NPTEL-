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

copy=read.copy(deep=false) # Shallow Copy ( Similar to Call by refernce)
copy1=read.copy(deep=true) # Deep Copy ( Similar to Call by Value)
