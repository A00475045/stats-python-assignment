# -*- coding: utf-8 -*-
"""
Created on Fri Dec 15 20:12:21 2023

@author: RanjitPandey1605
"""



import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt



st.title('Q3')
csv_file = st.file_uploader("select a csv file:", type="csv")


    
df = pd.read_csv(csv_file)

if 'Age' in df.columns and 'Name' in df.columns:
    st.write("This Graph shows the ages of individuals ")
  
    fig, ax = plt.subplots()
    
    ax.hist(df['Age'], bins=100, edgecolor='black')
    ax.set_xlabel('Age')        
    ax.set_ylabel('Name')
    ax.set_title('This Graph shows the ages of individuals')
    
    st.pyplot(fig)
        
else:
        st.error("Invalid File Format")
        
        

