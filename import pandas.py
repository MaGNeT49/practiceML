import pandas
import matplotlib.pyplot as plt
from mpl_toolkits.basemap import Basemap, cm
import numpy as np

df = pandas.read_csv("table.csv")

import plotly.express as px

fig = px.scatter(df, x="max_age_mya", y="min_age_mya", color="country")
fig.show()