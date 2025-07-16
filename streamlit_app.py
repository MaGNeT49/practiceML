import pandas as pd
import streamlit as st

def main():
    df = pd.read_csv("table.csv")

    st.title("Трилобиты")

    st.sidebar()
    st.dataframe(df)

if __name__ == "main":
    main()
