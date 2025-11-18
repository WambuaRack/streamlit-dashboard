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

