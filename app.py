import streamlit as st
import pandas as pd
import plotly.express as px
import numpy as np

st.set_page_config(page_title="Employee Dashboard", layout="wide")

st.title("Employee Dashboard")
st.write("Hello Rack! Your dashboard is ready")

@st.cache_data
def load_data(path):
    df = pd.read_csv(path)
    # basic cleaning
    df['Salary_USD'] = pd.to_numeric(df['Salary_USD'], errors='coerce')
    df['Age'] = pd.to_numeric(df['Age'], errors='coerce')
    df.dropna(subset=['Salary_USD','Age'], inplace=True)
    return df

df = load_data("Salary_Dataset.csv")

# Sidebar filters
st.sidebar.header("Filters")
cities = ["All"] + sorted(df['City'].dropna().unique().tolist())
selected_city = st.sidebar.selectbox("City", cities)
min_age, max_age = int(df['Age'].min()), int(df['Age'].max())
age_range = st.sidebar.slider("Age range", min_age, max_age, (min_age, max_age))
education_opts = ["All"] + sorted(df['Education'].dropna().unique().tolist())
selected_education = st.sidebar.selectbox("Education", education_opts)

# Apply filters
filtered = df.copy()
if selected_city != "All":
    filtered = filtered[filtered['City'] == selected_city]
if selected_education != "All":
    filtered = filtered[filtered['Education'] == selected_education]
filtered = filtered[(filtered['Age'] >= age_range[0]) & (filtered['Age'] <= age_range[1])]

# Metrics
col1, col2, col3, col4 = st.columns([1,1,1,1])
col1.metric("Employees", len(filtered))
col2.metric("Avg Salary", f"${filtered['Salary_USD'].mean():.2f}")
col3.metric("Median Salary", f"${filtered['Salary_USD'].median():.2f}")
col4.metric("Avg Age", f"{filtered['Age'].mean():.1f}")

# Charts
with st.expander("Charts"):
    fig1 = px.histogram(filtered, x="Salary_USD", nbins=30, title="Salary Distribution")
    st.plotly_chart(fig1, use_container_width=True)

    fig2 = px.scatter(filtered, x="Age", y="Salary_USD", color="Education",
                      hover_data=['City', 'Gender'], title="Salary vs Age")
    st.plotly_chart(fig2, use_container_width=True)

    # group by education bar chart
    edu_group = filtered.groupby("Education")['Salary_USD'].mean().reset_index().sort_values("Salary_USD", ascending=False)
    fig3 = px.bar(edu_group, x="Education", y="Salary_USD", title="Avg Salary by Education")
    st.plotly_chart(fig3, use_container_width=True)

# Data preview and download
st.write("### Filtered Data (first 200 rows)")
st.dataframe(filtered.head(200))

csv = filtered.to_csv(index=False).encode('utf-8')
st.download_button("Download filtered data", csv, "filtered_data.csv", "text/csv")
