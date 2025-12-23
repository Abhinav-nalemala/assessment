import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
from scipy.stats import linregress

def draw_plot():
    # Read data from file
    df = pd.read_csv('epa-sea-level.csv')

    # Create scatter plot
    plt.figure(figsize=(10, 6))
    plt.scatter(df['Year'], df['CSIRO Adjusted Sea Level'])

    # Create first line of best fit (1880–2050)
    res = linregress(df['Year'], df['CSIRO Adjusted Sea Level'])
    years = np.arange(1880, 2051)
    plt.plot(years, res.intercept + res.slope * years, 'r')

    # Create second line of best fit (2000–2050)
    df_2000 = df[df['Year'] >= 2000]
    res_2000 = linregress(df_2000['Year'], df_2000['CSIRO Adjusted Sea Level'])
    years_2000 = np.arange(2000, 2051)
    plt.plot(years_2000, res_2000.intercept + res_2000.slope * years_2000, 'green')

    # Add labels and title
    plt.xlabel('Year')
    plt.ylabel('Sea Level (inches)')
    plt.title('Rise in Sea Level')

    # Save plot and return data for testing (DO NOT MODIFY)
    plt.savefig('sea_level_plot.png')
    return plt.gca()
