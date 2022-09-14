#Shantanu Singh 2001MM32

#importing pandas
import pandas as pd 

#function for categorizing the data into different octant 
def octant_ident(x,y,z):
    if x>0 and y>0 and z>0:
        return 1 
    if x>0 and y>0 and z<0:
        return -1 
    if x>0 and y<0 and z>0:
        return  4 
    if x>0 and y<0 and z<0:
        return -4
    if x<0 and y>0 and z>0:
        return 2 
    if x<0 and y>0 and z<0:
        return -2 
    if x<0 and y<0 and z>0:
        return  3 
    if x<0 and y<0 and z<0:
        return -3


