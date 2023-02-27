import streamlit as st
import matplotlib.pyplot as plt
from PIL import Image
import seaborn as sns
import pandas as pd
import plotly.express as px
st.title("stars in our universe")
image=Image.open('C:\\Users\\Lenovo\\OneDrive\\Desktop\\Task1\\project_1\\resources\\images\\Galaxy_stars.jpg')
st.image(image, caption="Stars in our Univrse",width=500)
df=pd.read_csv("C:\\Users\\Lenovo\\OneDrive\\Desktop\\Task1\\project_1\\resources\\data\\stars.csv")
st.dataframe(df)
st.write(df.shape)

col1, col2 = st.columns(2)

fig_1 = px.histogram(df['Temperature (K)'])
col2.plotly_chart(fig_1, use_container_width=True)
fig_2 = px.box(df['Temperature (K)'])
col2.plotly_chart(fig_2, use_container_width=True)









