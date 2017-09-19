import matplotlib.pyplot as plt
import numpy as np

def read_data():
    x,y = [],[]
    with open('millikan.txt','r') as f:
        for line in f:
            _x,_y = map(float,line.split())
            x.append(_x)
            y.append(_y)
    x = np.array(x)
    y = np.array(y)
    return x,y

def least_square(x,y):
    N = len(x)
    ex = np.sum(x)/N
    exx = np.sum(x*x)/N
    ey = np.sum(y)/N
    exy = np.sum(x*y)/N
    d = (exx - ex*ex)
    m = (exy - ex*ey)/d
    c = (exx*ey - ex*exy)/d
    return m,c 

x,y = read_data()
m,c = least_square(x,y)

# Constants
# Electron Charge
elec = 1.602e-19  # C
# Accepted value of planck constant
h_acc = 6.626070040e-34  # J/s

h = m*elec
print("Accepted Value:    h =",h_acc)
print("Value from fit:    h =",h)
print("Percent  error: %err =",(h_acc-h)/h_acc*100,"%")


plt.plot(x,y,'bo')
plt.xlabel('$\\nu$ (Hz)')
plt.ylabel('V (volt)')
plt.savefig('reg_a.png')
plt.plot(x,[m*xi+c for xi in x],'g-')
plt.savefig('reg.png')
plt.show()
