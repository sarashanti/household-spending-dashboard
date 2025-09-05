import pandas as pd
import numpy as np
import glob
import calendar

files_prev = glob.glob("/Users/xxx/*.xlsx")
files_cur = glob.glob("/Users/xxx/*.csv")

whole = pd.DataFrame()
all = []

for x in files_prev:
    prev = pd.read_excel(x)
    all.append(prev)

for c in files_cur:
    bsc = pd.read_csv(c)
    print(bsc)
    bsc = bsc[['Date','Account','Category','Note','Amount']]
    bsc = bsc[(bsc.Category != 'Other Expense')&(bsc.Category != 'Other Income')&(bsc.Category != 'Withdrawal')&(bsc.Category != 'Outgoing transfer')&(bsc.Category != 'Incoming transfer')]
    
    def set_value(row_number, assigned_value):
        return assigned_value[row_number]

    sc={
        'Electricity Bill': 'Bills & Utilities',
        'Gas Bill': 'Bills & Utilities',
        'Internet Bill': 'Bills & Utilities',
        'Laundry': 'Bills & Utilities',
        'Security': 'Bills & Utilities',
        'Phone Bill': 'Bills & Utilities',
        'Rentals': 'Bills & Utilities',
        'Trash Bill': 'Bills & Utilities',
        'Water Bill': 'Bills & Utilities',
        'Insurances': 'Bills & Utilities',
        'Other Utility Bills': 'Bills & Utilities',
        'Books': 'Education',
        'Online Course': 'Education',
        'Education': 'Education',
        'Working Space' : 'Education',
        'Entry Tickets': 'Entertainment',
        'Games': 'Entertainment',
        'Movies': 'Entertainment',
        'Subscription': 'Entertainment',
        'Streaming Service': 'Entertainment',
        'Entertainment': 'Entertainment',
        'Playing': 'Entertainment',
        'Administration': 'Household',
        'Cleaning Products': 'Household',
        'Home Essentials': 'Household',
        'Kitchen': 'Household',
        'Pets': 'Household',
        'Repairing': 'Household',
        'Home Services': 'Household',
        'Fees & Charges': 'Fees & Charges',
        'Cafe': 'Food',
        'GoFood': 'Food',
        'Grab Food': 'Food',
        'Groceries': 'Food',
        'Food': 'Food',
        'Jajan': 'Food',
        'Jamuan': 'Food',
        'Males Masak': 'Food',
        'Pre Order': 'Food',
        'Restaurants': 'Food',
        'Café': 'Food',
        'Makan Berat': 'Food',
        'Angpao': 'Gifts & Donations',
        'Charity': 'Gifts & Donations',
        'Friends & Lover': 'Gifts & Donations',
        'Funeral': 'Gifts & Donations',
        'Marriage': 'Gifts & Donations',
        'Zakat & Kurban': 'Gifts & Donations',
        'Gifts & Donations': 'Gifts & Donations',
        'Doctor': 'Health & Fitness',
        'Fitness': 'Health & Fitness',
        'Lab': 'Health & Fitness',
        'Medical Check-up': 'Health & Fitness',
        'Personal Care': 'Health & Fitness',
        'Pharmacy': 'Health & Fitness',
        'Sports': 'Health & Fitness',
        'Health & Fitness': 'Health & Fitness',
        'Treatment': 'Health & Fitness',
        'Electricity Bill - PTB': 'Parents',
        'First Media': 'Parents',
        'Ibu': 'Parents',
        'Phone Bill - PTB': 'Parents',
        'Parents': 'Parents',
        'Accessories': 'Shopping',
        'Children & Babies': 'Shopping',
        'Electronics': 'Shopping',
        'Makeup': 'Shopping',
        'Personal Items': 'Shopping',
        'Stationary': 'Shopping',
        'Shopping': 'Shopping',
        'Angkot': 'Transportation',
        'Bus': 'Transportation',
        'Gojek': 'Transportation',
        'Grab Bike': 'Transportation',
        'Ojek': 'Transportation',
        'Paket': 'Transportation',
        'Parking Fees': 'Transportation',
        'Petrol': 'Transportation',
        'Saving' : 'Saving & Investment',
        'Investment' : 'Saving & Investment',
        'Saving & Investment': 'Saving & Investment',
        'Taxi': 'Transportation',
        'Tol': 'Transportation',
        'Train': 'Transportation',
        'TransJakarta': 'Transportation',
        'Travel Car': 'Transportation',
        'Vehicle Maintenance': 'Transportation',
        'Transportation': 'Transportation',
        'Hotel': 'Travel',
        'Oleh - Oleh': 'Travel',
        'Collect Savings': 'Income',
        'Salary': 'Income',
        'Gifts': 'Income',
        'Selling': 'Income',
        'Loan' : 'Debt & Loan',
        'Airplane' : 'Transportation',
        'Furniture': 'Shopping',
        'Fashion': 'Shopping',
        'Concert': 'Entertainment',
        'OVO': 'Fees & Charges',
        'GoPay': 'Fees & Charges',
        'Bank': 'Fees & Charges'
    }
    
    sc_2 = {
        'Bills & Utilities': 'Living',
        'Education': 'Living',
        'Entertainment': 'Playing',
        'Fees & Charges': 'Living',
        'Food': 'Living',
        'Gifts & Donations': 'Giving',
        'Health & Fitness': 'Living',
        'Household': 'Living',
        'Parents': 'Giving',
        'Shopping': 'Playing',
        'Transportation': 'Living',
        'Travel': 'Playing',
        'Saving & Investment': 'Saving',
        'Income': 'Income',
        'Debt & Loan' : 'Debt & Loan'
    }
    
    bsc['ParentCategory'] = bsc['Category'].apply(set_value,args=(sc,))
    bsc['ZAP']            = bsc['ParentCategory'].apply(set_value,args=(sc_2,))
    all.append(bsc)

for df in all:
    df['Date'] = pd.to_datetime(df['Date'])
    df['Amount'] = df['Amount'].abs()
    df['TransactionType'] = np.select([df['Category'] == 'Salary',
                                        df['Category'] == 'Gifts',
                                        df['Category'] == 'Collect Savings',
                                        df['Category'] == 'Selling'
                                       ],
                                       ['Income',
                                        'Income',
                                        'Income',
                                        'Income'],
                                       ['Spending'])
    df['MonthYear'] = (df['Date']-pd.DateOffset(days=24)).dt.to_period('M')+1 
    df['Month'] = df['MonthYear'].dt.month
    df['Year'] = df['MonthYear'].dt.year
    df['Note'] = df['Note'].replace([r'Admin\s',
                                     r'Admin\sbank\s',
                                     r'Admin\stopup\s',
                                     r'Admin\stop\sup\s',
                                     r'Admin\starik\stunai\s',
                                     r'Topup\s',
                                     r'topup\s',
                                     r'top\sup\s'],'',regex=True)
    df['Note'] = df['Note'].replace([r'Go\sPay',
                                     r'Gopay',
                                     r'gojek',
                                     r'gopay'],'GoPay',regex=True)
    df['Note'] = df['Note'].replace([r'Ovo',
                                     r'ovo'],'OVO',regex=True)
    df['Note'] = df['Note'].replace([r'bank\smandiri',
                                     r'Bank\smandiri'],'Mandiri',regex=True)

whole = pd.concat(all,ignore_index=True,axis=0).sort_values(['Year','Date'], ascending=[True,True]).reset_index(drop=True)
whole['MonthName'] = whole['Month'].map(lambda x: calendar.month_name[x])
whole = whole[['Year','Month','MonthName','MonthYear','Date','Account','TransactionType','ZAP','ParentCategory','Category','Note','Amount']]

whole.to_csv("/Users/xxx/lifetime_spending.csv")
whole.to_excel("/Users/xxx/lifetime_spending.xlsx")
