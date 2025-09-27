## Household Spending Dashboard

### Overview
Household Spending Dashboard is a visualization of personal expenses that utilizes extracted data from Money Lover. Money Lover is an app that allows you to track daily spending and its data can be exported in `.csv` format. The raw data is further processed using Python and Plotly Dash to create a Tableau-like dashboard.

##### Why Did I Make This Dashboard?
I have a yearly household finance review with my husband. The goal is to identify where our money goes, compare expenses with the previous year, and evaluate cost-saving opportunities. Many financial questions cross my mind, such as: Did I shop too much? Did my reluctance to cook significantly impact our food expenses? Did we unconsciously pay for unnecessary subscriptions? How much money have we saved since switching to a newer vehicle? Tracking changes by category allows us to answer these questions seamlessly and spend more wisely.

### Project Demo

### User Guide
1. Extract `.csv` data from Money Lover
2. Run `cleaning-money-lover-data.py` 
3. Run `visualization.py` 
4. Click `http://127.0.0.1:8050/` to view dashboard in new tab

### Sample Cleaned Data
| Year | Month | MonthName  | MonthYear | Date       | Account          | TransactionType | ZAP     | ParentCategory    | Category       | Note              | Amount |
|------|-------|------------|-----------|------------|------------------|-----------------|---------|-------------------|----------------|-------------------|--------|
| 2022 | 2     | February   | 2022-02   | 2022-02-14 | Cash Saras       | Spending        | Living  | Food              | Restaurant     | Valentine dinner  | 120000 |
| 2023 | 5     | May        | 2023-05   | 2023-05-08 | Jenius           | Spending        | Playing | Entertainment     | Subscription   | Spotify Premium   | 60000  |
| 2024 | 7     | July       | 2024-07   | 2024-07-21 | E-money          | Spending        | Living  | Transportation    | Train          | Office commute    | 15000  |
| 2025 | 1     | January    | 2025-01   | 2025-01-10 | Cash Operasional | Spending        | Living  | Bills & Utilities | Electricity    | PLN monthly bill  | 350000 |
| 2025 | 3     | March      | 2025-03   | 2025-03-19 | Cash Operasional | Spending        | Living  | Food              | Groceries      | Rice grain        | 75000  |


### Highlights per Files

##### `cleaning-moneylover-data.py`
1. The definition of one month is set from the 25th to the 24th of the next month. This is adjusted according to our payday, which falls on the 25th of every month.
2. I assigned labels for the Parent Category since this hierarchical labeling exists only in the Money Lover app but is not included in the exported `.csv` data.

##### `visualization.py`
I created dependencies among the graphs:
1. The treemap depends on the Monthly Breakdown line chart.
2. The barchart depends on the treemap selection.
3. The Year-on-Year Expenses linechart depends on the barchart selection. 

### Need To Be Done
- [ ] Create unclick/deselect feature in Monthly Breakdown linechart. Still looking for a workaround that enables the unclick feature in `clickData`
