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

    print(df2)

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
