from pathlib import Path
import csv
from datetime import datetime
import matplotlib.pyplot as plt

# Load the CSV
path = Path('san_francisco_weather.csv')
lines = path.read_text().splitlines()
reader = csv.reader(lines)

# Skip header row
header_row = next(reader)

# Column indexes
DATE_COL = 1    # second column
TMAX_COL = 2    # third column
TMIN_COL = 3    # fourth column

# Extract dates, highs, and lows
dates, highs, lows = [], [], []
for row in reader:
    try:
        # Take only the first 10 characters of date string in case there's time info
        current_date = datetime.strptime(row[DATE_COL][:10], '%Y-%m-%d')
        high = float(row[TMAX_COL])
        low = float(row[TMIN_COL])
    except ValueError:
        print(f"Missing or invalid data for row: {row}")
        continue
    else:
        dates.append(current_date)
        highs.append(high)
        lows.append(low)

# Plot the high and low temperatures
plt.style.use('seaborn-v0_8')
fig, ax = plt.subplots()
ax.plot(dates, highs, color='red', alpha=0.5, label='Highs')
ax.plot(dates, lows, color='blue', alpha=0.5, label='Lows')
ax.fill_between(dates, highs, lows, facecolor='blue', alpha=0.1)

# Format plot
ax.set_title("San Francisco Highs/Lows", fontsize=20)
fig.autofmt_xdate()
ax.set_ylabel("Temperature (F)", fontsize=16)
ax.tick_params(labelsize=16)
ax.legend()

plt.show()
