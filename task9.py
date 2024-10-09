import csv
import matplotlib.pyplot as plt
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

plt.plot(x, META)
plt.plot(x, AAPL)
plt.plot(x, AMZN)
plt.plot(x, NFLX)
plt.plot(x, NVDA)
plt.plot(x, GOOGL)

plt.show()