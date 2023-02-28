import streamlit as st
import matplotlib.pyplot as plt
import pandas as pd
import plotly.express as px
import os
from matplotlib import image
st.title("stars in our universe")
FILE_DIR = os.path.dirname(os.path.abspath(__file__))
# absolute path to this file's root directory
PARENT_DIR = os.path.join(FILE_DIR, os.pardir)
# absolute path of directory_of_interest
dir_of_interest = os.path.join(PARENT_DIR, "resources")

IMAGE_PATH = os.path.join(dir_of_interest, "images", "Galaxy_stars.jpg")
DATA_PATH = os.path.join(dir_of_interest, "data", "stars.csv")
img=image.imread(IMAGE_PATH)
st.image(img,width=450)
df=pd.read_csv(DATA_PATH)
st.dataframe(df)


st.write(df.shape)

col1, col2 = st.columns(2)

fig_1 = px.histogram(df['Temperature (K)'])
col2.plotly_chart(fig_1, use_container_width=True)
fig_2 = px.box(df['Temperature (K)'])
col2.plotly_chart(fig_2, use_container_width=True)








