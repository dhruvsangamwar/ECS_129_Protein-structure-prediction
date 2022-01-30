import pandas as pd
import pdbCleanup
import numpy as np
from numpy import genfromtxt

my_data = genfromtxt('degrees.csv', delimiter=',')
print(my_data)
