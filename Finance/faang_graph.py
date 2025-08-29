import csv
from datetime import datetime
import matplotlib.pyplot as plt


def load_data(filename, date_col=0, price_col=4):
    """Load dates and closing prices from a CSV file."""
    dates, prices = [], []
    with open(filename) as f:
        reader = csv.reader(f)
        header_row = next(reader)  # skip header
        for row in reader:
            try:
                current_date = datetime.strptime(row[0][:10], '%Y-%m-%d')
                price = float(row[price_col])
            except ValueError:
                # skip bad rows
                continue
            else:
                dates.append(current_date)
                prices.append(price)
    return dates, prices


# Load data for each FANG stock
files = {
    "Google": ("google_dataset.csv", "purple"),
    "Apple": ("apple_dataset.csv", "green"),
    "Amazon": ("amazon_dataset.csv", "orange"),
    "Netflix": ("netflix_dataset.csv", "red"),
    "Meta": ("meta_dataset.csv", "blue"),
}

plt.style.use('seaborn-v0_8')
fig, ax = plt.subplots()

# Plot each dataset
for company, (file, color) in files.items():
    dates, prices = load_data(file)
    ax.plot(dates, prices, label=company, color=color, alpha=0.7)

# Format plot
ax.set_title("Finance Closing Prices (Last 10 Years)", fontsize=20)
ax.set_xlim(datetime(2015, 1, 1), datetime.now())
ax.set_xlabel("Date", fontsize=14)
ax.set_ylabel("Closing Price ($)", fontsize=14)
fig.autofmt_xdate()
ax.tick_params(axis='both', which='major', labelsize=12)
ax.legend()  # <-- adds company labels

plt.show()
