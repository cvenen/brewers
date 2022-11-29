import pandas as pd

data = pd.read_csv('pitcher_data.csv')

# Initialize array of pitcher names
pitchers = ['Dallas, Micah', 'Smith, Hagen', 'Morris, Zack', 'Menefee, Joseph', 
    'Vermillion, Zebulon', 'Taylor, Evan', 'Tucker, Wyatt', 'Tygart, Brady']

# Calculate success rates 
rate = 0
for x in range(len(pitchers)):
    success_p = 0
    total_p = 0
    i = 0
    while i < len(data):
        if data.iloc[i, 0] == pitchers[x]:
            total_p += 1
            if data.iloc[i, 2] == 'StrikeCalled':
                success_p += 1
        i += 1
    rate = (success_p / total_p) * 100
    print(pitchers[x] + ': ' + str(rate))



