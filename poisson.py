import random
import math
import pandas as pd
import matplotlib.pyplot as plt

def fact(n):
    c = 1
    for i in range(1, n + 1):
        c *= i
    return c

def poisson(a, b):
    e = math.exp(-a)
    q = math.pow(a, b)
    num = e * q
    den = fact(b)
    return num / den

if __name__ == "__main__":
    p = []
    for i in range(21):
        p.append(poisson(1, i))
    
    
x = ["0","1","2","3","4","5","6","7","8","9","10"]
y = [p[0],p[1],p[2],p[3],p[4],p[5],p[6],p[7],p[8],p[9],p[10]]

plt.bar(x,y,label="Bars 1",color="black")

plt.xlabel("i")
plt.ylabel("Px(i)")
plt.title("Poisson(1)")
plt.legend()
plt.show()
