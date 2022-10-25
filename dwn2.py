import csv
from datetime import datetime
from matplotlib import pyplot as plt
highs=[]
lows=[]
dates=[]
with open('sitka_weather_2014.csv', newline='') as csvfile:
    reader = csv.DictReader(csvfile)
    for row in reader:
        highs.append(int(row['Max TemperatureF']))
        x=datetime.strptime(row['AKST'],'%Y-%m-%d')
        dates.append(x)
        lows.append(int(row['Min TemperatureF']))


print(highs)
print(len(highs))
fig=plt.figure(dpi=128,figsize=(10,16))
plt.title('Daily High temperature',fontsize='24')
plt.ylabel('temperature',fontsize='16')
plt.tick_params(axis='both',which='major',labelsize='6')
fig.autofmt_xdate()
plt.plot(dates,highs,c='red')
plt.plot(dates,lows,c='black')
plt.fill_between(dates,highs,lows,facecolor='blue',alpha=0.2)
plt.show()