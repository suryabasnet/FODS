#Write a Python program to draw a line with suitable label in the x axis, y axis and a title.
import matplotlib.pyplot as plt
X = range(1, 100)
Y = [value * 2 for value in X]
print("Values of X:")
print(*range(1,100))
print("Values of Y (twice of X):")
print(Y)
# Plot lines and/or markers to the Axes.
plt.plot(X, Y)
# Set the x axis label of the current axis.
plt.xlabel('x - axis')
# Set the y axis label of the current axis.
plt.ylabel('y - axis')
# Set a title
plt.title('Number of Covid Cases.')
# Display the figure.
plt.show()
