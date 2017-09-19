import numpy as np
import matplotlib
import matplotlib.pyplot as plt
import time

# Time an arbitrary functiion
def time_f(f,*args):
    t0 = time.time()
    f(*args)
    return time.time() - t0

# Iterating function
def m(z,c):
    return z*z + c

# Detmerine if item belongs in set
def in_set(c,N):
    z = c
    n = 0
    for n in range(1,N):
        if np.abs(z) > 2:
            break 
        z = m(z,c)
    return n 

# Calculates the set directly using vectorized operations
def vectorized_mendelbrot(N):
    x = np.linspace(-2,2,N)*np.ones((N,N))
    y = np.transpose(np.linspace(-2,2,N)*np.ones((N,N)))
    c = x + 1j*y
    return np.vectorize(in_set)(c,N)


# Creates the set by individually checking each value
# in half the set and setting the points so they are symmetric
# across y = 0
def reduced_mendelbrot(N):
    x = np.linspace(-2,2,N)*np.ones((N//2,N))
    y = np.transpose(np.linspace(-2,0,N//2)*np.ones((N,N//2)))
    c = x + 1j*y
    m = np.zeros((N,N))
    for nx in range(N//2-1):
        for ny in range(N):
            r = in_set(c[nx,ny],N)
            m[nx,ny] = r 
            m[N-1-nx,ny] = r 
    return m

# Creates the set using vectorized operations on
# half the y space and reflects the results along the y = 0
def vectorized_reduced_mendelbrot(N):
    x = np.linspace(-2,2,N)*np.ones((N//2,N))
    y = np.transpose(np.linspace(-2,0,N//2)*np.ones((N,N//2)))
    _m = np.vectorize(in_set)(x + 1j*y,N)
    m = np.zeros((N-1,N))
    m[:N//2] = _m
    m[N//2-1:] = _m[::-1]
    return m

# Method to quickly switch between various generating methods
def mendelbrot(N,f=vectorized_reduced_mendelbrot):
    return f(N)

# Method to handle runn
def _plot_mendel(M,N,cmap='Greys'):
    img = plt.imshow(M,cmap=cmap,interpolation="nearest")
    plt.set_title('N = '+str(N))
    plt.colorbar(img)

# Method to simply plot and show the set
def plot_mendel(N,cmap='Greys'):
    M = mendelbrot(N)
    _plot_mendel(M,N,cmap)
    plt.show()

# Method to plot and show 4 values of N 
def four_plot(cmap="Greys",title=""):
    n = [10,100,500,1000]
    fig,ax = plt.subplots(2,2)
    for i,N in enumerate(n):
        img = ax[i//2,i%2].imshow(np.log(mendelbrot(N)),cmap=cmap,interpolation="nearest")
        ax[i//2,i%2].set_title("N ="+str(N))
        ax[i//2,i%2].set_xticks([0,N//2,N])
        ax[i//2,i%2].set_xticklabels([-2,0,2])
        ax[i//2,i%2].set_yticks([0,N//2,N])
        ax[i//2,i%2].set_yticklabels([-2,0,2])
    plt.savefig("four_plot"+title)

# Method to plot and save plot of the set 
def save_mendel(N,cmap='Greys',fname=''):
    M = mendelbrot(N)
    _plot_mendel(M,N,cmap)
    plt.savefig(fname+"N"+str(N)+".png")

# Method to plot time dependance on N
def time_vs_N():
    N = np.arange(1,500)
    T = np.vectorize(time_m)(N)
    plt.plot(N,T)
    plt.show()

# Method to compare times for various methods
def time_all_versions():
    N = np.arange(10,50,10)
    F = [vectorized_mendelbrot,reduced_mendelbrot,vectorized_reduced_mendelbrot]
    T = []
    i = 1
    for f in F:
        def _time_m(N):
            t0 = time.time()
            f(N)
            return time.time() - t0
        T = np.vectorize(_time_m)(N)
        plt.plot(N,T,label='Method '+str(i))
        print(i,f)
        i += 1
    plt.plot(N,[n**3 for n in N],'k--',label='N^3') 
    plt.plot(N,[n**3/2 for n in N],color='grey',linestyle='--',label='N^3/2') 
    plt.legend(loc='upper left')
    plt.savefig('time_vs_method.png')
    plt.show()

four_plot(cmap='jet',title='color')
