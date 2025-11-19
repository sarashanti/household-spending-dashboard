
## Household Spending Dashboard

### 1. Overview
Household Spending Dashboard is a visualization of personal expenses that utilizes extracted data from Money Lover. Money Lover is an app that allows you to track daily spending and its data can be exported in `.csv` format. The raw data is further processed using Python and Plotly Dash to create a Tableau-like dashboard.

##### Why Did I Make This Dashboard?
I have a yearly household finance review with my husband. The goal is to identify where our money goes, compare expenses with the previous year, and evaluate cost-saving opportunities. Many financial questions cross my mind, such as: Did I shop too much? Did my reluctance to cook significantly impact our food expenses? Did we unconsciously pay for unnecessary subscriptions? How much money have we saved since switching to a newer vehicle? Tracking changes by category allows us to answer these questions seamlessly and spend more wisely.

### 2. Project Demo
![spending_dashboard_demo](https://github.com/user-attachments/assets/c15535f6-9999-444c-8933-749012410aca)

### 3. Sample Cleaned Data
[dummy_lifetime_spending.xlsx](https://github.com/user-attachments/files/22680074/dummy_lifetime_spending.xlsx)

### 4. Highlights per Files

##### `cleaning-moneylover-data.py`
1. The definition of one month is set from the 25th to the 24th of the next month. This is adjusted according to our payday, which falls on the 25th of every month.
2. I assigned labels for the Parent Category since this hierarchical labeling only available in the Money Lover app. It is not included in the exported `.csv` data.

##### `visualization.py`
I created dependencies among these graphs:
1. The treemap depends on the Monthly Breakdown line chart.
2. The barchart depends on the treemap selection.
3. The Year-on-Year Expenses linechart depends on the barchart selection. 

### 5. User Guide
1. Extract `.csv` data from Money Lover
2. Run `cleaning-money-lover-data.py` 
3. Run `visualization.py` 
4. Click `http://127.0.0.1:8050/` to view dashboard in new tab

### 6. Need To Be Done
- [ ] Create unclick/deselect feature in Monthly Breakdown linechart. Still looking for a workaround that enables the unclick feature in `clickData`
- [ ] Automate data extraction from MoneyLover app to python script
