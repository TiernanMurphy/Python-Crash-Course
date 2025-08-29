import csv
from datetime import datetime
import matplotlib.pyplot as plt

filename = 'seattle-weather.csv'
with open(filename) as f:
    reader = csv.reader(f)
    header_row = next(reader)

    for index, column_header in enumerate(header_row):
        print(index, column_header)

    # Column indexes
    DATE_COL = 0
    TMAX_COL = 2
    TMIN_COL = 3

    # Get dates and high temperatures from this file
    dates, highs, lows = [], [], []
    for row_num, row in enumerate(reader):
        current_date = datetime.strptime(row[DATE_COL], '%Y-%m-%d')
        try:
            high = int(row[TMAX_COL])
            low = int(row[TMIN_COL])
        except ValueError:
            print(f"Missing data for {current_date}")
        else:
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
ax.fill_between(dates, highs, lows, facecolor='blue', alpha=0.1)

# Format plot
plt.title("Seattle Highs and Lows", fontsize=24)
plt.xlabel('', fontsize=16)
fig.autofmt_xdate()
plt.ylabel("Temperature (F)", fontsize=16)
plt.tick_params(axis='both', which='major', labelsize=16)

plt.show()
