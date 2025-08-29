from pathlib import Path
import json

import plotly.express as px


# Read data as a string and convert to a Python object.
path = Path('eq_data_30_day_m1.geojson')
contents = path.read_text(encoding='utf-8')
all_eq_data = json.loads(contents)

# Examine all earthquakes in the dataset.
all_eq_dicts = all_eq_data['features']

mags, lons, lats = [], [], []
for eq_dict in all_eq_dicts:
    mags.append(eq_dict['properties']['mag'])
    lons.append(eq_dict['geometry']['coordinates'][0])
    lats.append(eq_dict['geometry']['coordinates'][1])
    title = eq_dict['properties']['title']

title = all_eq_data['metadata']['title']
print(title)
fig = px.scatter_geo(lat=lats, lon=lons, size=mags, color=mags,
                     color_continuous_scale='Viridis', title=title, size_max=10)
fig.show()
