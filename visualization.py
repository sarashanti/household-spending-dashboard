import dash
import dash_bootstrap_components as dbc
import plotly.express as px
import pandas as pd
import time

from dash import ctx, dcc, html, Input, Output, State
from jupyter_dash import JupyterDash

df = pd.read_excel('lifetime_spending.xlsx')
df.drop(['Unnamed: 0', 'MonthYear', 'Date', 'ZAP', 'Note'], axis=1, inplace=True)
df.tail()

#initialize dash app
app = JupyterDash(__name__, external_stylesheets=[dbc.themes.BOOTSTRAP])

#assigning colors to category and parent category
color_map_pc = {
     'Bills & Utilities': '#E48F72',
     'Education': '#FC6955',
     'Entertainment': '#6A76FC',
     'Fees & Charges': '#FED4C4',
     'Food': '#86CE00',
     'Gifts & Donations': '#BC7196',
     'Health & Fitness': '#F6F926',
     'Household': '#FF9616',
     'Income': '#479B55',
     'Loan': '#EEA6FB',
     'Parents': '#DC587D',
     'Saving & Investment': '#D626FF',
     'Savings': '#6E899C',
     'Shopping': '#00B5F7',
     'Transportation': '#E3EE9E',
     'Travel': '#C9FBE5'
}

color_map_c = {
        'Electricity Bill': '#E48F72',
        'Gas Bill': '#E48F72',
        'Internet Bill': '#E48F72',
        'Laundry': '#E48F72',
        'Security': '#E48F72',
        'Phone Bill': '#E48F72',
        'Rentals': '#E48F72',
        'Trash Bill': '#E48F72',
        'Water Bill': '#E48F72',
        'Insurances': '#E48F72',
        'Other Utility Bills': '#E48F72',
        'Course': '#FC6955',
        'Books': '#FC6955',
        'Online Course': '#FC6955',
        'Education': '#FC6955',
        'Working Space' : '#FC6955',
        'Entry Tickets': '#6A76FC',
        'Games': '#6A76FC',
        'Movies': '#6A76FC',
        'Subscription': '#6A76FC',
        'Streaming Service': '#6A76FC',
        'Entertainment': '#6A76FC',
        'Playing': '#6A76FC',
        'Concert': '#6A76FC',
        'Administration': '#FF9616',
        'Cleaning Products': '#FF9616',
        'Home Essentials': '#FF9616',
        'Kitchen': '#FF9616',
        'Pets': '#FF9616',
        'Repairing': '#FF9616',
        'Home Services': '#FF9616',
        'Fees & Charges': '#FED4C4',
        'OVO': '#FED4C4',
        'GoPay': '#FED4C4',
        'Bank': '#FED4C4',
        'GoFood': '#86CE00',
        'Grab Food': '#86CE00',
        'Groceries': '#86CE00',
        'Food': '#86CE00',
        'Jajan': '#86CE00',
        'Jamuan': '#86CE00',
        'Males Masak': '#86CE00',
        'Pre Order': '#86CE00',
        'Restaurants': '#86CE00',
        'Café': '#86CE00',
        'Makan Berat': '#86CE00',
        'Angpao': '#BC7196',
        'Charity': '#BC7196',
        'Friends & Lover': '#BC7196',
        'Funeral': '#BC7196',
        'Marriage': '#BC7196',
        'Zakat & Kurban': '#BC7196',
        'Gifts & Donations': '#BC7196',
        'Doctor': '#F6F926',
        'Fitness': '#F6F926',
        'Lab': '#F6F926',
        'Medical Check-up': '#F6F926',
        'Personal Care': '#F6F926',
        'Pharmacy': '#F6F926',
        'Sports': '#F6F926',
        'Health & Fitness': '#F6F926',
        'Treatment': '#F6F926',
        'Parents': '#DC587D',
        'Accessories': '#00B5F7',
        'Children & Babies': '#00B5F7',
        'Electronics': '#00B5F7',
        'Makeup': '#00B5F7',
        'Personal Items': '#00B5F7',
        'Stationary': '#00B5F7',
        'Shopping': '#00B5F7',
        'Furniture': '#00B5F7',
        'Fashion': '#00B5F7',
        'Angkot': '#E3EE9E',
        'Bus': '#E3EE9E',
        'Gojek': '#E3EE9E',
        'Grab Bike': '#E3EE9E',
        'Ojek': '#E3EE9E',
        'Paket': '#E3EE9E',
        'Parking Fees': '#E3EE9E',
        'Petrol': '#E3EE9E',
        'Saving' : '#D626FF',
        'Investment' : '#D626FF',
        'Saving & Investment': '#D626FF',
        'Taxi': '#E3EE9E',
        'Tol': '#E3EE9E',
        'Train': '#E3EE9E',
        'TransJakarta': '#E3EE9E',
        'Travel Car': '#E3EE9E',
        'Vehicle Maintenance': '#E3EE9E',
        'Transportation': '#E3EE9E',
        'Airplane' : '#E3EE9E',
        'Hotel': '#C9FBE5',
        'Oleh - Oleh': '#C9FBE5',
        'Collect Savings': '#479B55',
        'Salary': '#479B55',
        'Gifts': '#479B55',
        'Selling': '#479B55',
        'Loan' : '#EEA6FB'
    }

  app.layout = dbc.Container([
    dcc.Store(id="app_state", data={"last_month": None, "last_year": None}),
    
  #dashboard title
    dbc.Row([
        dbc.Col(
            html.H1(
                'HOUSEHOLD EXPENSES',
                style={
                    'color': 'darkblue',
                    'fontSize': 40,
                    'textAlign': 'center',
                    'font-family': 'verdana'
                },
                className="my-4"
            ),
            width=12
        )
    ]),

    #filter bar
    dbc.Card(
        dbc.CardBody([
            dbc.Row([
                dbc.Col([
                    html.Label('Transaction Type', className="fw-bold mb-1 font-verdana"),
                    dcc.Checklist(
                        id='transaction_type',
                        options=[{"label": t, "value": t} for t in df['TransactionType'].unique()],
                        value=['Spending'],
                        inline=True,
                        style={'display': 'flex', 'flex-wrap': 'wrap', 'gap': '10px'}
                    ),
                ], md=2),

                dbc.Col([
                    html.Label('Year', className="fw-bold mb-1 font-verdana"),
                    dcc.Dropdown(
                        id='year',
                        options=[{"label": "All", "value": "all"}] +
                                [{"label": y, "value": y} for y in df['Year'].unique()],
                        value="all",
                        multi=True,
                    ),
                ], md=2),

                dbc.Col([
                    html.Label('Month', className="fw-bold mb-1 font-verdana"),
                    dcc.Dropdown(
                        id='month',
                        options=[{"label": "All", "value": "all"}] +
                                [{"label": m, "value": m} for m in df['MonthName'].unique()],
                        value="all",
                        multi=True,
                    ),
                ], md=2),

                dbc.Col([
                    html.Label('Account', className="fw-bold mb-1 font-verdana"),
                    dcc.Dropdown(
                        id='account',
                        options=[{"label": "All", "value": "all"}] +
                                [{"label": "Saras only", "value": "saras-only"}] +
                                [{"label": a, "value": a} for a in sorted(df['Account'].unique())],
                        value="all",
                        multi=True,
                    ),
                ], md=2),

                dbc.Col([
                    html.Label('Parent Category', className="fw-bold mb-1 font-verdana"),
                    dcc.Dropdown(
                        id='parent_category',
                        options=[{"label": "All Expenses", "value": "all"}] +
                                [{"label": "All Expenses (exclude Saving & Investments)", "value": "all-exclude"}] +
                                [{"label": p, "value": p} for p in sorted(df['ParentCategory'].unique())],
                        value="all-exclude",
                        multi=True,
                    ),
                ], md=4),
            ], className="gy-0 mb-4")
        ]), className="pt-1 pb-1"
    ),

    #trend graphs card
    dbc.Card(
        dbc.CardBody([
            dbc.Row([
                dbc.Col(
                    dcc.Graph(id="spending-trend1"),
                    md=4, className="mb-4 p-2 rounded-0 font-verdana"
                ),
                dbc.Col(
                    dcc.Graph(id="spending-trend2", clear_on_unhover=True),
                    md=8, className="mb-4 p-2 rounded-0 font-verdana"
                )
            ])
        ]),
        className="gy-0 mb-4"
    ),

    #tree map card
    dbc.Card(
        dbc.CardBody([
            dbc.Row([
                dbc.Col(
                    dcc.Graph(id="spending-tree1"),
                    md=12, className="mb-4 p-2 rounded-0 font-verdana"
                )
            ])
        ]),
        className="gy-0 mb-4"
    ),

    #bar and trendline card
    dbc.Card(
        dbc.CardBody([
            dbc.Row([
                dbc.Col(
                    dcc.Graph(id="spending-bar1"),
                    md=6, className="mb-4 p-2 rounded-0 font-verdana"
                ),
                dbc.Col(
                    dcc.Graph(id="spending-trend3"),
                    md=6, className="mb-4 p-2 rounded-0 font-verdana"
                )
            ])
        ])
    )
], fluid=True)

@app.callback(
    Output('spending-trend1','figure'),
    Output('spending-trend2','figure'),
    Input('transaction_type','value'),
    Input('year','value'),
    Input('month','value'),
    Input('account','value'),
    Input('parent_category','value')
    )

def update_graphs1(transaction_type, year, month, account, parent_category):
    year = df['Year'].unique() if 'all' in year else year
    month = df['MonthName'].unique() if 'all' in month else month

    if 'saras-only' in account:
        account = [ac for ac in df['Account'].unique() if ac in ('BCA - Kado','Cash Saras','Cold Money','E-money Saras','Jenius','Mandiri')]
    elif 'all' in account:
        account = list(df['Account'].unique())
    else:
        account

    if 'all-exclude' in parent_category:
        parent_category = [cat for cat in df['ParentCategory'].unique() if cat != 'Saving & Investment']
    elif 'all' in parent_category:
        parent_category = list(df['ParentCategory'].unique())
    else:
        parent_category
    
    filtered_df = df[
        (df['TransactionType'].isin(transaction_type)) &
        (df['Year'].isin(year if 'all' not in year else df['Year'].unique())) &
        (df['MonthName'].isin(month)) &
        (df['Account'].isin(account)) &
        (df['ParentCategory'].isin(parent_category)) 
        ]

    df_trend1 = filtered_df.groupby(['Year','Month'])['Amount'].sum().reset_index()
    df_trend1 = df_trend1.groupby(['Year'])['Amount'].median().reset_index()
    df_trend1['Lag_Value'] = df_trend1['Amount'].shift(1)
    df_trend1['Diff'] = round(((df_trend1['Amount']/df_trend1['Lag_Value'])-1)*100,1).fillna(0)

    #define line chart
    fig_trend1 = px.line(df_trend1
                         , x="Year"
                         , y="Amount"
                         , custom_data= ['Diff']
                         , title = "Average Monthly Expenses Year Over Year"
                         , markers=True)
    fig_trend1.update_traces(mode="markers+lines"
                             , hovertemplate="Rp %{y:,.0f} (%{customdata[0]:+.1f}%)<extra></extra>")
    fig_trend1.update_layout(hovermode="x unified"
                             , plot_bgcolor="rgba(0,0,0,0)"
                             , margin=dict(l=40, r=40, t=60, b=60)
                             , xaxis_title=None
                             , yaxis_title=None
                             , title_x=0.5
                             , font=dict(
                                        family="Verdana",   
                                        size=12,          
                                        color="black"))
    fig_trend1.update_xaxes(type="category"
                            , showline=True
                            , linewidth=1
                            , linecolor="black"
                            , mirror=False)
    fig_trend1.update_yaxes(showline=True, linewidth=1, linecolor="black", mirror=False)

    #format title based on parent_category selection
    if set(parent_category) == set(df['ParentCategory'].unique()):
        title_text = "Monthly Breakdown on All Expenses"
    elif set(parent_category) == set([cat for cat in df['ParentCategory'].unique() if cat != "Saving & Investment"]):
        title_text = "Monthly Breakdown on All Expenses (exclude Saving & Investment)"
    else:
        title_text = "Monthly Breakdown on " + ", ".join(parent_category)

    df_trend2 = filtered_df.groupby(['Year','Month','MonthName'])['Amount'].sum().reset_index()
    
    fig_trend2 = px.line(df_trend2, x="MonthName", y="Amount", color="Year", title= title_text, markers=True)
    fig_trend2.update_traces(mode="markers+lines", hovertemplate="Rp %{y:,.0f}")
    fig_trend2.update_layout(hovermode="x unified", 
                             plot_bgcolor="rgba(0,0,0,0)",
                             margin=dict(l=40, r=40, t=60, b=40),
                             xaxis_title=None,
                             yaxis_title=None,
                             title_x=0.5,
                             font=dict(
                                        family="Verdana",   
                                        size=12,          
                                        color="black"     
                                    )
                            )
    fig_trend2.update_xaxes(showline=True, linewidth=1, linecolor="black", mirror=False)
    fig_trend2.update_yaxes(showline=True, linewidth=1, linecolor="black", mirror=False)
    return fig_trend1, fig_trend2

@app.callback(
    Output('spending-tree1','figure'),
    Output('app_state','data'),
    # Output('spending-trend2','clickData'),
    Input('spending-trend2','clickData'),
    Input('spending-trend2','hoverData'),
    Input('transaction_type','value'),
    Input('year','value'),
    Input('month','value'),
    Input('account','value'),
    Input('parent_category','value'),
    State('app_state','data')
    )

def update_treemap(clickData, hoverData, transaction_type, year, month, account, parent_category,app_state):
    year_filter = df['Year'].unique() if 'all' in year else year
    month_filter = df['MonthName'].unique() if 'all' in month else month

    if app_state is None:
        app_state = {"last_month": None, "last_year": None}

    #restore last clicked state
    latest_month = app_state.get("last_month")
    latest_year = app_state.get("last_year")

    #override activeData - filtering year and month from hover and click
    activeData = clickData or hoverData
    if activeData:
        clicked_year = activeData['points'][0]['customdata'][0] if 'customdata' in activeData['points'][0] else None
        clicked_month = activeData['points'][0]['x']
        if clicked_year:
            if latest_year is None:
                year_filter=[clicked_year]
            elif latest_year is not None and clicked_year!=latest_year:
                year_filter=[clicked_year]
                latest_year = clicked_year
            elif latest_year is not None and clicked_year==latest_year:
                year_filter = df['Year'].unique() if 'all' in year else year
                latest_year = None
        if clicked_month:
            if latest_month is None:
                month_filter=[clicked_month]
            elif latest_month is not None and clicked_month!=latest_month:
                month_filter=[clicked_month]
                latest_month=clicked_month
            elif latest_month is not None and clicked_month==latest_month:
                month_filter = df['MonthName'].unique() if 'all' in month else month
                latest_month = None
    else:
        year_filter = df['Year'].unique() if 'all' in year else year
        month_filter = df['MonthName'].unique() if 'all' in month else month
        
    #filtering account
    if 'saras-only' in account:
        account = [ac for ac in df['Account'].unique() if ac in ('BCA - Kado','Cash Saras','Cold Money','E-Money Saras','Jenius','Mandiri')]
    elif 'all' in account:
        account = list(df['Account'].unique())
    else:
        account

    #filtering parent category
    if 'all-exclude' in parent_category:
        parent_category = [cat for cat in df['ParentCategory'].unique() if cat != 'Saving & Investment']
    elif 'all' in parent_category:
        parent_category = list(df['ParentCategory'].unique())
    else:
        parent_category

    #final filter
    filtered_df = df[
        (df['TransactionType'].isin(transaction_type)) &
        (df['Year'].isin(year_filter)) &
        (df['MonthName'].isin(month_filter)) &
        (df['Account'].isin(account)) &
        (df['ParentCategory'].isin(parent_category)) 
        ]
    
    #table aggregation
    df_tree1 = filtered_df.groupby(['ParentCategory'])['Amount'].sum().reset_index().sort_values(by='Amount', ascending=False)
    df_tree1["Percentage"] = df_tree1["Amount"] / df_tree1["Amount"].sum() * 100

    #define tree chart
    fig_tree1 = px.treemap(df_tree1, path=["ParentCategory"], values="Amount", title="Breakdown of Expenses on Parent Category", hover_data={"Amount": True, "Percentage": ":.1f"},custom_data=["Amount", "Percentage"],color="ParentCategory",color_discrete_map=color_map_pc)
    fig_tree1.update_traces(texttemplate="%{label}<br>%{customdata[1]:.1f}%<br>Rp %{value}", hovertemplate="%{label}<br>%{customdata[1]:.1f}%<br>Rp %{value}")
    fig_tree1.update_layout(hovermode="x unified", 
                            title_x=0.5, 
                            margin=dict(l=40, r=40, t=60, b=40),
                            font=dict(
                                      family="Verdana",   
                                      size=12,          
                                      color="black"     
                                    )
                            )

    app_state["last_month"] = latest_month
    app_state["last_year"] = latest_year
  
    return fig_tree1, app_state

@app.callback(
     Output('spending-bar1','figure'),
     Input('spending-trend2','clickData'),
     Input('spending-trend2','hoverData'),
     Input('spending-tree1','hoverData'),
     Input('transaction_type','value'),
     Input('year','value'),
     Input('month','value'),
     Input('account','value'),
     Input('parent_category','value')
    )

def update_graphs2(clickData, hoverData, tree_hover, transaction_type, year, month, account, parent_category):
    year_filter = df['Year'].unique() if 'all' in year else year
    month_filter = df['MonthName'].unique() if 'all' in month else month

    if 'saras-only' in account:
        account = [ac for ac in df['Account'].unique() if ac in ('BCA - Kado','Cash Saras','Cold Money','E-Money Saras','Jenius','Mandiri')]
    elif 'all' in account:
        account = list(df['Account'].unique())
    else:
        account

    if 'all-exclude' in parent_category:
        parent_category = [cat for cat in df['ParentCategory'].unique() if cat != 'Saving & Investment']
    elif 'all' in parent_category:
        parent_category = list(df['ParentCategory'].unique())
    else:
        parent_category

    #override activeData - filtering year and month from hover and click    
    activeData = clickData or hoverData
    if activeData:
        clicked_year = activeData['points'][0]['customdata'][0] if 'customdata' in activeData['points'][0] else None
        clicked_month = activeData['points'][0]['x']
        if clicked_year:
            year_filter = [clicked_year]
        if clicked_month:
            month_filter = [clicked_month]
    else:
        year_filter = year_filter
        month_filter = month_filter

    filtered_df = df[
        (df['TransactionType'].isin(transaction_type)) &
        (df['Year'].isin(year_filter)) &
        (df['MonthName'].isin(month_filter)) &
        (df['Account'].isin(account)) &
        (df['ParentCategory'].isin(parent_category)) &
        (df['Category'].notnull())
        ]

    #setting hover on treemap
    if tree_hover and 'points' in tree_hover:
        hovered_category = tree_hover['points'][0]['label']
    else:
        hovered_category = None

    if hovered_category:
        breakdown_df = filtered_df[filtered_df['ParentCategory'] == hovered_category]
    else:
        breakdown_df = filtered_df
    
    df_bar1 = breakdown_df.groupby(['Category'])['Amount'].sum().reset_index()
    df_bar1 = df_bar1.sort_values(by='Amount', ascending=False)

    fig_bar1 = px.bar(df_bar1
                      , x="Amount"
                      , y="Category"
                      , text = "Amount"
                      , title= f"Breakdown of Expenses for {hovered_category}" if hovered_category else "Breakdown Expenses for All Categories"
                      ,color="Category"
                      ,color_discrete_map=color_map_c)   
    fig_bar1.update_traces(hovertemplate="%{label}<br>Rp %{value:,.0f}<extra></extra>"
                           , texttemplate="Rp %{text:,.0f}"
                           , textposition="inside")
    fig_bar1.update_layout(title_x=0.5,
                           showlegend=False,
                           plot_bgcolor="rgba(0,0,0,0)",
                           margin=dict(l=40, r=40, t=60, b=40),
                           xaxis=dict(visible=False),
                           xaxis_title=None,
                           yaxis_title=None,
                           font=dict(
                                    family="Verdana",   
                                    size=12,          
                                    color="black"     
                                    )
                          )
    fig_bar1.update_xaxes(showline=True, linewidth=1, linecolor="black", mirror=False)
    fig_bar1.update_yaxes(showline=True, linewidth=1, linecolor="black", mirror=False)

    return fig_bar1

@app.callback(
     Output('spending-trend3','figure'),
     Input('spending-bar1','hoverData'),
     Input('transaction_type','value'),
     Input('year','value'),
     Input('month','value'),
     Input('account','value'),
     Input('parent_category','value')
    )

def update_graphs3(hoverData, transaction_type, year, month, account, parent_category):
    year = df['Year'].unique() if 'all' in year else year
    month = df['MonthName'].unique() if 'all' in month else month

    if 'saras-only' in account:
        account = [ac for ac in df['Account'].unique() if ac in ('BCA - Kado','Cash Saras','Cold Money','E-Money Saras','Jenius','Mandiri')]
    elif 'all' in account:
        account = list(df['Account'].unique())
    else:
        account

    if 'all-exclude' in parent_category:
        parent_category = [cat for cat in df['ParentCategory'].unique() if cat != 'Saving & Investment']
    elif 'all' in parent_category:
        parent_category = list(df['ParentCategory'].unique())
    else:
        parent_category
    
    filtered_df = df[
        (df['TransactionType'].isin(transaction_type)) &
        (df['Year'].isin(year)) &
        (df['MonthName'].isin(month)) &
        (df['Account'].isin(account)) &
        (df['ParentCategory'].isin(parent_category)) &
        (df['Category'].notnull())
        ]

    hovered_category = None
    if hoverData and 'points' in hoverData:
        hovered_category = hoverData['points'][0]['label']

    if hovered_category:
        breakdown_df = filtered_df[(filtered_df['ParentCategory']==hovered_category)|(filtered_df['Category'] == hovered_category)]
    else:
        breakdown_df = filtered_df

    df_trend3 = breakdown_df.groupby(['Year','Category'])['Amount'].sum().reset_index()
    df_trend3['Lag_Value'] = df_trend3['Amount'].shift(1)
    df_trend3['Diff'] = round(((df_trend3['Amount']/df_trend3['Lag_Value'])-1)*100,1).fillna(0)
    
    fig_trend3 = px.line(df_trend3
                         , x="Year"
                         , y="Amount"
                         , custom_data = ['Diff']
                         , color="Category"
                         , color_discrete_map = color_map_c
                         , title = f"Year-On-Year Expenses on {hovered_category}" if hovered_category else "Year-On-Year Expenses on All Categories"
                         , markers=True
                        )
    fig_trend3.update_traces(mode="markers+lines"
                             , hovertemplate="Rp %{y:,.0f} (%{customdata[0]:+.1f}%)<extra></extra>")
    fig_trend3.update_layout(hovermode="x unified"
                             , plot_bgcolor="rgba(0,0,0,0)"
                             , margin=dict(l=40, r=40, t=60, b=40)
                             , showlegend=False
                             , xaxis_title=None
                             , yaxis_title=None
                             , title_x=0.5
                             , font=dict(
                                        family="Verdana",   
                                        size=12,          
                                        color="black"     
                                    )
                            )
    fig_trend3.update_xaxes(type="category",showline=True, linewidth=1, linecolor="black", mirror=False)                           
    fig_trend3.update_yaxes(showline=True, linewidth=1, linecolor="black", mirror=False)
        
    return fig_trend3


server_url = app.run_server(mode="external",debug=True,port=8050)
