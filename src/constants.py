import numpy as np

#the system can be imported as a .csv or .txt file
#other constants will be added soon

m = np.loadtxt("system.csv", delimiter=",")
m_txt = np.loadtxt("system.txt", skiprows=0, unpack=True)
G = 6.67408e-11 



