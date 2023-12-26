#https://colab.research.google.com/drive/1vG83NJTgxe-a1CM2mz_WXso5wD3aJkoD?usp=sharing

#https://colab.research.google.com/drive/1atSDjVt8f6c44Ww_80JCXRkh4k126F4U


import matplotlib.pyplot as plt

# Creating a figure and axes
fig, ax = plt.subplots()  # Create a figure containing a single axes
x = [1, 2, 3, 4, 5]  # Prices
y = [5, 4, 3, 2, 1]  # Demand
ax.plot(x, y)