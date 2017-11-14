# -*- coding: utf-8 -*-
"""
Created on Fri Jun 23 00:25:13 2017

@author: zdutta
"""

# Data Preprocessing Template

# Importing the libraries
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
from sklearn.preprocessing import LabelEncoder,OneHotEncoder
from sklearn.linear_model import LinearRegression
import statsmodels.formula.api as sm 



# Importing the dataset
dataset = pd.read_csv('50_Startups.csv')
X = dataset.iloc[:, :-1].values
y = dataset.iloc[:, -1].values

#encoding categorical data
labelencoder_X = LabelEncoder()
X[:,-1] = labelencoder_X.fit_transform(X[:,-1])
onehotencoder = OneHotEncoder(categorical_features=[-1])
X = onehotencoder.fit_transform(X).toarray()

#Avoiding the dummy variable trap 
X = X[:,1:]


# Splitting the dataset into the Training set and Test set
from sklearn.cross_validation import train_test_split
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size = 0.2, random_state = 0)

# Feature Scaling
"""from sklearn.preprocessing import StandardScaler
sc_X = StandardScaler()
X_train = sc_X.fit_transform(X_train)
X_test = sc_X.transform(X_test)
sc_y = StandardScaler()
y_train = sc_y.fit_transform(y_train)"""

#Fitting Multiple Linear Regression to the Training Set
regressor = LinearRegression()
regressor.fit(X_train, y_train)

#Predicting the Test set results
y_pred = regressor.predict(X_test)

#Building the optimal model using Backward Elimination
#X0 = 1, adding a column of ones
X = np.append(arr=np.ones((50,1)).astype(int),values = X,axis=1)
X_opt = X[:,[0,1,2,3,4,5]]
#ordinary least squares
regressor_OLS = sm.OLS(endog = y , exog = X_opt ).fit()
regressor_OLS.summary()

#removing predictor with the greatest P value over SL
X_opt = X[:,[0,1,3,4,5]]
regressor_OLS = sm.OLS(endog = y , exog = X_opt ).fit()
regressor_OLS.summary()

X_opt = X[:,[0,3,4,5]]
regressor_OLS = sm.OLS(endog = y , exog = X_opt ).fit()
regressor_OLS.summary()

X_opt = X[:,[0,3,5]] #R&D span powerful predictor
regressor_OLS = sm.OLS(endog = y , exog = X_opt ).fit()
regressor_OLS.summary()

X_opt = X[:,[0,3]] #R&D span and marketing span lightly over 0.05 SL 
regressor_OLS = sm.OLS(endog = y , exog = X_opt ).fit()
regressor_OLS.summary()
#optimal team of independent variables to predict profit is only R&D



