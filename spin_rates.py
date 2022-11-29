import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

data = pd.read_csv('pitcher_data.csv')

# Find spin rates for Four-Seam, Changeup, Slider, and Sinker pitches
pitchers = ['Dallas, Micah', 'Smith, Hagen', 'Menefee, Joseph']
pitch_type = ['Four-Seam', 'Changeup', 'Slider', 'Sinker']
rate_type = [[[],[],[]], [[],[],[]], [[],[],[]], [[],[],[]]]

# Find spin rate for each pitch type
for index in range(len(pitch_type)):
    i = 0
    while i < len(data):
        if data.iloc[i, 1] == pitch_type[index]:
            rate = data.iloc[i, 3]
            for x in range(len(pitchers)):
                if data.iloc[i, 0] == pitchers[x]:
                    rate_type[index][x].append(rate)
        i += 1

# Create graph for spin rates of each pitch type
labels = ['Dallas', 'Smith', 'Menefee']
titles = ['Spin Rate for Four-Seam Pitches', 'Spin Rate for Changeup Pitches', 'Spin Rate for Slider Pitches', 'Spin Rate for Sinker Pitches']

for a in range(len(rate_type)):
    plt.figure(a + 3)
    for index in range(len(rate_type[a])):
        x = []
        y = rate_type[a][index]
        for i in range(len(rate_type[a][index])):
            x.append(i + 1)
        plt.scatter(x, y, label= labels[index])
        if len(x) != 0:
            z = np.polyfit(x, y, 1)
            p = np.poly1d(z)
            plt.plot(x, p(x))
    plt.title(titles[a])
    plt.xlabel('Number of Pitches')
    plt.ylabel('Spin Rate')
    plt.legend()
plt.show()
        