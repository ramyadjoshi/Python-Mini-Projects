from matplotlib import pyplot as plt

x = []
y = []

for i in range(100):
    x.append(i)
    y.append(i)

    # Mention x and y limits to define their range
    plt.xlim(0, 100)
    plt.ylim(0, 100)
    
    # Plotting graph
    plt.plot(x, y, color = 'green')
    plt.pause(0.01)

plt.show()
# for bar graph animation
from matplotlib import pyplot as plt
from matplotlib.animation import FuncAnimation, writers
import numpy as np

fig = plt.figure(figsize = (7,5))
axes = fig.add_subplot(1,1,1)
axes.set_ylim(0, 300)
palette = ['blue', 'red', 'green', 
           'darkorange', 'maroon', 'black']

y1, y2, y3, y4, y5, y6 = [], [], [], [], [], []

def animation_function(i):
    y1 = i
    y2 = 5 * i
    y3 = 3 * i
    y4 = 2 * i
    y5 = 6 * i
    y6 = 3 * i

    plt.xlabel("Country")
    plt.ylabel("GDP of Country")
    
    plt.bar(["India", "China", "Germany", 
             "USA", "Canada", "UK"],
            [y1, y2, y3, y4, y5, y6],
            color = palette)

plt.title("Bar Chart Animation")

animation = FuncAnimation(fig, animation_function, 
                          interval = 50)
plt.show()
#  horizontal animation
from matplotlib import pyplot as plt
from matplotlib.animation import FuncAnimation
import random
import numpy as np

x = []
y = []
colors = []
fig = plt.figure(figsize=(7,5))

def animation_func(i):
    x.append(random.randint(0,100))
    y.append(random.randint(0,100))
    colors.append(np.random.rand(1))
    area = random.randint(0,30) * random.randint(0,30)
    plt.xlim(0,100)
    plt.ylim(0,100)
    plt.scatter(x, y, c = colors, s = area, alpha = 0.5)

animation = FuncAnimation(fig, animation_func, 
                          interval = 100)
plt.show()
