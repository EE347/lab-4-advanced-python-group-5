import csv
import matplotlib.pyplot as plt
import numpy as np
from datetime import datetime

x = []
META = []
AAPL =[]
AMZN = []
NFLX = []
NVDA = []
GOOGL = []
with open('task9.csv', 'r') as csvfile:
    reader = csv.reader(csvfile)
    headers = next(reader)

    for row in reader:
        x.append(row[0])
        META.append(float(row[1]))
        AAPL.append(float(row[2]))
        AMZN.append(float(row[3]))
        NFLX.append(float(row[4]))
        NVDA.append(float(row[5]))
        GOOGL.append(float(row[6]))

plt.plot(x, META, color= 'blue', label = 'META +184.22%')
plt.plot(x, AAPL, color = 'black', label = 'APPL +126.56%')
plt.plot(x, AMZN, color = 'gray', label = 'AMZN +141.12%')
plt.plot(x, NFLX, color = 'red', label = 'NFLX +193.34%')
plt.plot(x, NVDA, color = 'green', label = 'NVDA +290.15%' )
plt.plot(x, GOOGL, color = 'yellow', label = 'GOOGL +119.06%')

xlabs = ['2023-11', '2024-01', '2024-03','2024-05','2024-07','2024-09']
xtick = ['01/11/2023','02/01/2024','01/03/2024','01/05/2024', '01/07/2024', '01/09/2024']

plt.xlabel('Dates')
plt.ylabel('Price (USD)')
plt.legend(loc = "upper left")
plt.xticks(xtick,xlabs)

plt.show()