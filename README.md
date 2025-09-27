## Household Spending Dashboard

### Overview
Household Spending Dashboard is a visualization of personal expenses that utilizes extracted data from Money Lover. Money Lover is an app that allows you to track daily spending and its data can be exported in `.csv` format. The raw data is further processed using Python and Plotly Dash to create a Tableau-like dashboard.

#### Why Did I Make This Dashboard?
I have a yearly household finance review with my husband. The goal is to identify where our money goes, compare expenses with the previous year, and evaluate cost-saving opportunities. For example, did I shop too much? Did my reluctance to cook significantly impact our food expenses? Did we unconsciously pay for unnecessary subscriptions? How much money have we saved since switching to a newer vehicle? Tracking changes by category allows us to spend more wisely.

### Project Demo

### User Guide
1. Extract `.csv` data from Money Lover
2. Run `cleaning-money-lover-data.py` 
3. Run `visualization.py` 
4. Click `http://127.0.0.1:8050/` to view dashboard in new tab

### Highlights per Files

#### `cleaning-moneylover-data.py`
1. The definition of one month is set from the 25th to the 24th of the next month. This is adjusted according to my payday, which falls on the 25th of every month.
2. I assigned labels for the Parent Category since this hierarchical labeling exists only in the Money Lover app but is not included in the exported `.csv` data.
#### `visualization.py`

### Need To Be Done
- [ ] Create unclick/deselect feature in Monthly Breakdown linechart
