import pandas
import matplotlib.pyplot as plt
from mpl_toolkits.basemap import Basemap, cm
import numpy as np

df = pandas.read_csv("table.csv")

ages_mean = ((df['max_age_mya'] + df['min_age_mya']) / 2).to_list()

lons = df["longitude"]
lats = df["latitude"]

parallels = np.arange(-90,90,30)
meridians = np.arange(0,360,30)

map = Basemap(projection="mill", lon_0=0)

x, y = map(lons, lats)

map.drawparallels(parallels, linewidth=0.5)
map.drawmeridians(meridians, linewidth=0.5)
map.drawcoastlines(linewidth=0.25)
map.drawcountries(linewidth=0.25)
map.drawmapboundary(fill_color="#5cd4d4")

map.fillcontinents(color="#c7765e", lake_color="#5cd4d4")

map.scatter(x, y, 0.1, c=ages_mean, cmap="viridis", alpha=0.7)

plt.colorbar(location="bottom", label='Средней возраст\n окаменелостей в миллионах лет')

plt.title("Координаты раскопок окаменелостей трилобитов")
plt.show()