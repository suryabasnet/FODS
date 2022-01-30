import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

x=[0,1,2,3,4]
y=[0,2,4,6,8]

#resize your graph(dpi specifies quality, use 300 when saving)
plt.figure(figsize=(5,4), dpi=100)

##line 1

#keyword Argument Notation

#plt.plot(x,y, label="2x", color="red", linestyle="--" ,linewidth=2, marker='.',markeredgecolor='black', markersize=10)

#Shorthand notation
#fmt='[color][marker][line]'
plt.plot(x,y, 'b*--', label="2x")

##line 2

#select interval we want to plot points at
x2 = np.arange(0,4.5,0.5)

#plot part of graph as line
plt.plot(x2[:6], x2[:6]**2, 'r|-', label="x^2")

#plot remainder of graph as a dot
plt.plot(x2[5:], x2[5:]**2, 'r|--')

#Add a title (specify font parameters with fontdict)
plt.title('Hello World', fontdict={'fontname': 'Brush Script MT', 'fontsize': 40})

#X and Y Labels
plt.xlabel("Time")
plt.ylabel("Date")

#X,Y axis Tickmarks (scale of your graph)
plt.xticks([0,1,2,3,4,5])
plt.yticks([0,2,4,6,8,10])

#Add a Legend
plt.legend()

#save figure (dpi 300 is good for saving)
plt.savefig('my first graph.png', dpi=300)

#show plot
plt.show()
