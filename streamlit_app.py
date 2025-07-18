import pandas as pd
import streamlit as st
import matplotlib.pyplot as plt
from mpl_toolkits.basemap import Basemap, cm
import numpy as np
import altair as alt
from vega_datasets import data
import geopandas as gpd


def main():
    df = pd.read_csv("table.csv")
    st.title("Трилобиты")
    st.dataframe(df)

    #map = showMap(df)

    #st.altair_chart(map)


def showMap(df):
    data = df
    # gdf_world = gpd.read_file(data.world_110m.url, driver="TopoJSON")

    # defintion for interactive brush
    brush = alt.selection_interval(
        encodings=["longitude"],
        empty=False,
        value={"longitude": [-50, -110]}
    )

    # world disk
    sphere = alt.Chart(alt.sphere()).mark_geoshape(
        fill="transparent", stroke="lightgray", strokeWidth=1
    )

    # # countries as shapes
    # world = alt.Chart(data).mark_geoshape(fill="lightgray", stroke="white", strokeWidth=0.1)

    quakes = alt.Chart(data).transform_calculate(
    lon="longitude",
    lat="latitude",
).mark_circle(opacity=0.35, tooltip=True).encode(
    longitude="lon:Q",
    latitude="lat:Q",
    color=alt.when(brush).then(alt.value("goldenrod")).otherwise(alt.value("steelblue")),
    size=alt.Size("mag:Q").scale(type="pow", range=[1, 1000], domain=[0, 7], exponent=4),
).add_params(brush)

    return quakes

if __name__ == "__main__":
    main()
