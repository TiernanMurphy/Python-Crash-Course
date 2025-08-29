import csv
from datetime import datetime

import matplotlib.pyplot as plt

filename = 'sitka_weather_2018_simple.csv'
with open(filename) as f:
    reader = csv.reader(f)
    header_row = next(reader)

    # Get rain from dataset
    dates, rainfall = [], []
    for row in reader:
        current_date = datetime.strptime(row[2], '%Y-%m-%d')
        dates.append(current_date)
        rain = float(row[3])
        rainfall.append(rain)

    print(rainfall)

    for index, column_header in enumerate(header_row):
        print(index, column_header)

    print(header_row)

# Plot the high and low temperatures
plt.style.use('seaborn-v0_8')
fig, ax = plt.subplots()
ax.plot(dates, rainfall, c='blue', alpha=0.5)

# Format plot
plt.title("Sitka Rainfall - 2018", fontsize=24)
plt.xlabel('', fontsize=16)
fig.autofmt_xdate()
plt.ylabel("Inches", fontsize=16)
plt.tick_params(axis='both', which='major', labelsize=16)

plt.show()
