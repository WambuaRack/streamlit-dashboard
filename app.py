import streamlit as st  
import pandas as pd 
st.title("My Employee Dashboard")
st.write("Hello Rack! Your Dashboard is ready")


df=pd.read_csv("Salary_Dataset.csv")