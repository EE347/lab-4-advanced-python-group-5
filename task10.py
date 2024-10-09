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

plt.plot(x, META, color= 'blue')
plt.plot(x, AAPL, color = 'black')
plt.plot(x, AMZN, color = 'gray')
plt.plot(x, NFLX, color = 'red')
plt.plot(x, NVDA, color = 'green')
plt.plot(x, GOOGL, color = 'yellow')

plt.xlabel('Dates')
plt.ylabel('Price (USD)')
plt.legend(loc = "upper left")

plt.show()