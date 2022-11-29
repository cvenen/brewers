import pandas as pd

data = pd.read_csv('pitcher_data.csv')

# Count how many pitches each pitcher throws
pitchers = ['Dallas, Micah', 'Smith, Hagen', 'Morris, Zack', 'Menefee, Joseph', 
    'Vermillion, Zebulon', 'Taylor, Evan', 'Tucker, Wyatt', 'Tygart, Brady']
counts = [0] * len(pitchers)

for x in range(len(pitchers)):
    i = 0
    while i < len(data):
        if data.iloc[i, 0] == pitchers[x]:
            counts[x] += 1
        i += 1
    print(pitchers[x] + ': ' + str(counts[x]))
