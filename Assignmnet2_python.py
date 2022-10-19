#!/usr/bin/env python
# coding: utf-8

# In[1]:


import numpy as np


# In[2]:


a = np.random.randint(1,20,15)
#Random vector of size 15 having only Integers in the range 1-20.


# In[3]:


a


# In[5]:


a= a.reshape(3,5)
a
#Reshape the array to 3 by 5


# In[6]:


a.shape
#To print array shape


# In[8]:


a[a==a.max()]=0
a
#Replacing the max in each row by 0


# In[9]:


import pandas as pd


# In[11]:


data = pd.read_csv("C:/Users/deeks/OneDrive/Documents/machine learning/Python/data.csv")
data
#To read the given csv file


# In[14]:


data.describe()
#To show basic descrption of the data


# In[12]:


mean = data['Calories'].mean()
data
#To get the mean of the Calories


# In[13]:


data.head(20)


# In[15]:


data.isnull().sum()
#To see if there are any null values


# In[17]:


data['Calories'].fillna(value=mean,inplace=True)
data
#To replace the null values with the mean value


# In[18]:


data.head(20)


# In[21]:


result = data.groupby('Duration').agg({'Pulse': ['mean', 'min', 'max','count']})
result
#Selected two columns and aggregated the data using: min, max, count, mean


# In[23]:


data1 = data[(data['Calories']>500) & (data['Calories']<1000)]
data1
#Filtered the dataframe to select the rows with calories values between 500 and 1000. 


# In[26]:


data2 = data[(data['Calories']>500) & (data['Calories']<1000)]
data2
#Filtered the dataframe to select the rows with calories values > 500 and pulse < 100 which is nothing but same as previous one. 


# In[28]:


df_modified=data.drop("Maxpulse",axis=1)
df_modified
#Created a new “df_modified” dataframe that contains all the columns from data except for “Maxpulse”.


# In[29]:


data


# In[30]:


del data['Maxpulse']
data
#Deleted the “Maxpulse” column from the main df dataframe


# In[31]:


data["Calories"] = data["Calories"].astype(float).astype(int)
data
#Converting the datatype of Calories column to int datatype.


# In[32]:


data.plot.scatter(x = 'Duration', y = 'Calories')
#created a scatter plot for the two columns (Duration and Calories).


# In[33]:


import matplotlib.pyplot as plt
#Imported the required libraries to plot a pie chart
languages = 'Java', 'Python', 'PHP', 'JavaScript', 'C#', 'C++'
popuratity = [22.2, 17.6, 8.8, 8, 7.7, 6.7]
#Given data
colors = ["#1f77b4", "#ff7f0e", "#2ca02c", "#d62728", "#9467bd", "#8c564b"]
#Codes for the colors which are predefined
explode = (0.1, 0, 0, 0,0,0)  
#To only explode the first slice, we took 0.1
plt.pie(popuratity, explode=explode, labels=languages, colors=colors,
autopct='%2.1f%%', shadow=True, startangle=150)
#To plot

plt.axis('equal')
plt.show()

