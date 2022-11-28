import pandas as pd

data = pd.read_csv('pitcher_data.csv')

pitchers = ["Dallas, Micah", "Smith, Hagen", "Menefee, Joseph"]

# Find number of strikes thrown for each pitcher
strike_counts = [0, 0, 0]
for x in range(len(pitchers)):
    i = 0
    while i < len(data):
        if data.iloc[i, 0] == pitchers[x]:
            if data.iloc[i, 2] == "StrikeCalled":
                strike_counts[x] += 1
        i += 1

# Find the sequence of pitches
sequences = [[],[],[]]

for x in range(len(sequences)):
    i = 0
    while i < len(data):
        if data.iloc[i, 0] == pitchers[x]:
            if data.iloc[i, 2] == "StrikeCalled":
                duo = []
                curr_pitch = data.iloc[i, 1]
                if i != 0:
                    prev_pitch = data.iloc[i-1, 1]
                    duo.append(prev_pitch)
                duo.append(curr_pitch)
                sequences[x].append(duo)
        i += 1

# Find types of each sequence
types = [[], [], []]

for x in range(len(types)):
    i = 0
    while i < len(sequences[x]):
        duo = sequences[x][i]
        if i == 0:
            types[x].append(duo)
        else:
            if duo not in types[x]:
                types[x].append(duo)
        i += 1

# Count number of each sequence type
counts = [[0] * len(types[0]), [0] * len(types[1]), [0] * len(types[2])]

for x in range(len(counts)):
    for a in range(len(types[x])):
        i = 0
        while i < len(sequences[x]):
            if sequences[x][i] == types[x][a]:
                counts[x][a] += 1
            i += 1

# Print findings
for x in range(len(types)):
    print()
    print(pitchers[x])
    for i in range(len(types[x])):
        print(str(types[x][i]) + ": " + str(counts[x][i]))



