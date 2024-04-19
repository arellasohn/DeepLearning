# -*- coding: utf-8 -*-
"""neural_networks.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1TkLC0JPnua2XF-VXbfaSozRXh30u3X12

# 1. Library
"""

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

from tensorflow.keras.layers import Dense
from tensorflow.keras.models import Sequential

"""# 2. Load data
- X와 y분리
- training / test data 분리
"""

dataset = pd.read_csv('Iris_ohe.csv').values

dataset[-5:]

# X: column index 1부터 index 4까지 (SepalLength, SepalWidth, PetalLength, PetalWidth)
# y: column index 5부터 index 7(마지막 index)까지 (Setosa, Versicolor, Virginica)
X = dataset[:,1:5]
y = dataset[:,5:]
# print(X)
# print(y)
print(X.shape, y.shape)

from sklearn.model_selection import train_test_split
X_train,X_test,y_train,y_test = train_test_split(X,y,test_size=0.2,random_state=15)
print(X_train.shape, X_test.shape, y_train.shape, y_test.shape)

"""# 3. Artificial Neural Netwokrs(ANN) structure
- Multi-layer perceptron (MLP)

1) input layer의 node는 몇 개인가? 4개 = X column의 수 = 특징의 수(sepalWidth,sepalLength,petalWidth,petalLength)<br>
2) output layer의 node는 몇 개인가? 3개 = y column의 수 = class의 수(setosa,versicolor,virginica)<br>
3) 몇 개의 hidden layer로 구성할 것인가? 1개(임의로 지정)<br>
4) 각 hidden layer node의 수는 몇 개인가? 5개(임의로 지정)<br>
5) 어떠한 activation function을 사용할 것인가?
"""

# X_train에 포함된 하나의 sample에 대한 shape
sample_shape = X_train[0].shape  # (4,)
num_class = y_train.shape[1]     # 3
# y_train 또는 y_test의 shape은 각각 (데이터 sample의 수, class의 수)
# 그러므로 y_train.shape[0] = training data의 수, y_train.shape[1] = class의 수

# Sequential(ANN의 layer를 정의)
iris_model = Sequential([
    # 1. input layer → hidden layer
    Dense(5,activation='relu',input_shape=sample_shape),
    # → Dense(5,activation='relu',input_shape=(4,)),
    # Dense(hidden layer node의 수, activation function, input_shape(입력 데이터의 shape))
    # * activation = 'sigmoid' or 'relu' or 'tanh' or 'softmax' or 'linear'
    #   일반적으로 relu를 가장 많이 사용함
    #   softmax는 분류(classification) 문제에서 output layer에 적용됨
    # * input_shape은 X_train의 shape을 의미하지 않으며, X_train에 포함된 하나의 sample에 대한 shape을 의미한다.
    #   ex> X_train.shape = (120,4)일 때, X_train 중 하나의 data에 대한 shape을 의미하므로 input_shape = (4,)가 된다.
    #       X_train.shape에서 120은 sample의 수를 의미하며, neural networks를 설계할 sample의 수는 영향을 미치지 않는다.
    #       table 형태로 저장된 csv 파일 형태인 경우, 대부분의 경우 input_shape은 1 darray이다.
    #       위의 예에서는 input_shape = X_train[0].shape = (4,)

    # 2. hidden layer → output layer
    Dense(num_class,activation='softmax')
    # → Dense(3,activation='softmax')
    # 첫번째 layer를 제외한 나머지 추가 layer는 이전 layer로부터 입력 shape을 가져오므로, 지정할 필요 없음
    # 위의 경우, 이전 hidden layer의 node를 5개로 지정했으므로, input shape에 대한 정보를 따로 지정하지 않는다.
])

iris_model.summary()

"""# 4. ANN 학습"""

iris_model.compile(optimizer='adam',loss='categorical_crossentropy',metrics=['acc'])
# compile(optimizer, loss, metrics)
# * optimizer: cost(loss) function의 최소값을 찾는 방법 (RMSProp, adam, adaDelta 등)
#              default는 RMSProp이며, adam을 가장 많이 사용함
# * loss: cost(loss) function
#         classification 문제에서 학습에 사용되는 y가 One-hot-encoding 된 경우, 일반적으로 categorical_crossentropy를 사용
#         y가 One-hot-encoding이 아닌 값이 정수인 1열의 data일 경우, sparse_categorical_crossentropy를 사용
#         y가 2개의 class로 구성된 경우, binary_crossentropy를 사용
# * metrics: 학습과정에서 확인하는 성능 평가 척도

# fit(X,y,epochs,batch_size,validation_split)
# 1. X,y: 학습데이터
# 2. epochs: 학습과정에서 학습데이터 전체를 1회 반영 = 1 epoch
# 3. batch_size: 학습 과정에서 그룹핑할 데이터의 수 (1~sample의 수)
#                1 - 개별 데이터에 대한 loss에 대해 update 함 (1 epoch에 데이터의 수만큼 w와 b가 업데이트 됨) Stochastic grandient descent
#                sample의 수 - 모든 데이터에 대한 loss에 대해 update 함 (1 epoch에 1회 w와 b가 업데이트 됨) Batch gradient descent
#                1과 sample의 수 사이의 값 - mini Batch gradient descent
# 4. validation_split: 입력된 학습 데이터 중 일부를 결과 검증에 사용함 (0~1 사이의 값)

ep = 500
batch = 32
val_ratio = 0.2

learning_result = iris_model.fit(X_train, y_train,
                                 epochs = ep,
                                 batch_size = batch,
                                 validation_split = val_ratio)

"""# 5. 성능 시각화"""

plt.plot(learning_result.history['acc'])
plt.plot(learning_result.history['val_acc'])
plt.legend(['training data accuracy','validation data accuracy'])
plt.xlabel('epochs')
plt.ylabel('accuracy')

plt.plot(learning_result.history['loss'])
plt.plot(learning_result.history['val_loss'])
plt.legend(['training data loss','validation data loss'])
plt.xlabel('epochs')
plt.ylabel('loss')

"""# 6. test data 성능 평가"""

test_loss, test_acc = iris_model.evaluate(X_test,y_test)
print('Test Loss: ', test_loss)
print('Test Accuracy: ', test_acc)