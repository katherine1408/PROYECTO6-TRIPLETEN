import pandas as pd
import streamlit as st
import plotly.express as px 

car_data = pd.read_csv('vehicles_us.csv') # leer los datos

print(car_data.head())

hist_checkbox = st.checkbox('Mostrar histograma de kilometraje')

if hist_checkbox:
    # Mensaje y creación del histograma
    st.write('Creación de un histograma para el conjunto de datos de anuncios de venta de coches')
    fig_hist = px.histogram(car_data, x="odometer")
    st.plotly_chart(fig_hist, use_container_width=True)
    
# Casilla de verificación para el gráfico de dispersión
scatter_checkbox = st.checkbox('Mostrar gráfico de dispersión precio vs. kilometraje')

if scatter_checkbox:
    # Mensaje y creación del gráfico de dispersión
    st.write('Creación de un gráfico de dispersión de precio vs. kilometraje')
    fig_scatter = px.scatter(car_data, x="odometer", y="price", title="Precio vs. Kilometraje")
    st.plotly_chart(fig_scatter, use_container_width=True)
    


