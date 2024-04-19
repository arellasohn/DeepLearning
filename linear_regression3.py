# -*- coding: utf-8 -*-
"""linear_regression2.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1QOidLaKkTKHNZfH12W4PtRTMsERXhbcU
"""

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

"""# 1. Data Load"""

dataset = pd.read_csv('50_Startups.csv')
dataset.head(3)

"""- R&D Spend, Administration, Marketing Spend 정보를 이용하여 Profit 예측"""

startups = dataset.values

"""# 2. X와 y 분리"""

X = startups[:,:3]
y = startups[:,-1]

print(X.shape, y.shape)

"""# 3. Training data와 Test data 분리"""

from sklearn.model_selection import train_test_split

X_train, X_test, y_train, y_test = train_test_split(X,y,test_size=0.25,random_state=42)
print(X_train.shape, X_test.shape, y_train.shape, y_test.shape)
# X의 행의 수: sample의 수 (training과 test의 sample수는 다름(동일할 수 도 있음))
# X의 열의 수: 특징의 수 (R&D Spend, Administration, Marketing Spend), (training과 test의 특징 수는 반드시 동일해야 함)

"""# 4. Linear regression 학습"""

from sklearn.linear_model import LinearRegression
# LinearRegression model 생성 (profit을 예측하기 위한 lineasr regression model 생성)
lr = LinearRegression()
# Training data를 통해 model을 학생
lr.fit(X_train, y_train)
# fit을 실행한 후, model 생성 완료

"""# 5. Prediction (X_test값을 model의 입력으로 하여, Profit 값 예측하기)"""

pred = lr.predict(X_test)
# X_test.shape = (13,3)
# X_test는 R&D Spend, Administration, Marketing Spend 3개의 특징을 가진 13개의 sample data(X)
# pred: 13개 Sample data에 대한 예측값
# X_test에 대한 실제 값(target, 정답)은 y_test
# pred와 y_test를 비교하여, 성능을 평가할 수 있음
print(pred.shape)
print(pred)

"""# 6. Regression model 성능 평가하기"""

from sklearn.metrics import mean_squared_error, mean_absolute_error, r2_score
mse = mean_squared_error(y_test,pred)
mae = mean_absolute_error(y_test,pred)
r2 = r2_score(y_test,pred)

print('MSE: ', mse)
print('MAE: ', mae)
print('R2:  ', r2)
# MSE, MAE는 다른 model과 성능을 비교할 때는 좋은 척도이나, 단독으로 model을 평가하기는 애매함
# R2는 주로 0보다 크고, 1보다 같거나 작은 값이므로, classification에서 accuracy와 유사한 정보로, 단독으로 model을 평가하기 좋음

"""# 7. 결과 시각화

- y_test와 pred 한 번에 시각화하기
"""

plt.plot(y_test,marker='^',markersize=8,label='actual value') # 정답, target, actual value
plt.plot(pred,marker='*',markersize=10,label='prediction')   # 예측값, prediction
plt.legend()
plt.grid()
plt.ylabel('profit')
plt.title('Linear Regression')
