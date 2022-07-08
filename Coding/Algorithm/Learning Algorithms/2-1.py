import numpy as np
from scipy.optimize import curve_fit


def linear_model(n, a, b):
    return a*n+b


xs = [100, 1000, 10000]
ys = [0.063, 0.565, 5.946]

# 첫 번째 인자로 계수가 반환된다.
[(a, b), _] = curve_fit(linear_model, np.array(xs), np.array(ys))
print('Linear = {}*N + {}'.format(a, b))
