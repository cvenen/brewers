import pandas as pd
import matplotlib.pyplot as plt

data = pd.read_csv('pitcher_data.csv')

# Find the sequence of pitches resulting in StrikeCalled for each pitcher
pitchers = ['Dallas, Micah', 'Smith, Hagen', 'Menefee, Joseph']
sequences = [[],[],[]]
for x in range(len(sequences)):
    i = 0
    while i < len(data):
        if data.iloc[i, 0] == pitchers[x]:
            if data.iloc[i, 2] == 'StrikeCalled':
                duo = []
                curr_pitch = data.iloc[i, 1]
                if i != 0 and data.iloc[i, 0] == data.iloc[i-1, 0]:
                    prev_pitch = data.iloc[i-1, 1]
                    duo.append(prev_pitch)
                duo.append(curr_pitch)
                sequences[x].append(duo)
        i += 1

# Find the types pitches in each sequence per pitcher
pitch_types = [[], [], []]
for x in range(len(pitch_types)):
    i = 0
    while i < len(sequences[x]):
        duo = sequences[x][i]
        if i == 0:
            pitch_types[x].append(duo)
        else:
            if duo not in pitch_types[x]:
                pitch_types[x].append(duo)
        i += 1

# Count occurence of each sequence per pitcher
counts = [[0] * len(pitch_types[0]), [0] * len(pitch_types[1]), [0] * len(pitch_types[2])]
for x in range(len(counts)):
    for a in range(len(pitch_types[x])):
        i = 0
        while i < len(sequences[x]):
            if sequences[x][i] == pitch_types[x][a]:
                counts[x][a] += 1
            i += 1

# Graph the sequences thrown for each pitcher
names = ['Dallas', 'Smith', 'Menefee']
colors = ['blue', 'orange', 'green']
num = 0
while num < 3:
    keys = []
    values = []
    i = 0
    while i < len(pitch_types[num]):
        if len(pitch_types[num][i]) != 1:
            key = pitch_types[num][i][0] + ", " + pitch_types[num][i][1]
        else:
            key = pitch_types[num][i][0]
        keys.append(key)
        i += 1

    x = 0
    while x < len(counts[num]):
        values.append(counts[num][x])
        x += 1

    fig = plt.figure(num + 7, figsize = (12, 6))

    plt.bar(list(keys), list(values), color = colors[num])
    plt.xticks(rotation = 30, ha='right')
    plt.xlabel('Pitch Sequence')
    plt.ylabel('Number of Sequences Thrown')
    plt.title('Pitch Sequences Resulting in StrikeCalled for ' + names[num])
    num += 1
plt.show()
