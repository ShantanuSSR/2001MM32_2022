import pandas as pd

def octant_transition_count(mod=5000):
    
    try:
        data_framing = pd.read_excel('input_octant_transition_identify.xlsx')
    except:
        print("Error: File not found")
    u_mean = data_framing["U"].mean()
    v_mean = data_framing["V"].mean()
    w_mean = data_framing["W"].mean()

    data_framing['U avg'] = pd.Series([u_mean], dtype='float64')
    data_framing['V avg'] = pd.Series([v_mean], dtype='float64')
    data_framing['W avg'] = pd.Series([w_mean], dtype='float64')

    data_framing["U'=U - U avg"] = data_framing['U'] - u_mean
    data_framing["V'=V - V avg"] = data_framing['V'] - v_mean
    data_framing["W'=W - W avg"] = data_framing['W'] - w_mean

    oct = []
    len = data_framing.shape[0]

    val = 0
    for i in range(len):  # finding the octact

        if data_framing.at[i, "U'=U - U avg"] >= 0 and data_framing.at[i, "V'=V - V avg"] >= 0:
            val = 1
            if data_framing.at[i, "W'=W - W avg"] < 0:
                val = val*(-1)
            oct.append(val)

        elif data_framing.at[i, "U'=U - U avg"] < 0 and data_framing.at[i, "V'=V - V avg"] >= 0:
            val = 2
            if data_framing.at[i, "W'=W - W avg"] < 0:
                val = val*(-1)
            oct.append(val)

        elif data_framing.at[i, "U'=U - U avg"] < 0 and data_framing.at[i, "V'=V - V avg"] < 0:
            val = 3
            if data_framing.at[i, "W'=W - W avg"] < 0:
                val = val*(-1)
            oct.append(val)

        elif data_framing.at[i, "U'=U - U avg"] >= 0 and data_framing.at[i, "V'=V - V avg"] < 0:
            val = 4
            if data_framing.at[i, "W'=W - W avg"] < 0:
                val = val*(-1)
            oct.append(val)
    data_framing['Octact'] = oct

    count_dict = {1: 0, -1: 0, 2: 0, -2: 0, 3: 0, -3: 0, 4: 0, -4: 0}
    range_count_dict = {}

    lo = 0
    hi = mod

    while lo < len:  # finding count for each octact
        for x in range(lo, min(hi, len)):
            count_dict[data_framing.at[x, 'Octact']] += 1
        range_count_dict[str(lo) + '-' + str(hi-1)] = count_dict

        count_dict = {1: 0, -1: 0, 2: 0, -2: 0, 3: 0, -3: 0, 4: 0, -4: 0}

        lo = hi 
        hi = hi + mod

    for x in range(len):
        count_dict[data_framing.at[x, 'Octact']] += 1

    transition = [[0]*8 for _ in range(8)]
    range_transition = {}

    lo = 0
    hi = mod

    pos = {1: 0, -1: 1, 2: 2, -2: 3, 3: 4, -3: 5, 4: 6, -4: 7}

    while lo < len:  # finding the transition count
        for x in range(lo, min(hi, len)):
            if x+1 < len:
                i = pos[data_framing.at[x, 'Octact']]
                j = pos[data_framing.at[x+1, 'Octact']]

                transition[i][j] += 1

        range_transition[str(lo) + '-' + str(hi-1)] = transition

        transition = [[0]*8 for _ in range(8)]

        lo = hi 
        hi = hi + mod
    x = len
    while x>=0:
        if x+1 < len:
            i = pos[data_framing.at[x, 'Octact']]
            j = pos[data_framing.at[x+1, 'Octact']]

            temp = transition[i][j]
            transition[i][j] = temp + 1
        x = x-1

    data_framing.at[1, "dummy"] = "User Input"
    data_framing.rename(columns={'dummy': ''}, inplace=True)

    data_framing["dummy"] = pd.Series([], dtype='float64')
    data_framing.rename(columns={'dummy': ''}, inplace=True)

    data_framing[1] = pd.Series([], dtype='float64')
    data_framing[-1] = pd.Series([], dtype='float64')
    data_framing[2] = pd.Series([], dtype='float64')
    data_framing[-2] = pd.Series([], dtype='float64')
    data_framing[3] = pd.Series([], dtype='float64')
    data_framing[-3] = pd.Series([], dtype='float64')
    data_framing[4] = pd.Series([], dtype='float64')
    data_framing[-4] = pd.Series([], dtype='float64')

    data_framing.iat[0, 12] = "count_dictl Count"
    for x in count_dict:
        data_framing.at[0, x] = count_dict[x]

    data_framing.iat[1, 12] = "Mod " + str(mod)

    row = 2
    for x in range_count_dict:
        data_framing.iat[row, 12] = x
        arr = range_count_dict[x]
        for i in arr:
            data_framing.at[row, i] = arr[i]
        row += 1
    data_framing.iat[row, 12] = "Verified"
    for x in count_dict:
        data_framing.at[row, x] = count_dict[x]

    decode = {0: 1, 1: -1, 2: 2, 3: -2, 4: 3, 5: -3, 6: 4, 7: -4}

    row += 3
    data_framing.iat[row, 12] = "count_dictl Transition Count"
    row += 1
    data_framing.iat[row, 13] = "To"
    row += 1
    data_framing.iat[row, 12] = "Count"
    for x in pos:
        data_framing.at[row, x] = x
    row += 1
    data_framing.iat[row, 11] = "From"
    c = 0
    for i in range(8):
        data_framing.iat[row, 12] = decode[c]
        for j in range(8):
            data_framing.at[row, decode[j]] = transition[i][j]
        row += 1
        c += 1


    for x in range_transition:
        mod_trans = range_transition[x]

        row += 2
        data_framing.iat[row, 12] = "Mod Transition Count"
        row += 1
        data_framing.iat[row, 12] = x
        data_framing.iat[row, 13] = "To"
        row += 1
        data_framing.iat[row, 12] = "Count"
        for x in pos:
            data_framing.at[row, x] = x
        row += 1
        data_framing.iat[row, 11] = "From"
        c = 0
        for i in range(8):
            data_framing.iat[row, 12] = decode[c]
            for j in range(8):
                data_framing.at[row, decode[j]] = mod_trans[i][j]
            row += 1
            c += 1
    try:
            data_framing.to_excel('output_octant_transition_identify.xlsx',
                        index=False)  # writing the dataframe to excel file
    except:
        print("Error: Cannot create Excel file")

    print("Finished Executing")


try:
    mod = 5000  # variable value can be changed
    octant_transition_count(mod)
except:
    print("Some error occured")


