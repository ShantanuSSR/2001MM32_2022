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


octant_transition_count(mod)