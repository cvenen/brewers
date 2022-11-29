import pandas as pd
import matplotlib.pyplot as plt

data = pd.read_csv('pitcher_data.csv')

# Find the types of pitches each pitcher throws
pitchers = ['Dallas, Micah', 'Smith, Hagen', 'Menefee, Joseph']
pitches = [[], [], []]
for x in range(len(pitchers)):
    i = 0
    while i < len(data):
        pitch = data.iloc[i, 1]
        if data.iloc[i, 0] == pitchers[x]:
            pitches[x].append(pitch)
        i += 1
    
# Find the types of pitches thrown
types = [[], [], []]
for x in range(len(types)):
    i = 0
    while i < len(pitches[x]):
        throw = pitches[x][i]
        if i == 0:
            types[x].append(throw)
        else:
            if throw not in types[x]:
                types[x].append(throw)
        i += 1

# Count the number of times each pitch is thrown
counts = [[0] * len(types[0]), [0] * len(types[1]), [0] * len(types[2])]

for x in range(len(counts)):
    for a in range(len(types[x])):
        i = 0
        while i < len(pitches[x]):
            if pitches[x][i] == types[x][a]:
                counts[x][a] += 1
            i += 1

# Make piecharts for each pitcher's breakdowns
title = ['Dallas Pitch Breakdown', 'Smith Pitch Breakdown', 'Menefee Pitch Breakdown']

for x in range(len(pitchers)):
    plt.figure(x)
    plt.pie(counts[x], labels= types[x], autopct= '%1.1f%%', startangle= 90)
    plt.title(title[x])
plt.show()