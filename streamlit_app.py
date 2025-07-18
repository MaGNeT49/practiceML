import pandas as pd
import streamlit as st
import matplotlib.pyplot as plt
from mpl_toolkits.basemap import Basemap, cm
import numpy as np

def main():
    df = pd.read_csv("table.csv")
    st.title("Трилобиты")
    st.dataframe(df)

    st.pyplot(showMap(df))


def showMap(data):
    # max_age_mya = data['max_age_mya']

    # lons = data["longitude"]
    # lats = data["latitude"]

    # parallels = np.arange(-90,90,30)
    # meridians = np.arange(0,360,30)

    # map = Basemap(projection="mill", lon_0=0)

    # x, y = map(lons, lats)

    # map.drawparallels(parallels, linewidth=0.5, labels=[1, 0, 0, 0], fontsize=4)
    # map.drawmeridians(meridians, linewidth=0.5, labels=[0, 0, 0, 1], fontsize=4)
    # map.drawcoastlines(linewidth=0.25)
    # map.drawcountries(linewidth=0.25)
    # map.drawmapboundary(fill_color="#5cd4d4")

    # map.fillcontinents(color="#c7765e", lake_color="#5cd4d4")

    # map.scatter(x, y, 0.1, marker='o', c=max_age_mya, cmap="viridis")

    # plt.title("Координаты раскопок окаменелостей трилобитов")
    # plt.colorbar(location="bottom", label='Средней возраст\n окаменелостей в миллионах лет')
    # plt.scatter(x, y, 0.1, marker='o', c=ages_mean, cmap="viridis")

    # fig, axes = plt.subplot()

    # axes.scatter(x, y, 0.1, marker='o', c=max_age_mya, cmap="viridis")
    # axes.colorbar(location="bottom", label='Средней возраст\n окаменелостей в миллионах лет')
    # axes.title("Координаты раскопок окаменелостей трилобитов")
    
    arr = np.random.normal(1, 1, size=100)
    fig, ax = plt.subplots()
    ax.scatter(arr, arr)

    return fig


if __name__ == "__main__":
    main()
