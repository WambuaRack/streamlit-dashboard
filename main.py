import streamlit as st  
import pandas as pd 
import plotly.express as px 

# Title
st.title("My Employee Dashboard")
st.write("Hello Rack! Your Dashboard is ready")

# Load Data
df = pd.read_csv("Salary_Dataset.csv")

# Sidebar Filter
City = df['City'].unique()
selected_city = st.sidebar.selectbox("Select City", City)

# Filtered Data
filtered_df = df[df["City"] == selected_city]

# KPI Metrics
avg_salary = filtered_df["Salary_USD"].mean()
max_salary = filtered_df["Salary_USD"].max()
min_salary = filtered_df["Salary_USD"].min()

col1, col2, col3 = st.columns(3)
col1.metric("Average Salary", f"${avg_salary:,.0f}")
col2.metric("Highest Salary", f"${max_salary:,.0f}")
col3.metric("Lowest Salary", f"${min_salary:,.0f}")

# Filtered Data Preview
st.write("### Filtered Employee Data")
st.dataframe(filtered_df)

# Charts in Columns
c1, c2 = st.columns(2)

with c1:
    fig1 = px.line(filtered_df, x="Age", y="Salary_USD", title="Salary by Age")
    st.plotly_chart(fig1)

with c2:
    fig2 = px.histogram(filtered_df, x="Age", title="Age Distribution")
    st.plotly_chart(fig2)

# Second Row of Charts (Optional)
c3, c4 = st.columns(2)

with c3:
    fig3 = px.box(filtered_df, x="Gender", y="Salary_USD", title="Salary by Gender")
    st.plotly_chart(fig3)

with c4:
    fig4 = px.bar(filtered_df, x="Education", y="Salary_USD", title="Salary by Education")
    st.plotly_chart(fig4)
