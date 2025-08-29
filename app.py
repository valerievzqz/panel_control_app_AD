import streamlit as st
import pandas as pd
import plotly.express as px

car_data=pd.read_csv("vehicles_us.csv")
st.header("vehicles in the US - Graphs")
hist_check=st.checkbox("create histogram") #it can algo be a st.button
if hist_check:
    st.write("creating histogram of a data set about cars in the US")
    
    fig=px.histogram(car_data,x="odometer") #histograma
    st.plotly_chart(fig,user_container_width=True)

disp_check=st.checkbox("create dispersion plot")
if disp_check:
    st.write("creating dispersion plot of a data set about cars in the US")
    fig2=px.scatter(car_data,x="odometer",y="price") #dispersion
    st.plotly_chart(fig2,user_container_width=True)


