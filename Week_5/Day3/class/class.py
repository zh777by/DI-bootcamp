import matplotlib.pyplot as plt

# Creating a figure and axes
fig, ax = plt.subplots()  # Create a figure containing a single axes
x = [1, 2, 3, 4, 5]  # Prices
y = [5, 4, 3, 2, 1]  # Demand
ax.plot(x, y)