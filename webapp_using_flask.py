import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

st.header("document verifier")
upload_file=st.file_uploader("upload file:")
if upload_file is not None:   # Read the file to a dataframe using pandas
   df = pd.read_csv(upload_file)
   # Create a section for the dataframe statistics
st.header('Statistics of Dataframe')
st.write(df.describe())# Create a section for the dataframe header
st.header('Header of Dataframe')
st.write(df.head())
fig, ax = plt.subplots(1,1)
ax.scatter(x=df['Present_Price'], y=df['Kms_Driven'])
ax.set_xlabel('Present_Price')
ax.set_ylabel('Kms_Driven')
st.pyplot(fig)