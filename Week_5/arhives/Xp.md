## XP 

# What you will learn:

- Line and scatter plot creation: Understand and implement basic data visualization techniques to visualize relationships between variables.
- Saving plots: Learn how to save your visualizations for further use or presentation.
- Plotting mathematical functions: Understand how to use Matplotlib to visualize complex mathematical functions.
- Multiple plots and subplots: Learn how to display multiple plots in the same figure for better comparison and understanding.
- Legend addition: Enhance the clarity of your plots by adding a legend that maps data elements to their representation on the plot.
- Histogram creation: Understand how to use histograms to visualize the distribution of data.


**1.** Install Matplotlib and import it into a Python script using `import matplotlib.pyplot as plt`.

**2.** Create a basic line plot using the following data, which represents the demand for a product at different price points. Lower prices are usually associated with higher demand:
```python
x = [1, 2, 3, 4, 5]  # Prices
y = [5, 4, 3, 2, 1]  # Demand
```

   Plot the `x` and `y` lists and display the plot.

_The output should look like this:_
![Alt text](media/xp2.png)

**3.** Create a basic scatter plot using the following data, which represents children's heights at different ages:
    ```python
    x = [1, 2, 3, 4, 5]  # Age
    y = [75, 80, 88, 95, 105]  # Height in cm
    ```
   Plot the `x` and `y` lists using a scatter plot and display the plot.

_The output should look like this:_
![Alt text](media/xp3.png)

**4.** Modify the line plot from Exercise 2 to include a title ("Product Demand vs Price"), and labels for the x-axis ("Price") and y-axis ("Demand").

_The output should look like this:_
![Alt text](media/xp4.png)

**5.** Modify the scatter plot from Exercise 3 to include a title ("Children's Height vs Age"), and labels for the x-axis ("Age (years)") and y-axis ("Height (cm)").

_The output should look like this:_
![Alt text](media/xp5.png)

**6.** Save both plots (from exercises 4 and 5) to your local machine as .png files. Use the `savefig` function from Matplotlib.

---
For exercises 7-9: You can use the following data for producing the plots:
```python
x = np.linspace(-10, 10, 1000)
y1 = np.sin(x)
y2 = np.cos(x)
```
---

**7.** Create a line plot and scatter plot representing your favorite mathematical functions. Change the line color to `tab:blue` for the line plot and use a marker of your choice for the scatter plot.

_The output should look like this:_
![Alt text](media/xp7.png)

**8.** Plot the line plot and scatter plot from Exercise 7 on the same figure using subplots. Use `plt.subplots` to create a figure with two subplots.

_The output should look like this:_
![Alt text](media/xp8.png)

**9.** Modify the plots from Exercise 8 to include a legend. Use the `legend` function from Matplotlib.

_The output should look like this:_
![Alt text](media/xp9.png)

**10.**  Plot a histogram using the following data, which represents the distribution of grades in a class:
    ```python
    grades = [88, 90, 95, 92, 88, 90, 88, 85, 93, 92, 90, 87, 95, 90, 88]
    ```
    Use the `hist` function to create the histogram.

_The output should look like this:_
![Alt text](media/xp10.png)

**Duration (approx)**
2h