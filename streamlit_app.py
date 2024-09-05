import streamlit as st
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import numpy as np

"""
# 💡 Bulk correlations 

Quickly uncover potential relationships in a CSV dataset by getting an overview of correlation coefficients between several pairs of metrics.

See the code and how to interpret the chart [on the Github repo](https://github.com/searchgame/bulk-correlations). Made by [Victor Gras](https://victorgras.com).

---
## Usage:

1) Upload a CSV file from the left sidebar. Except for the first column, all columns must contain numeric values. The format expected is: 
```
item,metric_1,metric_2,metric_3,etc
```
For example, for a GA4 export:
```
Address,Word Count,GA4 Sessions,GA4 Views,GA4 Engaged sessions,GA4 Bounce rate,Performance Score,First Contentful Paint Time (ms),Speed Index Time (ms),Largest Contentful Paint Time (ms),Time to Interactive (ms),Total Blocking Time (ms),Cumulative Layout Shift,Image Count
https://www.example.com/article-1/,692,13,13,7,0.3,60,2294,3864.021,6255,6716,537,0.013,5
https://www.example.com/article-2/,114,5,5,1,0,61,2264,3316.94,8505,6850.5,418.5,0.059,6
https://www.example.com/article-3/,1780,20,21,11,0.27,52,2704,3881.909,9030,7943,712,0.001,8
...
```

2) The chart automatically appears under "Results:"

---

"""

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

    # Create a scatter plot for the selected metric pair
    x = data[selected_pair[0]]
    y = data[selected_pair[1]]
    fig, ax = plt.subplots(figsize=(8, 6))
    ax.scatter(x, y)
    ax.set_xlabel(selected_pair[0])
    ax.set_ylabel(selected_pair[1])
    ax.set_title(f"Scatter plot of {selected_pair[0]} vs {selected_pair[1]}")
    st.pyplot(fig)

else:
    st.sidebar.text('Please upload a CSV file.')
