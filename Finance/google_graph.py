import csv
from datetime import datetime

import matplotlib.pyplot as plt

google_file = 'google_dataset.csv'
with open(google_file) as f:
    reader = csv.reader(f)
    header_row = next(reader)

    # Get dates and closing prices from this file
    dates, closing_prices = [], []
    for row in reader:
        current_date = datetime.strptime(row[0], '%Y-%m-%d')
        price = float(row[4])
        dates.append(current_date)
        closing_prices.append(price)

    print(closing_prices)

    for index, column_header in enumerate(header_row):
        print(index, column_header)

    print(header_row)

# Plot closing prices
plt.style.use('seaborn-v0_8')
fig, ax = plt.subplots()
ax.plot(dates, closing_prices, c='purple', alpha=0.5)
# ax.plot(dates, lows, c='blue', alpha=0.5)  // plots second line in blue
# plt.fill_between(dates, highs, lows, facecolor='blue', alpha=0.1) // fills space between two lines

# Format plot
plt.title("Google Closing Prices", fontsize=24)
plt.xlabel('Dates', fontsize=16)
fig.autofmt_xdate()
plt.ylabel("Closing Price ($)", fontsize=16)
plt.tick_params(axis='both', which='major', labelsize=16)

plt.show()
