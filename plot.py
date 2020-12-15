import matplotlib.pyplot as plt

data = {'feature_1': 10, 
        'feature_2' : 20, 
        'feature_3': 5
}

Y = [feature for feature in data]
X = [data[feature] for feature in data]
width = 0.35       # the width of the bars: can also be len(x) sequence

fig, ax = plt.subplots()

ax.bar(Y, X, width)

ax.set_ylabel('# clicked')
ax.set_title('Example')
ax.legend()

plt.show()
