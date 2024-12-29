from pathlib import Path
import csv
from datetime import datetime
import matplotlib.pyplot as plt

path = Path('weather_data/sitka_weather_2021_simple.csv')
lines = path.read_text().splitlines()

reader = csv.reader(lines)
header_row = next(reader)

dates, highs, lows= [], [], []
for row in reader:
    current_date = datetime.strptime(row[2], '%Y-%m-%d')
    high = int(row[4])
    low = int(row[5])
    dates.append(current_date)
    highs.append(high)
    lows.append(low)

plt.style.use('seaborn-v0_8')
fig, ax = plt.subplots()

ax.plot(dates, highs, color= 'red')
ax.plot(dates, lows, color= 'blue')
ax.fill_between(dates,highs,lows,facecolor='blue',alpha = 0.5)

ax.set_title("Daily High and Low Temperatures, 2021", fontsize=24)
ax.set_xlabel('Date', fontsize=16)
ax.set_ylabel("Temperature (F)", fontsize=16)
ax.tick_params(labelsize=16)

fig.autofmt_xdate()
plt.grid(True)

plt.show()