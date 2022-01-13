# -*- coding: utf-8 -*-
"""
Created on Thu Jan 13 20:55:26 2022
@author: sreeh4ri
"""
import pandas as pd
import pickle
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression

# Read data and extract features
salary_data = pd.read_csv('Salary_Data.csv')
X = salary_data.drop(['Salary'], axis=1)
y = salary_data.drop(['YearsExperience'], axis=1)
# Split to train and test
X_train, X_test, y_train, y_test = train_test_split(
    X, y, random_state=42, test_size=0.2)
# Model
lr_model = LinearRegression().fit(X_train, y_train)
# Save model to disk
model_file = open('model.pkl', 'wb')
pickle.dump(lr_model, model_file)
model_file.close()
