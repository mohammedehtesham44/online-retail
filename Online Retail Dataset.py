#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd
import numpy as np


# In[2]:


dataset = pd.read_csv("onlineRetail.project.csv.csv")


# In[3]:


dataset.head()


# In[4]:


dataset.info()


# # GIVEN MINING FOR COLUMN FROM THE DATASET:-
# Invoice Number: This is the number that identifies a transaction.
# Stock code    : This refers to the product ID.
# Description   : This describes the product that a user purchased.
# Quantity      : It specified the quantity of the item purchased.
# Invoice Date  : The date on which the transaction took place.
# Unit Price    : Price of one product.
# Customer ID   : It identifies the customer
# Country       : The country where the transaction was performed

# # the unique volues¶

# In[5]:


print("Number of transactions: ",dataset['InvoiceNo'].nunique())
print("Number of products:",dataset['StockCode'].nunique())
print("Number of Customers:",dataset['CustomerID'].nunique())
print("Number of Countries:",dataset['Country'].nunique())


# In[6]:


#The percentage of customers with nulln id
print("percentage of Customer NA: ", round (dataset['CustomerID'].isnull().sum() * 100 / len(dataset),2),"%")


# In[7]:


#analysis the data.
dataset.describe()


# In[8]:


#Costomers by country
dataset['total_cost'] = dataset['Quantity'] = dataset['UnitPrice']
dataset.head()


# In[9]:


dataset.groupby('Country').sum().sort_values(by='total_cost',ascending=False)


# In[10]:


get_ipython().run_line_magic('matplotlib', 'inline')


# In[11]:


import matplotlib.pyplot as plt


# In[12]:


dataset.hist(bins=50, figsize=(20, 15))

