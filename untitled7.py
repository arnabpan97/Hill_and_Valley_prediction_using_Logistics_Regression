# -*- coding: utf-8 -*-
"""Untitled7.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1aZs7o3oe-YPIR59dfz61KBptbk3us118

**Import Data**
"""

import pandas as pd

import numpy as np

"""**import CSV as Dataframe**"""

df=pd.read_csv('https://github.com/YBI-Foundation/Dataset/raw/main/Hill%20Valley%20Dataset.csv')

"""**Get First Five Rows of Dataframe**"""

df.head()

"""**Get Information of Dataframe**

**`Hill and Valley prediction using Logistics Regression`**
"""

df.describe()

"""**Get Column Names**"""

df.columns

"""**All column Names not Printed**"""

print(df.columns.tolist())

"""**Get Shape of Dataframe**"""

df.shape

"""**Get Unique Value in y Variable**"""

df['Class'].value_counts()

df.groupby('Class').mean()

"""**Define y and X **"""

y=df['Class']

y.shape

y

x=df[['V1', 'V2', 'V3', 'V4', 'V5', 'V6', 'V7', 'V8', 'V9', 'V10', 'V11', 'V12', 'V13', 'V14', 'V15', 'V16', 'V17', 'V18', 'V19', 'V20', 'V21', 'V22', 'V23', 'V24', 'V25', 'V26', 'V27', 'V28', 'V29', 'V30', 'V31', 'V32', 'V33', 'V34', 'V35', 'V36', 'V37', 'V38', 'V39', 'V40', 'V41', 'V42', 'V43', 'V44', 'V45', 'V46', 'V47', 'V48', 'V49', 'V50', 'V51', 'V52', 'V53', 'V54', 'V55', 'V56', 'V57', 'V58', 'V59', 'V60', 'V61', 'V62', 'V63', 'V64', 'V65', 'V66', 'V67', 'V68', 'V69', 'V70', 'V71', 'V72', 'V73', 'V74', 'V75', 'V76', 'V77', 'V78', 'V79', 'V80', 'V81', 'V82', 'V83', 'V84', 'V85', 'V86', 'V87', 'V88', 'V89', 'V90', 'V91', 'V92', 'V93', 'V94', 'V95', 'V96', 'V97', 'V98', 'V99', 'V100', 'Class']]

x=df.drop('Class',axis=1)

x.shape

x

"""**Get Plot First Two Rows**"""

import matplotlib.pyplot as plt

plt.plot(x.iloc[0,:])
plt.title('Valley');

plt.plot(x.iloc[0,:])
plt.title('Hill');

"""**Get x Variables Standerdized**"""

from sklearn.preprocessing import StandardScaler

ss=StandardScaler()

x=ss.fit_transform(x)

x

x.shape

"""**Get Train Test Split**"""

from sklearn.model_selection import train_test_split

x_train,x_test,y_train,y_test=train_test_split(x,y,test_size=0.3,stratify=y,random_state=2529)

x_train.shape,x_test.shape,y_train.shape,y_test.shape

"""**Get Model Train**"""

from sklearn.linear_model import LogisticRegression

lr=LogisticRegression()

lr.fit(x_train,y_train)

"""**Get Model Prediction**"""

y_pred=lr.predict(x_test)

y_pred.shape

y_pred

"""**Get Probability of Each Predicted Class**"""

lr.predict_proba(x_test)

"""**Get Model Evalution**"""

from sklearn.metrics import confusion_matrix,classification_report

print(confusion_matrix(y_test,y_pred))

print(classification_report(y_test,y_pred))

"""**Get Future predictions**"""

x_new=df.sample(1)

x_new

x_new.shape

x_new=x_new.drop('Class',axis=1)

x_new.shape

x_new=ss.fit_transform(x_new)

y_pred_new=lr.predict(x_new)

y_pred_new

lr.predict_proba(x_new)