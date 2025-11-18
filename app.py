import streamlit as st  
import pandas as pd 
st.title("My Employee Dashboard")
st.write("Hello Rack! Your Dashboard is ready")


df=pd.read_csv("Salary_Dataset.csv")
st.write("### Raw Data Preview")
st.dataframe(df)

City=df['City'].unique()
selected_city=st.selectbox("Select City", City)
filtered_df =df[df["City"]==selected_city  ]
st.write("### Filtered Data")

st.dataframe(filtered_df)

import plotly.express as px 
fig = px.line(filtered_df, x="Age", y="Salary_USD", title="Salary by Age")

st.plotly_chart(fig)

fig =px.histogram(df, x="Age", )

st.plotly_chart(fig)