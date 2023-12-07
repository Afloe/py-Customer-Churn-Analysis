#!/usr/bin/env python
# coding: utf-8

# # Customer Churn Analysis

# In[1]:


import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt


# In[2]:


df = pd.read_csv(r"C:\Users\USER\Downloads\Customer-Churn.csv")
df


# In[3]:


df.drop_duplicates()


# In[4]:


"""
There are no duplicates from the data
"""


# In[5]:


df.info()


# In[6]:


pd.set_option('display.max.column', 22)
df


# In[7]:


"""
From the data set, the values of TotalCharges are numeric but its data type from the data info is object
Hence the need to change its data type to float
"""


# In[8]:


df['TotalCharges'] = pd.to_numeric(df['TotalCharges'], errors = 'coerce')
df['TotalCharges']


# In[9]:


df.info()


# In[10]:


df.isnull().sum()


# In[11]:


"""
Changing the data type of TotalCharges has indicated there were 11 null values in that column
"""


# In[70]:


df.describe()


# In[12]:


"""
Analysis on impact on some attritubes on Churn
"""


# In[13]:


df.columns


# In[14]:


"""
Impact of gender on Churn
"""


# In[16]:


df.groupby('gender')['customerID'].count()


# In[17]:


df.groupby(['gender', 'Churn'])['customerID'].count()


# In[19]:


df.groupby(['gender', 'Churn'])['customerID'].count().plot()


# In[18]:


sns.countplot(x = 'gender', data = df, hue = 'Churn')
plt.show()


# In[ ]:


"""
Impact of Senior Citizen on Churn
"""


# In[20]:


df.groupby('SeniorCitizen')['customerID'].count()


# In[21]:


df.groupby(['SeniorCitizen', 'Churn'])['customerID'].count()


# In[22]:


df.groupby(['SeniorCitizen', 'Churn'])['customerID'].count().plot()


# In[23]:


sns.countplot(x = 'SeniorCitizen', data = df, hue = 'Churn')
plt.show()


# In[24]:


"""
From the analysis made, those who are senior citizen had higher rate of churned services relative to those who are not
"""


# In[25]:


"""
Impact of InternetService on Churn
"""


# In[26]:


df.groupby('InternetService')['customerID'].count()


# In[27]:


df.groupby(['InternetService', 'Churn'])['customerID'].count()


# In[28]:


df.groupby(['InternetService', 'Churn'])['customerID'].count().plot()


# In[29]:


sns.countplot(x = 'InternetService', data = df, hue = 'Churn')
plt.show()


# In[30]:


"""
From the analysis on internet service, fiber optic had higher numbers and rate of churned services compared to the other
services
Hence, services on fiber optic needs to be improved to keep its customers
"""


# In[31]:


"""
Impact of online security on churn
"""


# In[32]:


df.groupby('OnlineSecurity')['customerID'].count()


# In[33]:


"""
Projection shown that a lot of customers do not have online security services
"""


# In[34]:


df.groupby(['OnlineSecurity', 'Churn'])['customerID'].count()


# In[35]:


df.groupby(['OnlineSecurity', 'Churn'])['customerID'].count().plot()


# In[36]:


sns.countplot(x = 'OnlineSecurity', data = df, hue = 'Churn')


# In[37]:


"""
The projection shows that most of the churned services were from customers with no online security
In order to keep customers, the teleco has to work on providing online security to its customers
"""


# In[38]:


"""
Impact on technical Support on churn
"""


# In[39]:


df.groupby('TechSupport')['customerID'].count()


# In[40]:


df.groupby(['TechSupport', 'Churn'])['customerID'].count()


# In[41]:


df.groupby(['TechSupport', 'Churn'])['customerID'].count().plot()


# In[42]:


sns.countplot(x = 'TechSupport', data = df, hue = 'Churn')
plt.show()


# In[43]:


"""
The visualization shows that large number of customers had no technical support and most of those customers churned services
The teleco has to work on improving and providing technical support to its customers
"""


# In[44]:


df.columns


# In[45]:


"""
Impact of contract on churn
"""


# In[46]:


df.groupby('Contract')['customerID'].count()


# In[47]:


df.groupby(['Contract', 'Churn'])['customerID'].count()


# In[48]:


sns.countplot(x = 'Contract', data = df, hue = 'Churn')
plt.show()


# In[49]:


"""
The visualization show that month-to-month had the highest number of customers and also had the highest rate of churn servies
"""


# In[50]:


"""
Correlation
"""


# In[51]:


df.corr()


# In[52]:


sns.heatmap(df.corr(), annot = True)
plt.show()


# In[53]:


"""
Each attritube is highly correlated to itself
Tenure and TotalCharges have the next high correlation
SeniorCitizen and Tenure have the least correlation between each other
"""


# In[54]:


"""
Boxplot of Churn on MonthlyCharges and TotalCharges
"""


# In[55]:


sns.boxplot(x = 'Churn', y = 'MonthlyCharges', data = df)
plt.show()


# In[56]:


sns.boxplot(x = 'Churn', y = 'TotalCharges', data = df)
plt.show()


# In[58]:


"""
From the visualization TotalCharges has outliers
"""


# In[59]:


"""
Linear relationship between TotalCharges and MonthlyCharges
"""


# In[64]:


sns.lmplot(x = 'TotalCharges', y = 'MonthlyCharges', data = df, hue = 'Churn')
plt.show()


# In[67]:


sns.distplot(df.TotalCharges, bins = 1000)
plt.show()


# In[73]:


sns.distplot(df.MonthlyCharges, bins = 20)
plt.show()


# In[69]:


df['TotalCharges']


# In[75]:


sns.pairplot(data = df)
plt.show()


# In[ ]:





# In[ ]:





# In[ ]:




