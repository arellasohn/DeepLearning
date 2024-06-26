# -*- coding: utf-8 -*-
"""perceptron.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1-zUSr1UAi1_tQR1h92ktU9yG6jOMZjrg

# 1. Perceptron
"""

# 입력이 2개인 perceptron
def perceptron(x1, x2, w1, w2, b):
    # z가 0보다 같거나 작을 경우, 0을 반환 (return 1)
    # z가 0보다 클 경우, 1을 반환 (return 1)
    z = w1*x1 + w2*x2 + b

    if z <= 0:
        return 0
    else:
        return 1

"""# 2. Perceptron으로 logic gate(AND, NAND, OR) 정의하기"""

def AND(x1, x2):
     # AND는 w1이 2, w2가 3, b가 -4인 perceptron
     y = perceptron(x1, x2, 2, 3, -4)
     return y

def NAND(x1, x2):
     # NAND는 w1이 -5, w2가 -3, b가 7인 perceptron
     y = perceptron(x1, x2, -5, -3, 7)
     return y

def OR(x1, x2):
     # OR는 w1이 3, w2가 3, b가 -2인 perceptron
     y = perceptron(x1, x2, 3, 3, -2)
     return y

print(AND(0, 0))
print(AND(0, 1))
print(AND(1, 0))
print(AND(1, 1))

print(NAND(0, 0))
print(NAND(0, 1))
print(NAND(1, 0))
print(NAND(1, 1))

print(OR(0, 0))
print(OR(0, 1))
print(OR(1, 0))
print(OR(1, 1))

"""# 3. NAND, OR, AND 함수를 이용하여 XOR 함수 정의하기"""

def XOR(x1, x2):
    s1 = NAND(x1, x2)
    s2 = OR(x1, x2)
    y = AND(s1, x2)

    return y

print(XOR(0, 0))
print(XOR(0, 1))
print(XOR(1, 0))
print(XOR(1, 1))