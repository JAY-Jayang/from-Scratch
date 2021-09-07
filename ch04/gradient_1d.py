# coding: utf-8
import numpy as np
import matplotlib.pylab as plt


def numerical_diff(f, x): # 중앙 차분 || 중심 차분 을 이용한 수치미분 -> 오차를 줄여줌
    h = 1e-4 # 0.0001
    return (f(x+h) - f(x-h)) / (2*h)

def numerical_diff_1(f, x):
    h = 1e-4
    return (f(x+h) - f(x)) / h


def function_1(x):
    return 0.01*x**2 + 0.1*x 


def tangent_line(f, x, mode = 'middle'):
    
    if mode == 'middle':
        d = numerical_diff(f, x)
        print(d)
        y = f(x) - d*x
        return lambda t: d*t + y

    elif mode == 'standard':
        d = numerical_diff_1(f, x)
        print(d)
        y = f(x) - d*x
        return lambda t: d*t + y  # 함수 안의 함수를 만들어 줌 t에 대한 함수

     
x = np.arange(0.0, 20.0, 0.1)
y = function_1(x)
plt.xlabel("x")
plt.ylabel("f(x)")

tf = tangent_line(function_1, 5)
y2 = tf(x)

plt.plot(x, y)
plt.plot(x, y2)
plt.show()

# tf = tangent_line(function_1, 5, mode = 'standard')
# y2 = tf(x)
# plt.plot(x,y)
# plt.plot(x,y2)
# plt.show()


