### 📄 c:\Users\Administrator\Desktop\dashboard\main.py
*Saved at: 11/18/2025, 11:45:26 AM*

**[ADDED]**
```
1     import streamlit as st  
2     import pandas as pd 
3     import plotly.express as px 
4     
5     # Title
6     st.title("My Employee Dashboard")
7     st.write("Hello Rack! Your Dashboard is ready")
8     
9     # Load Data
10    df = pd.read_csv("Salary_Dataset.csv")
11    
12    # Sidebar Filter
13    City = df['City'].unique()
14    selected_city = st.sidebar.selectbox("Select City", City)
15    
16    # Filtered Data
17    filtered_df = df[df["City"] == selected_city]
18    
19    # KPI Metrics
20    avg_salary = filtered_df["Salary_USD"].mean()
21    max_salary = filtered_df["Salary_USD"].max()
22    min_salary = filtered_df["Salary_USD"].min()
23    
24    col1, col2, col3 = st.columns(3)
25    col1.metric("Average Salary", f"${avg_salary:,.0f}")
26    col2.metric("Highest Salary", f"${max_salary:,.0f}")
27    col3.metric("Lowest Salary", f"${min_salary:,.0f}")
28    
29    # Filtered Data Preview
30    st.write("### Filtered Employee Data")
31    st.dataframe(filtered_df)
32    
33    # Charts in Columns
34    c1, c2 = st.columns(2)
35    
36    with c1:
37        fig1 = px.line(filtered_df, x="Age", y="Salary_USD", title="Salary by Age")
38        st.plotly_chart(fig1)
39    
40    with c2:
41        fig2 = px.histogram(filtered_df, x="Age", title="Age Distribution")
42        st.plotly_chart(fig2)
43    
44    # Second Row of Charts (Optional)
45    c3, c4 = st.columns(2)
46    
47    with c3:
48        fig3 = px.box(filtered_df, x="Gender", y="Salary_USD", title="Salary by Gender")
49        st.plotly_chart(fig3)
50    
51    with c4:
52        fig4 = px.bar(filtered_df, x="Education", y="Salary_USD", title="Salary by Education")
53        st.plotly_chart(fig4)
```

---

### 📄 c:\Users\Administrator\Desktop\dashboard\app.py
*Saved at: 11/18/2025, 11:18:04 AM*

**[REMOVED]**
```
(from line ~20)
df = load_data("data/Salary_Dataset.csv")

```
**[ADDED]**
```
20    df = load_data("Salary_Dataset.csv")
```

---

### 📄 c:\Users\Administrator\Desktop\dashboard\app.py
*Saved at: 11/18/2025, 11:17:33 AM*

**[REMOVED]**
```
(from line ~1)
import streamlit as st  
import pandas as pd 
st.title("My Employee Dashboard")
st.write("Hello Rack! Your Dashboard is ready")

```
**[ADDED]**
```
1     import streamlit as st
2     import pandas as pd
3     import plotly.express as px
4     import numpy as np
```
**[ADDED]**
```
6     st.set_page_config(page_title="Employee Dashboard", layout="wide")
```
**[REMOVED]**
```
(from line ~8)
df=pd.read_csv("Salary_Dataset.csv")
st.write("### Raw Data Preview")
st.dataframe(df)
st.table(df.head(5))
City=df['City'].unique()
selected_city=st.selectbox("Select City", City)
filtered_df =df[df["City"]==selected_city  ]
st.write("### Filtered Data")

```
**[ADDED]**
```
8     st.title("Employee Dashboard")
9     st.write("Hello Rack! Your dashboard is ready")
```
**[REMOVED]**
```
(from line ~11)
st.dataframe(filtered_df)

```
**[ADDED]**
```
11    @st.cache_data
12    def load_data(path):
13        df = pd.read_csv(path)
14        # basic cleaning
15        df['Salary_USD'] = pd.to_numeric(df['Salary_USD'], errors='coerce')
16        df['Age'] = pd.to_numeric(df['Age'], errors='coerce')
17        df.dropna(subset=['Salary_USD','Age'], inplace=True)
18        return df
```
**[REMOVED]**
```
(from line ~20)
import plotly.express as px 
fig = px.line(filtered_df, x="Age", y="Salary_USD", title="Salary by Age")

```
**[ADDED]**
```
20    df = load_data("data/Salary_Dataset.csv")
```
**[REMOVED]**
```
(from line ~22)
st.plotly_chart(fig)

fig =px.histogram(df, x="Age", )

st.plotly_chart(fig)

import plotly.express as px

fig = px.scatter(df, x="Age", y="Salary_USD", color="City",
                 hover_data=['Education', 'Gender'],
                 title="Salary vs Age by City")
st.plotly_chart(fig, use_container_width=True)
# sidebar controls

```
**[ADDED]**
```
22    # Sidebar filters
```
**[REMOVED]**
```
(from line ~24)
cities = df['City'].sort_values().unique()
selected_city = st.sidebar.selectbox("City", options=["All"] + list(cities))


```
**[ADDED]**
```
24    cities = ["All"] + sorted(df['City'].dropna().unique().tolist())
25    selected_city = st.sidebar.selectbox("City", cities)
```
**[REMOVED]**
```
(from line ~27)
age_range = st.sidebar.slider("Age range", min_age, max_age, (25, 45))

```
**[ADDED]**
```
27    age_range = st.sidebar.slider("Age range", min_age, max_age, (min_age, max_age))
28    education_opts = ["All"] + sorted(df['Education'].dropna().unique().tolist())
29    selected_education = st.sidebar.selectbox("Education", education_opts)
```
**[REMOVED]**
```
(from line ~31)
# apply filters

```
**[ADDED]**
```
31    # Apply filters
```
**[ADDED]**
```
35    if selected_education != "All":
36        filtered = filtered[filtered['Education'] == selected_education]
```
**[REMOVED]**
```
(from line ~39)
st.write(f"Filtered rows: {len(filtered)}")
st.dataframe(filtered.head(50))

```
**[ADDED]**
```
39    # Metrics
40    col1, col2, col3, col4 = st.columns([1,1,1,1])
41    col1.metric("Employees", len(filtered))
42    col2.metric("Avg Salary", f"${filtered['Salary_USD'].mean():.2f}")
43    col3.metric("Median Salary", f"${filtered['Salary_USD'].median():.2f}")
44    col4.metric("Avg Age", f"{filtered['Age'].mean():.1f}")
45    
46    # Charts
47    with st.expander("Charts"):
48        fig1 = px.histogram(filtered, x="Salary_USD", nbins=30, title="Salary Distribution")
49        st.plotly_chart(fig1, use_container_width=True)
50    
51        fig2 = px.scatter(filtered, x="Age", y="Salary_USD", color="Education",
52                          hover_data=['City', 'Gender'], title="Salary vs Age")
53        st.plotly_chart(fig2, use_container_width=True)
54    
55        # group by education bar chart
56        edu_group = filtered.groupby("Education")['Salary_USD'].mean().reset_index().sort_values("Salary_USD", ascending=False)
57        fig3 = px.bar(edu_group, x="Education", y="Salary_USD", title="Avg Salary by Education")
58        st.plotly_chart(fig3, use_container_width=True)
59    
60    # Data preview and download
61    st.write("### Filtered Data (first 200 rows)")
62    st.dataframe(filtered.head(200))
63    
64    csv = filtered.to_csv(index=False).encode('utf-8')
65    st.download_button("Download filtered data", csv, "filtered_data.csv", "text/csv")
```

---

### 📄 c:\Users\Administrator\Desktop\dashboard\app.py
*Saved at: 11/18/2025, 11:03:12 AM*

**[ADDED]**
```
33    # sidebar controls
34    st.sidebar.header("Filters")
35    cities = df['City'].sort_values().unique()
36    selected_city = st.sidebar.selectbox("City", options=["All"] + list(cities))
37    
38    min_age, max_age = int(df['Age'].min()), int(df['Age'].max())
39    age_range = st.sidebar.slider("Age range", min_age, max_age, (25, 45))
40    
41    # apply filters
42    filtered = df.copy()
43    if selected_city != "All":
44        filtered = filtered[filtered['City'] == selected_city]
45    filtered = filtered[(filtered['Age'] >= age_range[0]) & (filtered['Age'] <= age_range[1])]
46    
47    st.write(f"Filtered rows: {len(filtered)}")
48    st.dataframe(filtered.head(50))
```

---

### 📄 c:\Users\Administrator\Desktop\dashboard\app.py
*Saved at: 11/18/2025, 11:01:30 AM*

**[REMOVED]**
```
(from line ~25)
st.plotly_chart(fig)
```
**[ADDED]**
```
25    st.plotly_chart(fig)
26    
27    import plotly.express as px
28    
29    fig = px.scatter(df, x="Age", y="Salary_USD", color="City",
30                     hover_data=['Education', 'Gender'],
31                     title="Salary vs Age by City")
32    st.plotly_chart(fig, use_container_width=True)
```

---

### 📄 c:\Users\Administrator\Desktop\dashboard\app.py
*Saved at: 11/18/2025, 11:00:14 AM*

**[REMOVED]**
```
(from line ~10)


```
**[ADDED]**
```
10    st.table(df.head(5))
```

---

### 📄 c:\Users\Administrator\Desktop\dashboard\app.py
*Saved at: 11/18/2025, 10:57:04 AM*

**[ADDED]**
```
24    
```

---

### 📄 c:\Users\Administrator\Desktop\dashboard\app.py
*Saved at: 11/18/2025, 10:56:06 AM*

**[ADDED]**
```
21    st.plotly_chart(fig)
```

---

### 📄 c:\Users\Administrator\Desktop\dashboard\app.py
*Saved at: 11/18/2025, 10:55:45 AM*

**[REMOVED]**
```
(from line ~19)
fig=px.line(df,x="Age", y="Salary_USD", title="EDucation by Salary")
st.plotly_chart(fig)

```
**[ADDED]**
```
19    fig = px.line(filtered_df, x="Age", y="Salary_USD", title="Salary by Age")
```
**[ADDED]**
```
21    
```

---

### 📄 c:\Users\Administrator\Desktop\dashboard\app.py
*Saved at: 11/18/2025, 10:53:26 AM*

**[ADDED]**
```
20    st.plotly_chart(fig)
21    
22    fig =px.histogram(df, x="Age", )
```

---

### 📄 c:\Users\Administrator\Desktop\dashboard\app.py
*Saved at: 11/18/2025, 10:52:12 AM*

**[REMOVED]**
```
(from line ~19)
fig=px.line(df,x="Education", y="Salary_USD", title="EDucation by Salary")

```
**[ADDED]**
```
19    fig=px.line(df,x="Age", y="Salary_USD", title="EDucation by Salary")
```

---

### 📄 c:\Users\Administrator\Desktop\dashboard\app.py
*Saved at: 11/18/2025, 10:51:39 AM*

**[REMOVED]**
```
(from line ~19)
fig=px.line(x="Education", y="Salary_USD", title="EDucation by Salary")

```
**[ADDED]**
```
19    fig=px.line(df,x="Education", y="Salary_USD", title="EDucation by Salary")
```

---

### 📄 c:\Users\Administrator\Desktop\dashboard\app.py
*Saved at: 11/18/2025, 10:50:08 AM*

**[REMOVED]**
```
(from line ~19)
fig=px.line(x="Education", y="Salary_USD", title="EDucation by Salary")
```
**[ADDED]**
```
19    fig=px.line(x="Education", y="Salary_USD", title="EDucation by Salary")
20    st.plotly_chart(fig)
```

---

### 📄 c:\Users\Administrator\Desktop\dashboard\app.py
*Saved at: 11/18/2025, 10:49:47 AM*

**[REMOVED]**
```
(from line ~19)
fig=px.line(x="Education", y="Salary_USD")
```
**[ADDED]**
```
19    fig=px.line(x="Education", y="Salary_USD", title="EDucation by Salary")
```

---

### 📄 c:\Users\Administrator\Desktop\dashboard\app.py
*Saved at: 11/18/2025, 10:49:19 AM*

**[REMOVED]**
```
(from line ~19)
fig=px.line(x="Education", y=)
```
**[ADDED]**
```
19    fig=px.line(x="Education", y="Salary_USD")
```

---

### 📄 c:\Users\Administrator\Desktop\dashboard\app.py
*Saved at: 11/18/2025, 10:49:05 AM*

**[REMOVED]**
```
(from line ~19)
fig=px.line(x=)
```
**[ADDED]**
```
19    fig=px.line(x="Education", y=)
```

---

### 📄 c:\Users\Administrator\Desktop\dashboard\app.py
*Saved at: 11/18/2025, 10:48:39 AM*

**[ADDED]**
```
19    fig=px.line(x=)
```

---

### 📄 c:\Users\Administrator\Desktop\dashboard\app.py
*Saved at: 11/18/2025, 10:47:47 AM*

**[REMOVED]**
```
(from line ~16)
st.dataframe(filtered_df)
```
**[ADDED]**
```
16    st.dataframe(filtered_df)
17    
18    import plotly.express as px 
```

---

### 📄 c:\Users\Administrator\Desktop\dashboard\app.py
*Saved at: 11/18/2025, 10:46:03 AM*

**[REMOVED]**
```
(from line ~13)
filtered_df =df[df["City"]]==selected_city

```
**[ADDED]**
```
13    filtered_df =df[df["City"]==selected_city  ]
```

---

### 📄 c:\Users\Administrator\Desktop\dashboard\app.py
*Saved at: 11/18/2025, 10:45:21 AM*

**[ADDED]**
```
14    st.write("### Filtered Data")
15    
16    st.dataframe(filtered_df)
```

---

### 📄 c:\Users\Administrator\Desktop\dashboard\app.py
*Saved at: 11/18/2025, 10:44:33 AM*

**[REMOVED]**
```
(from line ~13)
filtered_df =df[df["City"]]==
```
**[ADDED]**
```
13    filtered_df =df[df["City"]]==selected_city
```

---

### 📄 c:\Users\Administrator\Desktop\dashboard\app.py
*Saved at: 11/18/2025, 10:44:16 AM*

**[REMOVED]**
```
(from line ~12)
selected_city=st.selectbox("Select City", City)
```
**[ADDED]**
```
12    selected_city=st.selectbox("Select City", City)
13    filtered_df =df[df["City"]]==
```

---

### 📄 c:\Users\Administrator\Desktop\dashboard\app.py
*Saved at: 11/18/2025, 10:43:16 AM*

**[ADDED]**
```
12    selected_city=st.selectbox("Select City", City)
```

---

### 📄 c:\Users\Administrator\Desktop\dashboard\app.py
*Saved at: 11/18/2025, 10:42:38 AM*

**[REMOVED]**
```
(from line ~11)
years=df['City']
```
**[ADDED]**
```
11    City=df['City'].unique()
```

---

### 📄 c:\Users\Administrator\Desktop\dashboard\app.py
*Saved at: 11/18/2025, 10:42:10 AM*

**[REMOVED]**
```
(from line ~9)
st.dataframe(df)
```
**[ADDED]**
```
9     st.dataframe(df)
10    
11    years=df['City']
```

---

### 📄 c:\Users\Administrator\Desktop\dashboard\app.py
*Saved at: 11/18/2025, 10:40:50 AM*

**[REMOVED]**
```
(from line ~8)
st.write("#Raw Data Preview")

```
**[ADDED]**
```
8     st.write("### Raw Data Preview")
```

---

### 📄 c:\Users\Administrator\Desktop\dashboard\app.py
*Saved at: 11/18/2025, 10:40:09 AM*

**[ADDED]**
```
8     st.write("#Raw Data Preview")
9     st.dataframe(df)
```

---

### 📄 c:\Users\Administrator\Desktop\dashboard\app.py
*Saved at: 11/18/2025, 10:39:22 AM*

**[REMOVED]**
```
(from line ~7)
df=pd.read_csv("Salary_Dataset.csv")
```
**[ADDED]**
```
7     df=pd.read_csv("Salary_Dataset.csv")
```

---

### 📄 c:\Users\Administrator\Desktop\dashboard\app.py
*Saved at: 11/18/2025, 10:39:06 AM*

**[REMOVED]**
```
(from line ~7)
df=pd.read_csv("")
```
**[ADDED]**
```
7     df=pd.read_csv("Salary_Dataset.csv")
```

---

### 📄 c:\Users\Administrator\Desktop\dashboard\app.py
*Saved at: 11/18/2025, 10:38:50 AM*

**[REMOVED]**
```
(from line ~2)


```
**[ADDED]**
```
2     import pandas as pd 
```
**[REMOVED]**
```
(from line ~4)
st.write("Hello Rack! Your Dashboard is ready")
```
**[ADDED]**
```
4     st.write("Hello Rack! Your Dashboard is ready")
5     
6     
7     df=pd.read_csv("")
```

---

### 📄 c:\Users\Administrator\Desktop\dashboard\app.py
*Saved at: 11/18/2025, 10:37:25 AM*

**[REMOVED]**
```
(from line ~3)
st.title("My Employee Dashboard")
```
**[ADDED]**
```
3     st.title("My Employee Dashboard")
4     st.write("Hello Rack! Your Dashboard is ready")
```

---

### 📄 c:\Users\Administrator\Desktop\dashboard\app.py
*Saved at: 11/18/2025, 10:36:45 AM*

**[ADDED]**
```
1     import streamlit as st  
2     
3     st.title("My Employee Dashboard")
```

---

