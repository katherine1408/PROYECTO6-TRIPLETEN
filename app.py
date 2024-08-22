import pandas as pd
import streamlit as st
import plotly.express as px 

car_data = pd.read_csv('vehicles_us.csv') # leer los datos

print(car_data.head())

hist_button = st.button('Construir Histograma')

if hist_button:
    
    st.write('Creación de un histograma con los valores del odometro de los autos')
    fig = px.histogram(car_data,x='odometer')
    st.plotly_chart(fig)
    
scatter_button = st.button('Construir gráfico de dispersión')

if scatter_button:
    # Mensaje y creación del gráfico de dispersión
    st.write('Creación de un gráfico de dispersión de precio vs. kilometraje')
    fig_scatter = px.scatter(car_data, x="odometer", y="price", title="Precio vs. Kilometraje")
    st.plotly_chart(fig_scatter, use_container_width=True)
    


