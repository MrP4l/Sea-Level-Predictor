import pandas as pd
import matplotlib.pyplot as plt
from scipy.stats import linregress


def draw_plot():
    # Read data from file
    df = pd.read_csv('epa-sea-level.csv')

    # Create scatter plot
    x = df['Year']
    y = df['CSIRO Adjusted Sea Level']
    fig, ax = plt.subplots(figsize=(16, 9))
    plt.scatter(x, y)

    # Create first line of best fit
    res = linregress(x, y)
    xp = pd.Series([i for i in range(1880, 2051)])
    yp = res.intercept + res.slope*xp
    plt.plot(xp, yp, 'r')


    #res = linregress(x, y)
    #plt.plot(x, res.intercept + res.slope * x, 'g')

    #x2 = list(range(1880, 2051))
    #y2 = []
    #for year in x2:
    #    y2.append(res.intercept + res.slope * year)
    #plt.plot(x2, y2, 'r', label='Bests Fit Line 1')

    # Create second line of best fit
    df2 = df.loc[df['Year'] >= 2000]
    x2 = df2['Year']
    y2 = df2['CSIRO Adjusted Sea Level']
    res2 = linregress(x2, y2)
    xp2 = pd.Series([i for i in range(2000, 2051)])
    yp2 = res2.intercept + res2.slope*xp2
    plt.plot(xp2, yp2, 'g')

    #df2 = df.loc[df['Year'] >= 2000]
    #x3 = df2['Year']
    #y3 = df2['CSIRO Adjusted Sea Level']
    #plt.scatter(x, y)

    #res2 = linregress(x3, y3)
    #plt.plot(x3, res2.intercept + res2.slope * x3, 'r')

    #x3 = list(range(2000, 2051))
    #y3 = []
    #for year in x3:
    #    y3.append(res2.intercept + res2.slope * year)
    #plt.plot(x3, y3, 'r', label='Bests Fit Line 2')
   


    # Add labels and title
    plt.xlabel('Year')
    plt.ylabel('Sea Level (inches)')
    plt.title('Rise in Sea Level')

    # Save plot and return data for testing (DO NOT MODIFY)
    plt.savefig('sea_level_plot.png')
    return plt.gca()
