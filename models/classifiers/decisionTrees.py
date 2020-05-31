#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd
from sklearn import preprocessing
from sklearn.model_selection import train_test_split
from keras.models import Sequential
import matplotlib.pyplot as plt
from sklearn import datasets, svm, metrics
import numpy as np
from matplotlib.colors import ListedColormap
from sklearn.preprocessing import StandardScaler
from sklearn.svm import SVC
from sklearn.tree import DecisionTreeClassifier
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score


# In[2]:


#Loading dataset


# In[3]:


df = pd.read_csv('dataset.csv')  #error_bad_lines=False


# In[4]:


df


# In[5]:


dataset = df.values


# In[6]:


dataset


# In[7]:


X = dataset[:,0:98] #Input features, the first 99 columns of the dataset


# In[8]:


X


# In[9]:


Y = dataset[:,98] #The feature i aim to predict


# In[10]:


Y


# In[11]:


min_max_scaler = preprocessing.MinMaxScaler()
X_scale = min_max_scaler.fit_transform(X) 
#scaler for make the range between 0 e 1


# In[12]:


X_scale


# Splitting the dataset, val_and_test size will be 30% of the overall dataset, then we split again in two parts
# test and val.

# In[13]:


X_train, X_val_and_test, Y_train, Y_val_and_test = train_test_split(X_scale, Y, test_size=0.3)


# In[14]:


X_val, X_test, Y_val, Y_test = train_test_split(X_val_and_test, Y_val_and_test, test_size=0.5)


# In[15]:


print(X_train.shape, X_val.shape, X_test.shape, Y_train.shape, Y_val.shape, Y_test.shape)


# In[16]:


X


# In[17]:


classifier = DecisionTreeClassifier(max_depth=3)


# In[18]:


classifier.fit(X_train, Y_train)


# In[19]:


predicted = classifier.predict(X_test)


# In[20]:


predicted.shape
Y_test.shape


# In[21]:


print(accuracy_score(Y_test, predicted))


# In[36]:


print("Classification report for classifier %s:\n%s\n"
      % (classifier, metrics.classification_report(Y_test, predicted)))

