import csv
from datetime import datetime
import matplotlib.pyplot as plt


def load_data(filename, date_col=2, max_col=6):
    """Load dates and closing prices from a CSV file."""
    dates, highs = [], []
    with open(filename) as f:
        reader = csv.reader(f)
        header_row = next(reader)  # skip header
        for row in reader:
            try:
                current_date = datetime.strptime(row[date_col], '%Y-%m-%d')
                max_temp = int(row[max_col])
            except ValueError:
                # skip bad rows
                continue
            else:
                dates.append(current_date)
                highs.append(max_temp)
    return dates, highs


files = {
    "Sitka": ("sitka_weather_2018_simple.csv", "blue"),
    "Valley": ("death_valley_2018_full.csv", "red"),
}

plt.style.use('seaborn-v0_8')
fig, ax = plt.subplots()

# Plot each dataset
for location, (file, color) in files.items():
    dates, highs = load_data(file)
    ax.plot(dates, highs, label=location, color=color, alpha=0.7)

# Format plot
ax.set_title("Sitka Alaska & Death Valley Temp Highs -- 2018", fontsize=20)
ax.set_xlabel("Date", fontsize=14)
ax.set_ylabel("Temperature (F)", fontsize=14)
fig.autofmt_xdate()
ax.tick_params(axis='both', which='major', labelsize=12)

plt.show()