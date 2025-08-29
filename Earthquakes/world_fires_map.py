import csv
import plotly.express as px

filename = 'world_fires_1_day.csv'

LAT_COL = 0
LON_COL = 1
BRIGHT_COL = 2
DATE_COL = 5

# Load data from csv file
lats, lons, brights = [], [], []
with open(filename) as f:
    reader = csv.reader(f)
    header_row = next(reader)
    for row in reader:
        try:
            lat = float(row[LAT_COL])
            lon = float(row[LON_COL])
            bright = float(row[BRIGHT_COL])
        except ValueError:
            continue  # skip bad rows
        lats.append(lat)
        lons.append(lon)
        brights.append(bright)

# Plot the fires
title = "World Fires on April 3rd, 2022"
fig = px.scatter_geo(
    lat=lats,
    lon=lons,
    size=brights,
    color=brights,
    color_continuous_scale="Hot",
    size_max=10,
    projection="orthographic",
    title=title
)

fig.show()