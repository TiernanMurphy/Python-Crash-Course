import csv
from datetime import datetime

import matplotlib.pyplot as plt

filename = 'sitka_weather_2018_simple.csv'
with open(filename) as f:
    reader = csv.reader(f)
    header_row = next(reader)

    # Column indexes
    DATE_COL = 2
    TMAX_COL = 5
    TMIN_COL = 6

    # Get dates and high/low temperatures from this file
    dates, highs, lows = [], [], []
    for row in reader:
        current_date = datetime.strptime(row[DATE_COL], '%Y-%m-%d')
        high = int(row[TMAX_COL])
        low = int(row[TMIN_COL])
        dates.append(current_date)
        highs.append(high)
        lows.append(low)

    print(highs)

    for index, column_header in enumerate(header_row):
        print(index, column_header)

    print(header_row)

# Plot the high and low temperatures
plt.style.use('seaborn-v0_8')
fig, ax = plt.subplots()
ax.plot(dates, highs, c='red', alpha=0.5)
ax.plot(dates, lows, c='blue', alpha=0.5)
plt.fill_between(dates, highs, lows, facecolor='blue', alpha=0.1)

# Format plot
plt.title("Sitka Daily Highs/Lows - 2018", fontsize=24)
plt.xlabel('', fontsize=16)
fig.autofmt_xdate()
plt.ylabel("Temperature (F)", fontsize=16)
plt.tick_params(axis='both', which='major', labelsize=16)

plt.show()
