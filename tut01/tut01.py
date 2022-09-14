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


#reading the input file
data_framing = pd.read_csv("octant_input.csv") 

# doing data pre-prcessing:
data_framing.at[0,'u_mean']=data_framing['U'].mean() 
data_framing.at[0,'v_mean']=data_framing['V'].mean()
data_framing.at[0,'w_mean']=data_framing['W'].mean()

data_framing['U-u_mean']=data_framing['U']-data_framing.at[0,'u_mean']
data_framing['V-v_mean']=data_framing['V']-data_framing.at[0,'v_mean']
data_framing['W-w_mean']=data_framing['W']-data_framing.at[0,'w_mean']

data_framing['octant'] = data_framing.apply(lambda y: octant_ident(y['U-u_mean'], y['V-v_mean'], y['W-w_mean']),axis=1)

data_framing[' '] = ''
data_framing.at[1,' '] = 'user input'

#counting overall using value_counts function
data_framing.at[0,'octant ID'] = 'overall count'
data_framing.at[0,'-1'] = data_framing['octant'].value_counts()[-1]
data_framing.at[0,'-2'] = data_framing['octant'].value_counts()[-2]
data_framing.at[0,'-3'] = data_framing['octant'].value_counts()[-3]
data_framing.at[0,'-4'] = data_framing['octant'].value_counts()[-4]
data_framing.at[0,'1']  = data_framing['octant'].value_counts()[1]
data_framing.at[0,'2']  = data_framing['octant'].value_counts()[2]
data_framing.at[0,'3'] = data_framing['octant'].value_counts()[3]
data_framing.at[0,'4'] = data_framing['octant'].value_counts()[4]

