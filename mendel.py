import numpy as np
import matplotlib
import matplotlib.pyplot as plt
import matplotlib.animation as plta 
import time


def m(z,c):
    return z*z + c

def in_set(c,N):
    z = c
    for n in range(1,N):
        if np.abs(z) > 2:
            return 0 
        z = m(z,c)
    return 1

def mendelbrot(N):
    x = np.linspace(-2,2,N)*np.ones((N,N))
    y = np.transpose(np.linspace(-2,2,N)*np.ones((N,N)))
    c = x + 1j*y
    return np.vectorize(in_set)(c,N)

def time_m(N):
    t0 = time.time()
    mendelbrot(N)
    return time.time() - t0

def plot_mendel(N):
    plt.imshow(mendelbrot(N),cmap="Greys",interpolation="nearest")
    plt.annotate('N = '+str(N),
		xy=(0, 0), xycoords='data',
		xytext=(.85, .05), textcoords='axes fraction',
		bbox=dict(boxstyle="round", fc="0.9"))
    plt.show()

def time_vs_N():
    N = np.arange(1,500)
    vf = np.vectorize(time_m)
    T = vf(N)
    plt.plot(N,T)
    plt.show()

N = 1000
plot_mendel(N)
