import pandas as pd
import streamlit as st
import altair as alt
import plotly.express as px


def main():
    st.set_page_config(layout="wide", page_title="Анализ времени на трилобитах")

    st.title("Шаталов Илья Андреевич, 2023-ФГиИБ-ПИ-1б, 25 вариант: Трилобиты.")

    mapTab, dataTab = st.tabs(["Карта трилобитов", "Исходные данные"])

    @st.cache_data
    def load_data():
        return pd.read_csv("table.csv")
    
    df = load_data()

    with mapTab:
        map = getFigureMap(df)
        
        st.plotly_chart(map)

    with dataTab:
        st.dataframe(df)


def getFigureMap(df):
    fig = px.scatter_map(df, "latitude", "longitude", "max_age_mya", hover_name="scientific_name", zoom=1, color_continuous_scale=px.colors.carto.Temps)
    # fig.update_traces(cluster=dict(enabled=True))

    return fig

if __name__ == "__main__":
    main()
