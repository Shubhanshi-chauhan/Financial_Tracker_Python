#!/usr/bin/env python
# coding: utf-8

# In[1]:


#required for manipulating data
import pandas as pd
import numpy as np


# In[2]:



#required for building the interactive dashboard
import panel as pn
pn.extension('tabulator')
import hvplot.pandas
import holoviews as hv
hv.extension('bokeh')


# In[3]:


# create dataset manually

data = [
    ['CARD_PAYMENT', 'Current', '2024-01-26 22:02:47', '2024-01-27 10:10:12', 'Tesco Stores 6601', -600, 0, 'GBP', 'COMPLETED', 521.07],
    ['CARD_PAYMENT', 'Current', '2024-01-26 16:13:50', '2024-01-27 11:50:32', 'Zettle_*donovan?s Bake', -250, 0, 'GBP', 'COMPLETED', 518.57],
    ['CARD_PAYMENT', 'Current', '2024-01-26 08:26:35', '2024-01-27 13:42:55', 'apple.com/bill', -399, 0, 'GBP', 'COMPLETED', 514.58],
    ['CARD_PAYMENT', 'Current', '2024-01-27 13:16:59', '2024-01-28 09:59:20', 'Tesco Stores 6601', -485, 0, 'GBP', 'COMPLETED', 509.73],
    ['CARD_PAYMENT', 'Current', '2024-01-27 10:43:22', '2024-01-28 11:48:36', 'Zettle_*the Good Eatin', -3300, 0, 'GBP', 'COMPLETED', 506.43],
    ['CARD_PAYMENT', 'Current', '2024-01-27 19:07:07', '2024-01-28 15:51:42', 'Toogoodtog Mzs3m03xcn9', -500, 0, 'GBP', 'COMPLETED', 501.43],
    ['CARD_PAYMENT', 'Current', '2024-01-28 01:14:16', '2024-01-29 08:55:25', 'Montys Bar', -210, 0, 'GBP', 'COMPLETED', 480.43],
    ['CARD_PAYMENT', 'Current', '2024-01-28 16:26:00', '2024-01-29 09:41:04', 'Amznmktplace', -899, 0, 'GBP', 'COMPLETED', 471.44],
    ['CARD_PAYMENT', 'Current', '2024-01-28 19:59:36', '2024-01-29 09:49:29', 'Tesco Stores 6601', -865, 0, 'GBP', 'COMPLETED', 462.79],
    ['CARD_PAYMENT', 'Current', '2024-01-27 22:59:58', '2024-01-29 10:08:56', 'Urban 40', -126, 0, 'GBP', 'COMPLETED', 450.19],
    ['CARD_PAYMENT', 'Current', '2024-01-27 22:06:03', '2024-01-29 10:08:56', 'Urban 40', -610, 0, 'GBP', 'COMPLETED', 444.09],
    ['CARD_PAYMENT', 'Current', '2024-01-29 02:39:46', '2024-01-29 10:55:55', 'Tfl Travel Charge', -425, 0, 'GBP', 'COMPLETED', 439.84],
    ['CARD_PAYMENT', 'Current', '2024-01-28 15:06:44', '2024-01-29 11:31:51', 'Sq *lavelle Coffee Limite', -320, 0, 'GBP', 'COMPLETED', 436.64],
    ['CARD_PAYMENT', 'Current', '2024-01-29 15:08:04', '2024-01-31 14:06:07', 'Tubebuddycom*', -243, 0.02, 'GBP', 'COMPLETED', 451.69],
    ['CARD_PAYMENT', 'Current', '2024-01-29 15:11:03', '2024-01-31 14:45:55', 'Sp Blomma Beauty', -30, 0, 'GBP', 'COMPLETED', 416.69],
    ['CARD_PAYMENT', 'Current', '2024-01-29 20:03:55', '2024-01-31 15:11:28', 'Uber* Trip', -1346, 0, 'GBP', 'COMPLETED', 403.23],
    ['CARD_PAYMENT', 'Current', '2024-01-29 14:31:09', '2024-01-31 17:29:48', 'Caravan', -2767, 0, 'GBP', 'COMPLETED', 375.56],
    ['CARD_PAYMENT', 'Current', '2024-01-30 01:57:58', '2024-01-31 17:41:29', 'Tfl Travel Charge', -425, 0, 'GBP', 'COMPLETED', 371.31],
    ['CARD_PAYMENT', 'Current', '2024-01-31 02:36:53', '2024-01-31 18:03:14', 'Tfl Travel Charge', -165, 0, 'GBP', 'COMPLETED', 369.66],
    ['CARD_PAYMENT', 'Current', '2024-01-29 19:13:59', '2024-01-31 18:46:41', 'Hart Shoreditch Hotel', -360, 0, 'GBP', 'COMPLETED', 366.06],
    ['CARD_PAYMENT', 'Current', '2024-01-30 19:03:58', '2024-01-31 19:00:20', 'Tesco Stores 6601', -425, 0, 'GBP', 'COMPLETED', 361.81],
    ['CARD_PAYMENT', 'Current', '2024-01-30 13:41:48', '2024-01-31 19:32:36', 'Lidl Gb London', -812, 0, 'GBP', 'COMPLETED', 343.69],
    ['CARD_PAYMENT', 'Current', '2024-01-30 11:55:40', '2024-01-31 19:55:25', 'E5 Bakehouse Canning T', -1236, 0, 'GBP', 'COMPLETED', 331.33],
    ['CARD_PAYMENT', 'Current', '30-02-2024 11:55:40', '02-02-2024 11:55:40', 'Amznmktplace', -1707, 0, 'GBP', 'COMPLETED', 555.43],
    ['CARD_PAYMENT', 'Current', '30-02-2024 11:55:40', '02-02-2024 11:55:40', 'Starbucks', -395, 0, 'GBP', 'COMPLETED', 551.48],
    ['CARD_PAYMENT', 'Current', '30-02-2024 11:55:40', '02-02-2024 11:55:40', 'Tfl Travel Charge', -260, 0, 'GBP', 'COMPLETED', 548.88],
    ['CARD_PAYMENT', 'Current', '30-02-2024 11:55:40', '02-02-2024 11:55:40', 'Millennium Mini Store', -50, 0, 'GBP', 'COMPLETED', 543.88],
    ['CARD_PAYMENT', 'Current', '30-02-2024 11:55:40', '02-02-2024 11:55:40', 'cm.com', -253, 0, 'GBP', 'COMPLETED', 290.88],
    ['CARD_PAYMENT', 'Current', '30-02-2024 11:55:40', '02-02-2024 11:55:40', 'Katsute100', -1225, 0, 'GBP', 'COMPLETED', 278.63],
    ['CARD_PAYMENT', 'Current', '30-02-2024 11:55:40', '02-02-2024 11:55:40', 'Ubr* Pending.uber.com', -1366, 0, 'GBP', 'COMPLETED', 264.97],
    ['CARD_PAYMENT', 'Current', '30-02-2024 11:55:40', '02-02-2024 11:55:40', 'Ubr* Pending.uber.com', -703, 0, 'GBP', 'COMPLETED', 257.94],
    ['CARD_PAYMENT', 'Current', '30-02-2024 11:55:40', '02-02-2024 11:55:40', 'Starbucks', -390, 0, 'GBP', 'COMPLETED', 254.04],
     ['CARD_PAYMENT', 'Current', '2024-03-26 22:02:47', '2024-03-27 10:10:12', 'Tesco Stores 6601', -635, 0, 'GBP', 'COMPLETED', 521.07],
    ['CARD_PAYMENT', 'Current', '2024-03-26 16:13:50', '2024-03-27 11:50:32', 'Zettle_*donovan?s Bake', -250, 0, 'GBP', 'COMPLETED', 518.57],
    ['CARD_PAYMENT', 'Current', '2024-03-26 08:26:35', '2024-03-27 13:42:55', 'apple.com/bill', -399, 0, 'GBP', 'COMPLETED', 514.58],
    ['CARD_PAYMENT', 'Current', '2024-03-27 13:16:59', '2024-03-28 09:59:20', 'Tesco Stores 6601', -485, 0, 'GBP', 'COMPLETED', 509.73],
    ['CARD_PAYMENT', 'Current', '2024-03-27 10:43:22', '2024-03-28 11:48:36', 'Zettle_*the Good Eatin', -330, 0, 'GBP', 'COMPLETED', 506.43],
    ['CARD_PAYMENT', 'Current', '2024-03-27 19:07:07', '2024-03-28 15:51:42', 'Toogoodtog Mzs3m03xcn9', -50, 0, 'GBP', 'COMPLETED', 501.43],
    ['CARD_PAYMENT', 'Current', '2024-03-28 01:14:16', '2024-03-29 08:55:25', 'Montys Bar', -210, 0, 'GBP', 'COMPLETED', 480.43],
    ['CARD_PAYMENT', 'Current', '2024-03-28 16:26:00', '2024-03-29 09:41:04', 'Amznmktplace', -899, 0, 'GBP', 'COMPLETED', 471.44],
    ['CARD_PAYMENT', 'Current', '2024-03-28 19:59:36', '2024-03-29 09:49:29', 'Tesco Stores 6601', -865, 0, 'GBP', 'COMPLETED', 462.79],
    ['CARD_PAYMENT', 'Current', '2024-03-27 22:59:58', '2024-03-29 10:08:56', 'Urban 40', -126, 0, 'GBP', 'COMPLETED', 450.19],
    ['CARD_PAYMENT', 'Current', '2024-03-27 22:06:03', '2024-03-29 10:08:56', 'Urban 40', -61, 0, 'GBP', 'COMPLETED', 444.09],
    ['CARD_PAYMENT', 'Current', '2024-03-29 02:39:46', '2024-03-29 10:55:55', 'Tfl Travel Charge', -425, 0, 'GBP', 'COMPLETED', 439.84],
    ['CARD_PAYMENT', 'Current', '2024-03-28 15:06:44', '2024-03-29 11:31:51', 'Sq *lavelle Coffee Limite', -320, 0, 'GBP', 'COMPLETED', 436.64],
    ['CARD_PAYMENT', 'Current', '2024-03-29 15:08:04', '2024-03-31 14:06:07', 'Tubebuddycom*', -243, 0.02, 'GBP', 'COMPLETED', 451.69],
    ['CARD_PAYMENT', 'Current', '2024-03-29 15:11:03', '2024-03-31 14:45:55', 'Sp Blomma Beauty', -35, 0, 'GBP', 'COMPLETED', 416.69],
    ['CARD_PAYMENT', 'Current', '2024-03-29 20:03:55', '2024-03-31 15:11:28', 'Uber* Trip', -136, 0, 'GBP', 'COMPLETED', 403.23],
    ['CARD_PAYMENT', 'Current', '2024-03-29 14:31:09', '2024-03-31 17:29:48', 'Caravan', -277, 0, 'GBP', 'COMPLETED', 375.56],
    ['CARD_PAYMENT', 'Current', '2024-03-30 01:57:58', '2024-03-31 17:41:29', 'Tfl Travel Charge', -425, 0, 'GBP', 'COMPLETED', 371.31],
    ['CARD_PAYMENT', 'Current', '2024-03-31 02:36:53', '2024-03-31 18:03:14', 'Tfl Travel Charge', -165, 0, 'GBP', 'COMPLETED', 369.66],
    ['CARD_PAYMENT', 'Current', '2024-03-29 19:13:59', '2024-03-31 18:46:41', 'Hart Shoreditch Hotel', -360, 0, 'GBP', 'COMPLETED', 366.06],
    ['CARD_PAYMENT', 'Current', '2024-03-30 19:03:58', '2024-03-31 19:00:20', 'Tesco Stores 6601', -425, 0, 'GBP', 'COMPLETED', 361.81],
    ['CARD_PAYMENT', 'Current', '2024-03-30 13:41:48', '2024-03-31 19:32:36', 'Lidl Gb London', -812, 0, 'GBP', 'COMPLETED', 343.69],
    ['CARD_PAYMENT', 'Current', '2024-03-30 11:55:40', '2024-03-31 19:55:25', 'E5 Bakehouse Canning T', -126, 0, 'GBP', 'COMPLETED', 331.33],
    
]

columns = ['Type', 'Product', 'Started Date', 'Completed Date', 'Description', 'Amount', 'Fee', 'Currency', 'State', 'Balance']

df = pd.DataFrame(data=data, columns=columns)


# In[4]:


df.head(60)


# In[5]:


#clean df

df = df[['Completed Date', 'Description', 'Amount']] #keep only desired columns
df['Description'] = df['Description'].map(str.lower) #lower case of descriptions

df = df.rename(columns={'Completed Date': 'Date'})   #rename columns
df['Category'] = 'unassigned'                        #add category column

df.head()


# In[ ]:


#define all categories

    # Self-Care
    # Fines
    # Lore So What
    # Coffee
    # Groceries
    # Shopping
    # Restaurants
    # Transport
    # Travel
    # Entertainment
    # Gifts
    # Services
    # Excluded


# In[10]:


#Assign transactions to the correct category

# Self-Care

df['Category'] = np.where(df['Description'].str.contains(
    'cash at tesco old st h exp|boots|royal'), 
    'Self-Care', df['Category'] )
    
# Fines

df['Category'] = np.where(df['Description'].str.contains(
    'car rental'), 
    'Fines', df['Category'] )
    
# Lore So What

df['Category'] = np.where(df['Description'].str.contains(
    'tubebuddy|itunes|dario|calendly|canva|epidemic|upwork|lada'), 
    'Shubhanshi', df['Category'] )
    
# Coffee

df['Category'] = np.where(df['Description'].str.contains(
    'lavelle|hart|starbucks|barista|new road|mama shelter'), 
    'Coffee', df['Category'] )
    
# Shopping
    
df['Category'] = np.where(df['Description'].str.contains(
    'islington|at camden town'), 
    'Shopping', df['Category'] )
    
# Restaurants

df['Category'] = np.where(df['Description'].str.contains(
    'bakehouse|zettle|caravan|kod|eating|o ver|mcdonald|manteca|wine house|giacomo|real greek|restaurant|katsute|tonkotsu|zia lucia|viet|change please|me zhi chua|osm'), 
    'Restaurants', df['Category'] )
        
# Entertainment
    
df['Category'] = np.where(df['Description'].str.contains(
    'montys|urban|oshveda|egg|francesco|budgens whitechapel'), 
    'Entertainment', df['Category'] )
    
# Gifts
    
df['Category'] = np.where(df['Description'].str.contains(
    'gucci|blomma'), 
    'Gifts', df['Category'] )
    
# Services
    
df['Category'] = np.where(df['Description'].str.contains(
    'apple|snappy|exchanged to usd'), 
    'Services', df['Category'] )
    
# Excluded
    
df['Category'] = np.where(df['Description'].str.contains(
    'from|paypal|amznmktplace|starnow|refund|giffgaff|backstage|hectagon|tower hamlets bc|sweet suites|temporary hold|cm.com'), 
    'Excluded', df['Category'] )

# Groceries

df['Category'] = np.where(df['Description'].str.contains(
    'tesco|sainsbury|asda|lidl|toogoodtog|nisa|market|millennium mini store'), 
    'Groceries', df['Category'] )

# Transport
    
df['Category'] = np.where(df['Description'].str.contains(
    'uber|zipcar|bird|tfl|Ewa'), 
    'Transport', df['Category'] )
    
# Travel
    
df['Category'] = np.where(df['Description'].str.contains(
    'ryanair|easyjet|airways'), 
    'Travel', df['Category'] )

# Convert the "Date" column to a datetime format
df['Date'] = pd.to_datetime(df['Date'])

# Extract the month and year information
df['Month'] = df['Date'].dt.month
df['Year'] = df['Date'].dt.year
    
pd.options.display.max_rows = 999
df.head(60)


# In[12]:


#Get the lastest month and year
latest_month =  df['Month'].max()
latest_year =  df['Year'].max()

#Filter the dataframe to include transaction from the latest month
last_month_expenses = df[(df['Month'] == latest_month) & (df['Year'] == latest_year)]


# In[13]:


last_month_expenses = last_month_expenses.groupby('Category')['Amount'].sum().reset_index()

last_month_expenses['Amount']=last_month_expenses['Amount'].astype('str')
last_month_expenses['Amount']=last_month_expenses['Amount'].str.replace('-','')
last_month_expenses['Amount']=last_month_expenses['Amount'].astype('float')        #get absolute figures

last_month_expenses = last_month_expenses[last_month_expenses["Category"].str.contains("Excluded|unassigned") == False]    #exclude "excluded" category
last_month_expenses = last_month_expenses.sort_values(by='Amount', ascending=False)    #sort values
last_month_expenses['Amount'] = last_month_expenses['Amount'].round().astype(int)      #round values

last_month_expenses


# In[14]:


#last month total

last_month_expenses_tot = last_month_expenses['Amount'].sum()
last_month_expenses_tot


# In[15]:


def calculate_difference(event):
    income = float(income_widget.value)
    recurring_expenses = float(recurring_expenses_widget.value)
    monthly_expenses = float(monthly_expenses_widget.value)
    difference = income - recurring_expenses - monthly_expenses
    difference_widget.value = str(difference)

income_widget = pn.widgets.TextInput(name="Income", value="0")
recurring_expenses_widget = pn.widgets.TextInput(name="Recurring Expenses", value="0")
monthly_expenses_widget = pn.widgets.TextInput(name="Non-Recurring Expenses", value=str(last_month_expenses_tot))
difference_widget = pn.widgets.TextInput(name="Last Month's Savings", value="0")

income_widget.param.watch(calculate_difference, "value")
recurring_expenses_widget.param.watch(calculate_difference, "value")
monthly_expenses_widget.param.watch(calculate_difference, "value")

#pn.Row(income_widget, recurring_expenses_widget, monthly_expenses_widget, difference_widget).show()


# In[16]:


## Create last month expenses bar chart
last_month_expenses_chart = last_month_expenses.hvplot.bar(
    x='Category', 
    y='Amount', 
    height=250, 
    width=850, 
    title="Last Month Expenses",
    ylim=(0, 500))

last_month_expenses_chart


# In[17]:


# Create monthly expenses trend bar chart 


df['Date'] = pd.to_datetime(df['Date'])            # convert the 'Date' column to a datetime object
df['Month-Year'] = df['Date'].dt.to_period('M')    # extract the month and year from the 'Date' column and create a new column 'Month-Year'
monthly_expenses_trend_by_cat = df.groupby(['Month-Year', 'Category'])['Amount'].sum().reset_index()

monthly_expenses_trend_by_cat['Amount']=monthly_expenses_trend_by_cat['Amount'].astype('str')
monthly_expenses_trend_by_cat['Amount']=monthly_expenses_trend_by_cat['Amount'].str.replace('-','')
monthly_expenses_trend_by_cat['Amount']=monthly_expenses_trend_by_cat['Amount'].astype('float')
monthly_expenses_trend_by_cat = monthly_expenses_trend_by_cat[monthly_expenses_trend_by_cat["Category"].str.contains("Excluded") == False]

monthly_expenses_trend_by_cat = monthly_expenses_trend_by_cat.sort_values(by='Amount', ascending=False)
monthly_expenses_trend_by_cat['Amount'] = monthly_expenses_trend_by_cat['Amount'].round().astype(int)
monthly_expenses_trend_by_cat['Month-Year'] = monthly_expenses_trend_by_cat['Month-Year'].astype(str)
monthly_expenses_trend_by_cat = monthly_expenses_trend_by_cat.rename(columns={'Amount': 'Amount '})

monthly_expenses_trend_by_cat


# In[18]:



#Define Panel widget

select_category1 = pn.widgets.Select(name='Select Category', options=[
    'All',
    'Self-Care',
    'Fines',
    'LoreSoWhat',
    'Coffee',
    'Groceries',
    'Shopping',
    'Restaurants',
    'Transport',
    'Travel',
    'Entertainment',
    'Gifts',
    'Services',
    #'Excluded'
])

select_category1


# In[19]:


# define plot function
def plot_expenses(category):
    if category == 'All':
        plot_df = monthly_expenses_trend_by_cat.groupby('Month-Year').sum()
    else:
        plot_df = monthly_expenses_trend_by_cat[monthly_expenses_trend_by_cat['Category'] == category].groupby('Month-Year').sum()
    plot = plot_df.hvplot.bar(x='Month-Year', y='Amount ')
    return plot

# define callback function
@pn.depends(select_category1.param.value)
def update_plot(category):
    plot = plot_expenses(category)
    return plot

# create layout
monthly_expenses_trend_by_cat_chart = pn.Row(select_category1, update_plot)
monthly_expenses_trend_by_cat_chart[1].width = 600

monthly_expenses_trend_by_cat_chart


# In[21]:


# Create summary table

df = df[['Date', 'Category', 'Description', 'Amount']]
df['Amount']=df['Amount'].astype('str')
df['Amount']=df['Amount'].str.replace('-','')
df['Amount']=df['Amount'].astype('float')        #get absolute figures

df = df[df["Category"].str.contains("Excluded") == False]    #exclude "excluded" category
df['Amount'] = df['Amount'].round().astype(int)      #round values
df


# In[22]:


# Define a function to filter the dataframe based on the selected category
def filter_df(category):
    if category == 'All':
        return df
    return df[df['Category'] == category]

# Create a DataFrame widget that updates based on the category filter
summary_table = pn.widgets.DataFrame(filter_df('All'), height = 300,width=400)

# Define a callback that updates the dataframe widget when the category filter is changed
def update_summary_table(event):
    summary_table.value = filter_df(event.new)

# Add the callback function to the category widget
select_category1.param.watch(update_summary_table, 'value')

summary_table


# In[28]:


# Create Final Dashboard

template = pn.template.FastListTemplate(
    title="Personal Finances Summary",
    sidebar=[
        pn.pane.Markdown("## *If you can't manage your money, making more won't help*"),

        pn.pane.Markdown(""),
        pn.pane.Markdown(""),
        select_category1
    ],
    main=[
        pn.Row(income_widget, recurring_expenses_widget, monthly_expenses_widget, difference_widget, width=950),
        pn.Row(last_month_expenses_chart, height=240),
        pn.GridBox(
            monthly_expenses_trend_by_cat_chart[1],
            summary_table,
            ncols=2,
            width=500,  
            align='start',
            sizing_mode='stretch_width'
        )
    ]
)

template.show()


# In[ ]:




