"""
Make sure the imported packages are installed in your global site_packages,
otherwise this program will result in an error for missing packages.

This algortihm performes a simple linear regression against a diamond data,
which is also called a single variable linear regression.
"""
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

# Read the excel file and collect the data inside a DataFrame
data = pd.read_excel("./11989_Diamond Data.xlsx")

xAxis = 0
yAxis = 1

# Initialize the inputs
b0 = float(input("B0: "))
b1 = float(input("B1: "))
# alpha = float(input("Learning Rate: "))
alpha = 1

def predictYValue(b0, b1, x):
    """
    Calculate the height of the regression line in the given x-axis value.
    :param b0: The intercept of the linne against the y-axis.
    :param b1: The slope of the regressionn line.
    :param x: The x-axis value from the dataset row.
    :return: The predicted Y-axis value.
    """
    return b0 + b1 * x

TYPE_INTERCEPT = 1
TYPE_SLOPE = 2
def calculateError(b0, b1, alpha, data, type):
    """
    Calculate the error based on the type of coefficient being optimized
    :param b0: The intercept of the linne against the y-axis.
    :param b1: The slope of the regressionn line.
    :param alpha: The learning rate, a user configured floating value.
    :param data: The Pandas DataFrame containing the data.
    :param type: The coefficient type being optimized.
    :return: The optimized version of the coefficient.
    """
    m = data.shape[0]

    error = 0
    if type == TYPE_INTERCEPT:
        for i in range(0, m):
            error += (predictYValue(b0, b1, data.iloc[i, xAxis]) - data.iloc[i, yAxis])

    elif type == TYPE_SLOPE:
        for i in range(0, m):
            error += ((predictYValue(b0, b1, data.iloc[i, xAxis]) - data.iloc[i, yAxis]) * data.iloc[i, xAxis])

    error = error /  m
    return error


# Change these values based on the table column names
xLabelPlaceholder = "Caratage"
yLabelPlaceholder = "Price"

# Create a plot and scatter figure
fig, axs = plt.subplots(figsize=(6,6))
axs.set_xlabel = xLabelPlaceholder
axs.set_ylabel = yLabelPlaceholder
axs.grid()

# Iterate between epoch while animating them
predictedYList = []
line, = axs.plot(data[xLabelPlaceholder], [None] * data.shape[0])
scatter = axs.scatter(data[xLabelPlaceholder], data[yLabelPlaceholder])


# for i in range(2000):
#     b0Error = calculateError(b0, b1, alpha, data, TYPE_INTERCEPT)
#     b1Error = calculateError(b0, b1, alpha, data, TYPE_SLOPE)
#     newB0 = b0 - alpha * b0Error
#     newB1 = b1 - alpha * b1Error
#
#     b0 = newB0
#     b1 = newB1
#
# predictedYList = []
# for i in range(0, data.shape[0]):
#     predictedYList.append(predictYValue(b0, b1, data.iloc[i, xAxis]))
#
# # Change the line data to show difference
# line.set_data(data["Caratage"], predictedYList)

k = 0
def animate(frame):
    global b0, b1, alpha, k
    b0Error = calculateError(b0, b1, alpha, data, TYPE_INTERCEPT)
    b1Error = calculateError(b0, b1, alpha, data, TYPE_SLOPE)
    newB0 = b0 - alpha * b0Error
    newB1 = b1 - alpha * b1Error

    b0 = newB0
    b1 = newB1

    # Add the result into the list
    predictedYList = []
    for i in range(0, data.shape[0]):
        predictedYList.append(predictYValue(b0, b1, data.iloc[i, xAxis]))

    # Change the line data to show difference
    line.set_data(data[xLabelPlaceholder], predictedYList)

    print("Cost: = " + str((b0Error, b1Error)))
    k += 1
    if (k % 5 == 0): print("Counter = " + str(k))

    return line,


anim = FuncAnimation(fig, animate, frames=12, interval=1, blit=True)

plt.show()
