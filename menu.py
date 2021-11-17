# -*- coding: utf-8 -*-
"""
Created on Wed Sep 22 11:51:21 2021

@author: Acer
"""
#%%

import os
import base64
import pandas as pd
import numpy as np
import streamlit as st
import plotly_express as px
import matplotlib.pyplot as plt
st.subheader("Importing the dataset")

st.set_option('deprecation.showfileUploaderEncoding', False)

uploaded_file = st.file_uploader(label="Upload your csv or excel file. (200 MB max)",
                         type=['csv','xlsx'])

global df
if uploaded_file is not None:
    print(uploaded_file)
    print("hello! file is uploaded")
    try:
        df = pd.read_csv(uploaded_file)
    except Exception as e:
        print(e)
        df = pd.read_excel(uploaded_file)
        
try:
    st.write("uploaded file will show above")
except Exception as e:
    print(e)
    st.subheader("Error shows because dataset is not uploaded yet or need to upload to correct file type.")

#df = pd.read_csv(uploaded_file)
#st.write(df)
#st.dataframe(df=df)


check = st.sidebar.checkbox('reveal data')
print(check)
if check:
    st.write(df)

check1 = st.sidebar.checkbox('reveal the basic description of data')
print(check1)
if check1:
    
    bar = st.sidebar.selectbox("description of the dataset :", ['head','description','null','datatypes'])
    print(bar)
    if bar == 'head':
        st.write("head of the dataset:",df.head())
    elif bar == 'description':
        st.write("description of the dataset:",df.describe().T)
    elif bar == 'null':
        st.write("checking the Null value of the dataset:",df.isnull().sum())
    elif bar == 'datatypes':
        st.write("datatype of  the dataset:",df.dtypes)



check2 = st.sidebar.checkbox("basic statistics of the dataset")
print(check2)
if check2:
    button = st.sidebar.selectbox("stats:",['means','median','sum','minimum','maximum','count','variance','standard deviation','mean absolute devition'])
    print(button)
    if button == 'means':
        st.write('means',df.mean())
    elif button == 'median':
        st.write('median',df.median())
    elif button == 'sum':
        st.write('sum of columns',df.sum())
    elif button == 'minimum':
        st.write('minimum of columns',df.min())
    elif button == 'maximum':
        st.write('maximum of columns',df.max())
    elif button == 'count':
        st.write('count of columns',df.count())
    elif button == 'variance':
        st.write('variance of columns',df.var())
    elif button == 'standard deviation':
        st.write('standard deviation of columns',df.std())
    elif button == 'mean absolute devition':
        st.write('mean absulote deviation of the columns',df.mad())
    

#"""I have to add multiple graph options and their options to represent graphs."""        
check3 = st.sidebar.checkbox("select the option for the graph you want to see!")
print(check3)
if check3:
    button1 = st.sidebar.selectbox('charts types: ',['pie chart','bar chart','histogram','box plot','scatter plot','line graph','all line plot','all area plot'])
    print(button1)
    if button1 == 'pie chart':
        st.write('select the options')
        x = st.selectbox('select the numeric values.',df.columns)
        y = st.selectbox('select the categorical values', df.columns)
        fig = px.pie(df, values=x, names=y)
        #fig.show()
        fig.update_layout(width=800)
        st.write(fig)
    elif button1 == 'bar chart':
        st.write('select the options')
        x_axis = st.selectbox('enter the categorical values', df.columns)
        y_axis = st.selectbox('enter the numerical values', df.columns)
        fig = px.bar(df,x=x_axis,y=y_axis)
        st.write(fig)
    elif button1 == 'histogram':
        x_axis = st.selectbox('enter the numerical variable', df.columns)
        #y = st.slider('number of bins',3, 50)
        fig = px.histogram(df,x=x_axis)
        st.write(fig)
    elif button1 == 'box plot':
        x_axis =st.selectbox("enter the numerical values/columns", df.columns)
        #st.subheader('Optional')
        y_axis = st.selectbox('categorical variable',df.columns)
        fig = px.box(df,y = x_axis,x=y_axis)
        st.write(fig)
        """need to work on scatter plot"""
    elif button1 == 'scatter plot':
        x_axis = st.selectbox('enter the numerical values 1', df.columns)
        y_axis = st.selectbox('enter the numerical values 2', df.columns)
        #r =st.slider("size of points", 1,10)
        fig = px.scatter(df,x=x_axis,y=y_axis)
        st.write(fig)
    elif button1 == 'line graph':
        x_axis = st.selectbox("enter the variable(s)",df.columns)
        df = df.sort_values(by=x_axis)
        y_axis = st.selectbox('index values', df.columns)
        #a = st.slider("Size of the lines",1,5)
        fig = px.line(df,x=x_axis, y= y_axis)
        st.write(fig)
    elif button1 == 'all line plot':
        st.line_chart(df)
    elif button1 == 'all area plot':
        #check == st.selectbox('graph name')
        st.area_chart(df)


#st.write("dataset's columns name")
#column_list = df.columns.tolist()
#column_list.sort()
check4 = st.sidebar.checkbox("select the option for the unique values!")
print(check4)
column_list = df.columns.tolist()
column_list.sort()
if check4:
    button1 = st.sidebar.selectbox('Select Column Name Here', column_list)
    #st.write(f"Selected Column: {button1}")

    unique_list = df[button1].unique()
    #st.write(unique_list)

    selected_unique_values = st.selectbox('Choose The Unique Value', unique_list)
    st.write(f'You want dataframe for unique value: {selected_unique_values}')

    df1 = df[df[button1]==selected_unique_values]
    #if st.checkbox('Show DataFrame'):
    st.write('Here The Unique DataFrame')
    st.write(df1)
        
    

    def filedownload(df):
        csv = df1.to_csv(index=False)
        b64 = base64.b64encode(csv.encode()).decode() 
        href = f'<a href="data:file/csv;base64,{b64}" download="dataframe.csv">Download CSV File</a>'
        return href
    
    st.markdown(filedownload(df1), unsafe_allow_html=True)      
      