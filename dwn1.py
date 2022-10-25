import csv
from datetime import datetime
from matplotlib import pyplot as plt
highs=[]
dates=[]
with open('cx.csv', newline='') as csvfile:
    reader = csv.DictReader(csvfile)
    for row in reader:
        highs.append(int(row['Max TemperatureF']))
        x=datetime.strptime(row['AKDT'],'%m/%d/%Y')
        dates.append(x)


print(highs)
print(len(highs))
fig=plt.figure(dpi=128,figsize=(10,16))
plt.title('Daily High temperature',fontsize='24')
plt.ylabel('temperature',fontsize='16')
plt.tick_params(axis='both',which='major',labelsize='6')
fig.autofmt_xdate()
plt.plot(dates,highs,c='red')
plt.show()
