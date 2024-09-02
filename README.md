# 💡 Bulk correlations

A simple python app to quickly uncover potential relationships in a CSV dataset by getting an overview of correlation coefficients between several pairs of metrics. Made with [Streamlit](https://streamlit.io/).

[https://bulk-correlations.streamlit.app/](https://bulk-correlations.streamlit.app/)  

## Usage:

1) Uploade a CSV file from the left sidebar. The format expected is: 
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


## How to read the chart:

![alt text](https://github.com/searchgame/bulk-correlations/blob/main/example-bulk-correlations.png?raw=true)

Coming soon!
