import pandas as pd
import streamlit as st
import plotly.express as px 

car_data = pd.read_csv('vehicles_us.csv') # leer los datos

print(car_data.head())

hist_button = st.button('Construir Histograma')

if hist_button:
    
    st.write('Creación de un histograma con los valores del odometro de los autos')
    fig = px.histogram(car_data,x='odometer')
    st.plotly.fig
    


