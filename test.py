import numpy as np
import time

def dot(n):
    times = []
    for i in range(10):
      a = np.random.rand(n,n,n)
      b = np.random.rand(n,n,n)
      t0 = time.time()
      c = np.dot(a, b)
      t1 = time.time()
      times.append(t1 - t0)
    print("Dot product test: %fs"% (sum(times) / len(times)),",n="+str(n))

def resize():
    times = []
    t0 = time.time()
    a = np.random.rand(100000000)
    for i in range(100):
      b = np.resize(a, (1000,200,500))
    t1 = time.time()
    print("Resize test: %fs"% (t1 - t0))

resize()
dot(90)