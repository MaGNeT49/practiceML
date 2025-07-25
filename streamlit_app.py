import pandas as pd
import streamlit as st
import altair as alt
import plotly.express as px
import joblib
from sklearn.model_selection import train_test_split
import shap
import catboost
import matplotlib.pyplot as plt


def main():
    st.set_page_config(layout="wide", page_title="Анализ времени на трилобитах")

    st.title("Шаталов Илья Андреевич, 2023-ФГиИБ-ПИ-1б, 25 вариант: Трилобиты.")

    mapTab, shapTab, metricTab, dataTab = st.tabs(["Карта трилобитов", "SHAP анализ и результаты обучения модели", "Метрики модели", "Исходные данные"])

    @st.cache_data
    def load_data():
        return pd.read_csv("table_clear.csv")
    
    @st.cache_data
    def load_model():
        model = joblib.load('trilobite_age_predictor_new.pkl')

        return model
    
    def load_metric():
        return pd.read_csv("metrics.csv")
    
    df = load_data()
    
    model = load_model()
    
    features = ['order_num_scaled', 'diet_scaled', 'presevation_mode_count_scaled', 'country_scaled']
    target = "max_age_mya"
    
    X = df[features]
    y = df[target]
    
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
    
    with mapTab:
        col1, col2 = st.columns(2)
        
        with col1:
            map = getFigureMap(df)

            st.plotly_chart(map)

    
    with shapTab:
        col1, col2 = st.columns(2)
        
        with col1:
            st.subheader("Важность признаков")
            
            explainer = shap.Explainer(model)
            shap_values = explainer(X_test)

            fig1 = plt.figure(figsize=(6, 4))
            
            shap.summary_plot(shap_values, X_test, plot_type="bar")
            plt.tight_layout()
            st.pyplot(fig1)
        
        with col2:
            st.subheader("SHAP-анализ")
            
            explainer = shap.Explainer(model)
            shap_values = explainer(X_test)
            
            fig2 = plt.figure(figsize=(6, 4))
            
            shap.summary_plot(shap_values, X_test)
            plt.tight_layout()
            st.pyplot(fig2)
    
    with metricTab:
        st.subheader("Оценка качества модели")
        col1, col2, col3, col4, col5 = st.columns(5)
        
        metric = load_metric()
        
        r2_value = metric[0:1].values.tolist()[0][1]
        mae_value = metric[1:2].values.tolist()[0][1]
        max_error_value = metric[2:3].values.tolist()[0][1]
        med_abs_proc_error = metric[3:4].values.tolist()[0][1]
        MSE = metric[4:5].values.tolist()[0][1]
        
        col1.metric("R² (Коэф. детерминации)", f"{r2_value:.2f}")
        col2.metric("MAE (Средняя ошибка)", f"{mae_value:,.2f}")
        col3.metric("Max Error", f"{max_error_value:,.2f}")
        col4.metric("Медианная абсолютная процентная ошибка", f"{med_abs_proc_error:,.3f}%")
        col5.metric("MSE", f"{MSE:,.2f}")
        
    with dataTab:
        st.dataframe(df)


def getFigureMap(df):
    fig = px.scatter_map(df, 
                         lat="latitude", 
                         lon="longitude", 
                         color="max_age_mya", 
                         hover_name="scientific_name", 
                         hover_data=["country"], 
                         zoom=1, 
                         color_continuous_scale="viridis")


    return fig

if __name__ == "__main__":
    main()
