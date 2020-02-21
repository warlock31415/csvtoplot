import csv
import matplotlib.pyplot as plt
import numpy as np

with open('test.csv', encoding='ascii',errors="surrogateescape") as csvfile:
    data = list(csv.reader(csvfile))   

i=0
while i < len(data):
  data[i] = data[i][0].split(';')
  i += 1

Time = [None]*(len(data)-1) 
index = [None] * (len(data)-1)
Pressure_ProcessGas = [None] * (len(data)-1)

for i in range(1,len(data)-1):
  Time[i] = data[i][0]
  index = int(data[i][1])
  Pressure_ProcessGas = float(data[i][2])

plt.plot(index,Pressure_ProcessGas)
plt.show()

print('AHHHHHHHHHHHHHHHH')