import pandas as pd

def octant_transition_count(mod=5000):
     try:
        # reading excel to pandas dataframe
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


octant_transition_count(mod)