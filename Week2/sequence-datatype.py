# -*- coding: utf-8 -*-
"""
Created on Tue Sep 22 08:19:46 2020

@author: Ojas Gupta
"""

str="ojas" #this is how you create a string
obj=[1,2,3,4,5,6] #this is how you create a list
print(str)
obj1=[1,2,3,4,'a',"ojas"]  #list with mixed data types
print(obj1)
from array import *
arr=array('i',(1,2,3,4))
print(arr)
for x in arr : print(x) #this is how you declare an array using array import
                         #using python and use for loops

tup=(1,2,3) #tuple. The values of the tuples cannot be changed.
oj={1:"first",2:"last",3:"Second"} #decalring the dictionary
print(oj)
for k in oj : print(k) 
ojas=dict([('first',1),('Second',2)])
print(ojas)  # Creating dictionary using dict function
   # A list can be an element of a dictionary
rn=range(1,12)
for x in rn: print(x) # in the range funciton,the values store are the starting value and the hughest value-1.
                       # We can print the values using for loops.