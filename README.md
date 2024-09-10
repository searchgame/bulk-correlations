# 💡 Bulk correlations

A simple python app to quickly uncover potential relationships in a CSV dataset by getting an overview of correlation coefficients between several pairs of metrics. Made with [Streamlit](https://streamlit.io/).

[https://bulk-correlations.streamlit.app/](https://bulk-correlations.streamlit.app/)  

## Usage:

1) Upload a CSV file from the left sidebar.

- Except for the first column, all columns must contain numeric values.

- Make sure that your CSV file is using comma as separator (not semicolon).

- Make sure that the column names of your CSV file doesn't contain special characters such as parentheses or quotes (white spaces, hyphens and underscores are okay).

The format expected is:
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

2) The correlation matrix automatically appears under "Results:"

3) Once the correlation matrix is displayed, a dropdown list containing all the metrics pairs will appear. The list is sorted from most correlating (positively or negatively) to least correlating. When selecting a metrics pair, a scatter plot will appear below showing the actual distribution of the data points.

## How to read the chart:

![alt text](https://github.com/searchgame/bulk-correlations/blob/main/example-bulk-correlations.png?raw=true)

Coming soon!
