import numpy as np
import matplotlib.pyplot as plt

def f(x):
    a = x**6 + 3*x**5 + 4*x**4 + 1/3*x**3 + 2*x**2 + x - 10
    return a

def T_0(x):
    return 1
def T_1(x):
    return x
def T_2(x):
    return 2*x**2-1
def T_3(x):
    return 4*x**3-3*x
def T_4(x):
    return 8*x**4-8*x**2+1
def T_5(x):
    return 16*x**5-20*x**3+5*x

x = np.arange(-1, 3, 0.001)
y1 = []
y2 = []
y3 = []
for i in x:
    y1.append(f(i))
    y2.append(-7.18750* T_0(i) +  3.12500* T_1(i) +   3.43750* T_2(i) +  0.83333* T_3(i))
    y3.append(-7.18750* T_0(i) +  3.12500* T_1(i) +  3.46875* T_2(i) +  1.02083* T_3(i) +  0.68750* T_4(i) +  0.18750* T_5(i))

plt.plot(x, y1, label="f(x)")
plt.plot(x, y2, label="S_3(x)")
plt.plot(x, y3, label="S_5(x)")
plt.grid()
plt.legend()
plt.show()