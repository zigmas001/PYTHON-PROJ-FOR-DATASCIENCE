#!/usr/bin/env python
# coding: utf-8

# In[1]:


# QUESTION 1


# In[2]:


get_ipython().system('pip install yfinance==0.2.4')
#!pip install pandas==1.3.3


# In[3]:


import yfinance as yf
import pandas as pd


# In[4]:


tesla = yf.Ticker("TSLA")


# In[5]:


tesla_price = tesla.history(period = "max")


# In[6]:


tesla_price.reset_index(inplace = True)
tesla_price["Date"] = tesla_price["Date"].dt.date
tesla_price.head(5)


# In[7]:


# QUESTION 2


# In[13]:


get_ipython().system('pip install bs4')
get_ipython().system('pip install html5lib')
get_ipython().system('pip install lxml==4.9.1')


# In[9]:


import pandas as pd
import requests
from bs4 import BeautifulSoup


# In[10]:


url = 'https://www.macrotrends.net/stocks/charts/TSLA/tesla/revenue'


# In[ ]:





# In[11]:


tesla_data = requests.get(url).text
print(tesla_data)


# In[12]:


soup = BeautifulSoup(tesla_data, 'html5lib')


# In[13]:


tesla_revenue = pd.DataFrame(columns=["Date", "Revenue"])


# In[14]:


# Find all tables with class 'historical_data_table'
tables = soup.find_all('table', class_='historical_data_table')

# Extract the second table (index 1) with title 'Tesla Quarterly Revenue'
table = tables[1]

# Find the table body and iterate over the rows
table_body = table.find('tbody')
rows = table_body.find_all('tr')

for row in rows:
    cells = row.find_all('td')
    if len(cells) >= 2:
        date = cells[0].text.strip()
        revenue = cells[1].text.strip().replace('$', '').replace(',', '')
        
        # Skip rows with empty revenue
        if revenue != '':
            tesla_revenue = pd.concat([tesla_revenue, pd.DataFrame({"Date": [date], "Revenue": [revenue]})], ignore_index=True)


# In[15]:


print(tesla_revenue.tail())


# In[16]:


# QUESTION 3


# In[17]:


import yfinance as yf
import pandas as pd


# In[18]:


gamestop = yf.Ticker("GME")


# In[19]:


gamestop_price = gamestop.history(period = "max")


# In[20]:


gamestop_price.reset_index(inplace = True)
gamestop_price["Date"] = gamestop_price["Date"].dt.date
gamestop_price.head()


# In[21]:


# QUESTION 4


# In[22]:


url = 'https://www.macrotrends.net/stocks/charts/GME/gamestop/revenue'
gme_data = requests.get(url).text
print(gme_data)


# In[23]:


soup = BeautifulSoup(gme_data, 'html5lib')


# In[24]:


gme_revenue = pd.DataFrame(columns=["Date", "Revenue"])


# In[25]:


# Find all tables with class 'historical_data_table'
tables = soup.find_all('table', class_='historical_data_table')

# Extract the second table (index 1) with title 'Tesla Quarterly Revenue'
table = tables[1]

# Find the table body and iterate over the rows
table_body = table.find('tbody')
rows = table_body.find_all('tr')

for row in rows:
    cells = row.find_all('td')
    if len(cells) >= 2:
        date = cells[0].text.strip()
        revenue = cells[1].text.strip().replace('$', '').replace(',', '')
        
        # Skip rows with empty revenue
        if revenue != '':
            gme_revenue = pd.concat([gme_revenue, pd.DataFrame({"Date": [date], "Revenue": [revenue]})], ignore_index=True)


# In[26]:


print(gme_revenue.tail())


# In[27]:


# QUESTION 5


# In[28]:


import matplotlib.pyplot as plt

def make_graph1(dataframe, x_column, y_column, title):
    dataframe = dataframe.sort_values(x_column)  # Sort the dataframe by the x_column in ascending order
    plt.figure(figsize=(12, 8))
    plt.plot(dataframe[x_column], dataframe[y_column])
    plt.xlabel(x_column)
    plt.ylabel("Price ($US)")
    plt.title(title)
    plt.xticks(rotation=45)
    plt.grid(True)
    plt.show()

def make_graph2(dataframe, x_column, y_column, title):
    dataframe = dataframe.sort_values(x_column)  # Sort the dataframe by the x_column in ascending order
    plt.figure(figsize=(12, 8))
    plt.plot(dataframe[x_column], dataframe[y_column])
    plt.xlabel(x_column)
    plt.ylabel("Revenue ($US Millions)")
    plt.title(title)
    plt.xticks(rotation=45)
    plt.gca().yaxis.set_major_locator(plt.MultipleLocator(10))
    plt.gca().xaxis.set_major_locator(plt.MultipleLocator(10))
    plt.grid(True)
    plt.show()

    
# Plot the data
make_graph1(tesla_price, "Date", "Close", "Tesla Historical Share Price")
make_graph2(tesla_revenue, "Date", "Revenue", "Tesla Historical Revenue")


# In[29]:


# QUESTION 6


# In[30]:


import matplotlib.pyplot as plt

def make_graph1(dataframe, x_column, y_column, title):
    dataframe = dataframe.sort_values(x_column)  # Sort the dataframe by the x_column in ascending order
    plt.figure(figsize=(12, 8))
    plt.plot(dataframe[x_column], dataframe[y_column])
    plt.xlabel(x_column)
    plt.ylabel("Price ($US)")
    plt.title(title)
    plt.xticks(rotation=45)
    plt.grid(True)
    plt.show()

def make_graph2(dataframe, x_column, y_column, title):
    dataframe = dataframe.sort_values(x_column)  # Sort the dataframe by the x_column in ascending order
    plt.figure(figsize=(12, 8))
    plt.plot(dataframe[x_column], dataframe[y_column])
    plt.xlabel(x_column)
    plt.ylabel("Revenue ($US Millions)")
    plt.title(title)
    plt.xticks(rotation=45)
    plt.gca().yaxis.set_major_locator(plt.MultipleLocator(10))
    plt.gca().xaxis.set_major_locator(plt.MultipleLocator(10))
    plt.grid(True)
    plt.show()
 
    
    
# Plot the data
make_graph1(gamestop_price, "Date", "Close", "GameStop Historical Share Price")
make_graph2(gme_revenue, "Date", "Revenue", "GameStop Historical Revenue")

