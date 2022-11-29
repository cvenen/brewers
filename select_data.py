import pandas as pd

# Read data from the original csv
data = pd.read_csv('20220423-Olsen-1.csv')

# Make a new csv with select data
pitcher = ''
type = ''
call = ''
rate = 0

df = pd.DataFrame({'Pitcher': [pitcher], 'AutoPitchType': [type], 'PitchCall': [call], 'SpinRate': [rate]})

i = 0
while i < len(data):
    pitcher = data.iloc[i, 5]
    type = data.iloc[i, 20]
    call = data.iloc[i, 21]
    rate = data.iloc[i, 31]
    df2 = {'Pitcher': pitcher, 'AutoPitchType': type, 'PitchCall': call, 'SpinRate': rate}
    df = df.append(df2, ignore_index = True)
    i += 1

df.to_csv('pitcher_data.csv', index=False)