import time
import tra_lopputyo
import math
import matplotlib.pyplot as plt
import numpy as np
from scipy import optimize


def calculate_runtime(n):
    if n == 10:
        start_time = time.time()
        tra_lopputyo.run(f'./testidata/graph_testdata/graph_ADS2018_{n}_1.txt')
        runtime = time.time() - start_time
    else:
        start_time = time.time()
        tra_lopputyo.run(f'./testidata/graph_testdata/graph_ADS2018_{n}.txt')
        runtime = time.time() - start_time

    return runtime


def calculate_large_runtime(n):

    start_time = time.time()
    tra_lopputyo.run(f'./testidata/graph_large_testdata/graph_ADS2018_{n}.txt')
    runtime = time.time() - start_time

    return runtime


def fitted_function(x, a, b, c):
    return a + b*x + c*x**2


if __name__ == "__main__":
    size = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100]
    runtime = []

    large_size = [200, 300, 500, 750, 1000, 1500, 2000]
    large_runtime = []

    for n in size:
        runtime.append(calculate_runtime(n))

    for n in large_size:
        large_runtime.append(calculate_large_runtime(n))

    params, params_covariance = optimize.curve_fit(
        fitted_function, np.ndarray(size + large_size), np.ndarray(runtime + large_runtime))

    #plt.plot(size + large_size, runtime + large_runtime)
    plt.plot(size, fitted_function(size, params[0], params[1], params[2]))
    plt.show()
    print(runtime)
    print(large_runtime)
