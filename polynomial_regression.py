# -*- coding: utf-8 -*-
"""polynomial_regression.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1MrScxJV8vil8DDi5nwl_FG5v7juukiwe
"""

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

"""# 1. Data Load"""

dataset = pd.read_csv('Position_Salaries.csv')
dataset

"""# 2. X와 y 분리"""

# dataset을 ndarray로 변환
salary = dataset.values
salary

# X: Level, y: Salary
# Level입력에 대해 Salary를 예측하는 regression model

# X는 모든 행, 두 번째(index=1) 열
# X는 반드시 2D array가 되어야 함
# 2D array가 되기 위해서는 행과 열 모두 범위로 표기해야 함
X = salary[:, 1:2]

# y는 모든 행, 마지막(index=2 or -1) 열
y = salary[:, -1]

print(X.shape, y.shape)

"""# 3. Training data와 Test data 분리"""

# train:test = 7:3
from sklearn.model_selection import train_test_split

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=42)

print(X_train.shape, X_test.shape, y_train.shape, y_test.shape)

"""# 4. Polynomial features"""

from sklearn.preprocessing import PolynomialFeatures

# PolynomialFeatures 객체 생성 시 degree 입력
pf = PolynomialFeatures(degree=1)

# fit: PolynomialFeatures로 확장하기 위한 전략 수립(실제 변환 X)
pf.fit(X_train)

# transform: 반드시 fit 실행 후 변환(transform)해야 함
Xp_train = pf.transform(X_train)

"""# 5. Linear Regression 학습"""

from sklearn.linear_model import LinearRegression

# LinearRegression을 학습(fit)할 때, PolynomialFeatures를 사용하면 Polynomial Regression인 것임
p_lr = LinearRegression()
p_lr.fit(Xp_train, y_train)

"""# 6. Prediction(X_test에 대한 예측값)"""

# predict에 적용되는 X_test는 반드시 학습에서 적용한 PolynomialFeatures 형태로 변환해야 함
Xp_test = pf.transform(X_test)
y_pred = p_lr.predict(Xp_test)

"""# 7. 성능 확인(mean_squared_error, r2_score)"""

from sklearn.metrics import mean_squared_error, mean_absolute_error, r2_score

print(mean_absolute_error(y_test, y_pred))
print(r2_score(y_test, y_pred))

"""# 8. 결과 시각화"""

np.arange(1, 11, 0.1)

plt.scatter(X_train, y_train)
plt.scatter(X_test, y_test)

# np.arange(1, 11, 0.1): 1부터 11 사이의 값을 0.1 간격으로 생성(11은 포함 X)
# np.arange(1, 11, 0.1).reshape(-1, 1): 위의 결과를 1열로 구성된 2D array로 변환
X_sample = np.arange(1, 11, 0.1).reshape(-1, 1)

Xp_sample = pf.transform(X_sample)
y_sample_pred = p_lr.predict(Xp_sample)

plt.plot(X_sample, y_sample_pred, color='red')
plt.legend(['Training', 'Test', 'Polynomial model'])