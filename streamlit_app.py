import streamlit as st
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import numpy as np

# Set a title
st.title('Results:')

# Set a sidebar for user input
st.sidebar.title("Settings")

# Upload the CSV file
file_upload = st.sidebar.file_uploader("Upload CSV", type=['csv'])

# Check if a file is uploaded
if file_upload is not None:

    # Load the CSV file
    data = pd.read_csv(file_upload, header=None)

    # Set the first row as column names
    data.columns = data.iloc[0].values
    data = data.iloc[1:]

    # Remove first column
    data = data.iloc[:, 1:]

    # Convert data to numeric
    data = data.apply(pd.to_numeric, errors='coerce')

    # Compute correlation matrix
    corr = data.corr()

    # Generate a mask for the upper triangle
    mask = np.triu(np.ones_like(corr, dtype=bool))

    # Set up the matplotlib figure
    fig, ax = plt.subplots(figsize=(11, 9))

    # Draw the heatmap with the mask
    sns.heatmap(corr, mask=mask, annot=True, fmt=".2f", cmap='coolwarm', vmin=-1, vmax=1, ax=ax)
    plt.title('Correlation of your data')

    # Show the plot in Streamlit
    st.pyplot(fig)

    # Create a list of metric pairs with their correlation coefficients
    metric_pairs = []
    for i in range(len(data.columns)):
        for j in range(i+1, len(data.columns)):
            pair = (data.columns[i], data.columns[j])
            corr_value = corr.iloc[i, j]
            metric_pairs.append((pair, corr_value))

    # Sort the metric pairs based on the absolute value of correlation
    sorted_pairs = sorted(metric_pairs, key=lambda x: abs(x[1]), reverse=True)

    # Create a list of formatted strings for the dropdown
    dropdown_options = [f"{pair[0]} vs {pair[1]} (corr: {corr:.2f})" for pair, corr in sorted_pairs]

    # Add a dropdown to select a metric pair
    selected_pair_str = st.selectbox("Select a metric pair", dropdown_options)

    # Extract the selected pair from the string
    selected_pair = tuple(selected_pair_str.split(' (')[0].split(' vs '))

    # Create a scatter plot with regression line for the selected metric pair
    x = data[selected_pair[0]]
    y = data[selected_pair[1]]
    fig, ax = plt.subplots(figsize=(10, 8))
    sns.regplot(x=x, y=y, ax=ax, scatter_kws={'alpha':0.5})
    ax.set_xlabel(selected_pair[0])
    ax.set_ylabel(selected_pair[1])
    ax.set_title(f"Scatter plot with regression line: {selected_pair[0]} vs {selected_pair[1]}")
    st.pyplot(fig)

else:
    st.sidebar.text('Please upload a CSV file.')
