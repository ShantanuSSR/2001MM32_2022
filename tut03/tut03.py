import pandas as pd
import os
os.system('cls')

from datetime import datetime
start_time = datetime.now()

#Help https://youtu.be/H37f_x4wAC0
def octant_longest_subsequence_count():
    df1 = pd.read_excel('input_octant_longest_subsequence.xlsx')
    df2 = pd.read_excel('input_octant_longest_subsequence.xlsx')

    df2.drop(df2.columns[df2.columns.str.contains('unnamed', case=False)], axis=1, inplace=True)

    len1 = len(df1['Time'])
    # lets start with data pre-processing
    df2['Time'] = df1['Time']
    df2['U'] = df1['U']
    df2['V'] = df1['V']
    df2['W'] = df1['W']

    U_avg = df2['U'].mean()
    V_avg = df2['V'].mean()
    W_avg = df2['W'].mean()

    df2.loc[0, 'U Avg'] = U_avg
    df2.loc[0, 'V Avg'] = V_avg
    df2.loc[0, 'W Avg'] = W_avg

    for x in range(len1):
        df2.loc[x, "U'=U - U avg"] = df2.loc[x, 'U'] - df2.loc[0, 'U Avg']
        df2.loc[x, "V'=V - V avg"] = df2.loc[x, 'V'] - df2.loc[0, 'V Avg']
        df2.loc[x, "W'=W - W avg"] = df2.loc[x, 'W'] - df2.loc[0, 'W Avg']

    for n in range(len1):
        x = df2.loc[n, "U'=U - U avg"]
        y = df2.loc[n, "V'=V - V avg"]
        z = df2.loc[n, "W'=W - W avg"]

        if (x > 0 and y > 0 and z > 0):
            df2.loc[n, 'Octant'] = 1
        if (x > 0 and y > 0 and z < 0):
            df2.loc[n, 'Octant'] = -1
        if (x > 0 and y < 0 and z > 0):
            df2.loc[n, 'Octant'] = 4
        if (x > 0 and y < 0 and z < 0):
            df2.loc[n, 'Octant'] = -4
        if (x < 0 and y > 0 and z > 0):
            df2.loc[n, 'Octant'] = 2
        if (x < 0 and y > 0 and z < 0):
            df2.loc[n, 'Octant'] = -2
        if (x < 0 and y < 0 and z > 0):
            df2.loc[n, 'Octant'] = 3
        if (x < 0 and y < 0 and z < 0):
            df2.loc[n, 'Octant'] = -3

    # print(df2)
    # the lists that is l1,l2,l3......l8 store the total no of repeated counts for 1,-1,2,-2 .... 
    # the values in c1,c2,c3...c8 stores how many times -1,1,-2,2.... respectively appears
    octant = df2['Octant']
    l1 = []
    c1 = 1
    for i in range(1,len1):
        if octant[i-1]==1 and octant[i]==1:
            c1 = c1 + 1
        else:
            l1.append(c1)
            c1 = 1

    l2 = []
    c2 = 1
    for i in range(1,len1):
        if octant[i-1]==-1 and octant[i]==-1:
            c2 = c2 + 1
        else:
            l2.append(c2)
            c2 = 1
    
    l3 = []
    c3 = 1
    for i in range(1,len1):
        if octant[i-1]==2 and octant[i]==2:
            c3 = c3 + 1
        else:
            l3.append(c3)
            c3 = 1
    
    l4 = []
    c4 = 1
    for i in range(1,len1):
        if octant[i-1]==-2 and octant[i]==-2:
            c4 = c4 + 1
        else:
            l4.append(c4)
            c4 = 1
    
    l5 = []
    c5 = 1
    for i in range(1,len1):
        if octant[i-1]==3 and octant[i]==3:
            c5 = c5 + 1
        else:
            l5.append(c5)
            c5 = 1
    
    l6 = []
    c6 = 1
    for i in range(1,len1):
        if octant[i-1]==-3 and octant[i]==-3:
            c6 = c6 + 1
        else:
            l6.append(c6)
            c6 = 1
    
    l7 = []
    c7 = 1
    for i in range(1,len1):
        if octant[i-1]==4 and octant[i]==4:
            c7 = c7 + 1
        else:
            l7.append(c7)
            c7 = 1
    
    l8 = []
    c8 = 1
    for i in range(1,len1):
        if octant[i-1]==-4 and octant[i]==-4:
            c8 = c8 + 1
        else:
            l8.append(c8)
            c8 = 1

    # Here at this step we are storing the maximum of each list and total amount of time appearing in the lists
    max1 = max(l1)
    cf1 = l1.count(max1)
    max2 = max(l2)
    cf2 = l2.count(max2)
    max3 = max(l3)
    cf3 = l3.count(max3)
    max4 = max(l4)
    cf4 = l4.count(max4)
    max5 = max(l5)
    cf5 = l5.count(max5)
    max6 = max(l6)
    cf6 = l6.count(max6)
    max7 = max(l7)
    cf7 = l7.count(max7)
    max8 = max(l8)
    cf8 = l8.count(max8)

from platform import python_version
ver = python_version()

if ver == "3.8.10":
    print("Correct Version Installed")
else:
    print("Please install 3.8.10. Instruction are present in the GitHub Repo/Webmail. Url: https://pastebin.com/nvibxmjw")


octant_longest_subsequence_count()






#This shall be the last lines of the code.
end_time = datetime.now()
print('Duration of Program Execution: {}'.format(end_time - start_time))
