#!/usr/bin/env python
# coding: utf-8

# # Iris Model
# ***

# In[1]:


import numpy as np
import pandas as pd
import matplotlib.pyplot as plt


# ### 1. Load data into the python environment
# ***

# In[2]:


data = pd.read_excel('./iris.xls')
data.head()


# In[3]:


data.Classification.value_counts()


# From the above result it can be concluded that the above problem statement belongs to **"Multi-Class Classification Problem"**

# ### 2. Pre-processing
# ***

# In[4]:


# shape
data.shape


# In[5]:


# info
data.info()


# There are 4 columns in iris dataset out of which the predictor column 'Classification' belongs to object type. Rest columns belongs to float

# In[6]:


# check for null values
data.isna().sum()


# There are null values present in dataset

# In[7]:


for column in data.columns[:-1]:
    data[column].plot.hist()
    plt.show()


# From the histogram it is clear that columns in dataset are almost normally distributed, so null values can be replaced with mean

# In[8]:


data.describe().T


# In[9]:


# Filling missing values
for column in data.columns[:-1]:
    data[column].fillna(round(data[column].mean(), 1), inplace= True)


# In[10]:


data.isna().sum()


# All the null values have been removed

# In[11]:


data.describe().T


# Filling with mean didnot introduce observable change in dataset

# In[12]:


# Label Encode 'Classification' Column
from sklearn.preprocessing import LabelEncoder
data['Classification'] = LabelEncoder().fit_transform(data['Classification'])


# In[13]:


data.Classification.value_counts()


# ### 3. Model Building
# ***

# In[14]:


# Function to check model performances
from sklearn.metrics import f1_score, accuracy_score, precision_score, recall_score, confusion_matrix
def check_model_metrices(y_test, y_pred):
    print('Model Accuracy = ', accuracy_score(y_test, y_pred))
    print('Model Precision = ', precision_score(y_test, y_pred, average='micro'))
    print('Model Recall = ', recall_score(y_test, y_pred, average='micro'))
    print('Model F1 Score = ', f1_score(y_test, y_pred, average='micro'))
    print('Confusion Matrix = \n', confusion_matrix(y_test, y_pred))


# In[15]:


# feature selection
X = data[data.columns[:-1]] # features
y = data['Classification'] # target
print(f'Feature shape: {X.shape}')


# In[16]:


# Spliting to training and testing sets
from sklearn.model_selection import train_test_split
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=42)
print(f'X_train shape: {X_train.shape}')
print(f'X_test shape: {X_test.shape}')


# #### Model : Random Forest
# ***

# In[17]:


from sklearn.ensemble import RandomForestClassifier
rf = RandomForestClassifier()
rf.fit(X_train, y_train)
rf_pred = rf.predict(X_test)


# In[18]:


check_model_metrices(y_test, rf_pred)


# In[19]:


import pickle
pickle_file = open('./iris-model.pkl', 'wb')
pickle.dump(rf, pickle_file)
pickle_file.close()

