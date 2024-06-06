# // $ streamlit run app.py to run it on the browser
import pandas as pd
import plotly.express as px
import streamlit as st
import os
file_directory = os.path.dirname(os.path.abspath(__file__))

path = os.path.join(file_directory, '../../../data/Datafiniti_Fast_Food_Restaurants_Jun19.csv')
df = pd.read_csv (path)
dfres = df[['name', 'province']].value_counts().reset_index().head(100)


st.title('Fast Food Count Across the US')
st.write ('Built by [Iris Otano](https://www.linkedin.com/in/irisotano/)')
fig = px.bar(
    data_frame=dfres, x='province', y='count',color='name', facet_col='name', facet_col_wrap=3, height=1000)


st.plotly_chart(fig)


dfres