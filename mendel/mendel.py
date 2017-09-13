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
            return n 
        z = m(z,c)
    return n

def mendelbrot(N):
    x = np.linspace(-2,2,N)*np.ones((N,N))
    y = np.transpose(np.linspace(-2,2,N)*np.ones((N,N)))
    c = x + 1j*y
    return np.vectorize(in_set)(c,N)

def time_m(N):
    t0 = time.time()
    mendelbrot(N)
    return time.time() - t0

def _plot_mendel(N,cmap='Greys'):
    img = plt.imshow(mendelbrot(N),cmap=cmap,interpolation="nearest")
    plt.annotate('N = '+str(N),
		xy=(0, 0), xycoords='data',
		xytext=(.8, .05), textcoords='axes fraction',
		bbox=dict(boxstyle="round", fc="0.9"))
    plt.colorbar(img)
    
def plot_mendel(N,cmap='Greys'):
    _plot_mendel(N,cmap)
    plt.show()

def save_mendel(N,cmap='Greys',fname=''):
    _plot_mendel(N,cmap)
    plt.savefig(fname+"N"+str(N)+".png")

def time_vs_N():
    N = np.arange(1,500)
    T = np.vectorize(time_m)(N)
    plt.plot(N,T)
    plt.show()

n = [500]#[10,100,500,1000]
for N in n:
    save_mendel(N,cmap='jet',fname='color_')
