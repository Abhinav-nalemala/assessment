import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import numpy as np


def draw_cat_plot():
    df = pd.read_csv("medical_examination.csv")

    # Add 'overweight' column
    df['overweight'] = None

    # Normalize data by making 0 always good and 1 always bad
    df['cholesterol'] = None
    df['gluc'] = None

    # Draw Categorical Plot
    df_cat = None

    # Create catplot
    fig = None

    # Do not modify the next two lines
    fig.savefig('catplot.png')
    return fig


def draw_heat_map():
    df = pd.read_csv("medical_examination.csv")

    # Clean the data
    df_heat = None

    # Calculate the correlation matrix
    corr = None

    # Generate a mask for the upper triangle
    mask = None

    # Set up the matplotlib figure
    fig, ax = None

    # Draw the heatmap
    sns.heatmap(corr, mask=mask, annot=True, fmt=".1f", center=0)
    fig.savefig('heatmap.png')
    return fig
