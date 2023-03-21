import numpy as np
import time
import matplotlib.pyplot as plt
import sys
from mpi4py import MPI

A = np.array([[1,1],[2,2]])

aaa = np.shape(A)

test = aaa[1]

print(np.shape(A)[1])